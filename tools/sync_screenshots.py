#!/usr/bin/env python3
# =============================================================================
#  sync_screenshots.py — pull the app screenshots into the site, per language
#  Contact: mmorath <maroon_pavers.6t@icloud.com>
#
#  The app repos own their screenshots: each has a UI-test suite that captures
#  the whole set once per language (`make screenshots` there). This site used to
#  receive them by hand, which is how docs/hecate/capture/ ended up showing one
#  un-localized set from July on all four language pages. This script is the
#  hand-copy, written down:
#
#      <app repo>/docs/screenshots/<lang>/<screen-id>.png
#          → docs/assets/screens/<lang>/<site-name>.png,  downscaled to 720 px
#            high (the width the page CSS actually renders; a 1320x2868 device
#            PNG is ~900 KB of payload for a 331 px thumbnail).
#
#  Only the names in SCREENS are touched. The Viewer and tvOS images in the same
#  directories come from other repos and other runs — they are left alone.
#
#  Usage:
#      tools/sync_screenshots.py              # sync every language
#      tools/sync_screenshots.py --lang de    # just one
#      tools/sync_screenshots.py --check      # report staleness, write nothing
#
#  Source repos default to siblings of this one; override with
#  HECATE_CAPTURE_REPO / HECATE_ADMIN_REPO.
#
#  Exit codes: 0 = every mapped image present (and up to date, under --check)
#              1 = a source screenshot was missing, or --check found drift
#              2 = usage / a source repo is not where it should be
# =============================================================================
"""Sync the per-language app screenshots from the app repos into docs/assets."""

from __future__ import annotations

import argparse
import os
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

LANGUAGES = ["en", "de", "fr", "es"]

# The height the site serves. The pages render these ~331 px wide; anything
# larger is bytes the visitor pays for and never sees.
TARGET_HEIGHT = 720

# Where each app repo keeps its per-language doc set. Capture follows the shared
# screenshot spec (docs/screenshots/<lang>/); Admin exports to generated/<lang>/.
REPOS = {
    "capture": ("HECATE_CAPTURE_REPO", "iOS-Hecate-Capture", "docs/screenshots/{lang}"),
    "admin":   ("HECATE_ADMIN_REPO",   "iOS-Hecate-Admin",   "docs/screenshots/generated/{lang}"),
}

# site image name → (app, screen id in that app's doc set)
#
# Keep this list short and load-bearing: every entry is an image some page
# embeds, and a page that embeds an image not listed here will silently keep an
# old one. Referenced from docs/hecate/index*.md and docs/hecate/capture/index*.md.
SCREENS = {
    "capture-assets":   ("capture", "home-outbox"),
    "capture-detail":   ("capture", "asset-detail"),
    "capture-sent":     ("capture", "home-sent"),
    "capture-settings": ("capture", "settings-hub"),
    # The Admin set. `admin-detail` used to map to `04-profile-detail`, a
    # screen the walk no longer produces — the mapping went stale silently,
    # which is exactly the failure this file's header warns about. It now
    # points at the editor, and the Admin page finally has a gallery of its
    # own instead of two images borrowed by the landing page.
    "admin-profiles":   ("admin",   "01-profiles-home"),
    "admin-detail":     ("admin",   "02-editor"),
    "admin-wizard":     ("admin",   "wizard-blocks-picker"),
    "admin-steps":      ("admin",   "12-wizard-blocks-added-list"),
    "admin-review":     ("admin",   "14-wizard-full-review"),
    "admin-broker":     ("admin",   "21-broker-list"),
    # The getting-started page (docs/hecate/getting-started/) walks a reader
    # through broker setup and provisioning. These come from Capture and not
    # from Admin on purpose: the broker screens are HecateKit's, identical in
    # both apps, and Admin's doc set has them in English only — a German page
    # showing an English screenshot is worse than one showing Capture's.
    "gs-broker-connection": ("capture", "settings-broker-connection"),
    "gs-broker-auth":       ("capture", "settings-broker-auth"),
    "gs-broker-share-qr":   ("capture", "settings-broker-share-qr"),
    "gs-provisioning":      ("capture", "dialog-provisioning-confirm"),
}


def die(msg: str, code: int = 2) -> None:
    print(f"sync_screenshots: {msg}", file=sys.stderr)
    raise SystemExit(code)


def png_size(path: Path) -> tuple[int, int]:
    """(width, height) from the IHDR chunk — no image library needed."""
    with path.open("rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        die(f"not a PNG: {path}")
    return struct.unpack(">II", head[16:24])


def resolve_repo(app: str, site: Path) -> Path:
    env_var, sibling, _ = REPOS[app]
    root = Path(os.environ.get(env_var, site.parent / sibling)).expanduser()
    if not root.is_dir():
        die(f"no {app} repo at {root} — clone it next to this one or set {env_var}")
    return root


def source_path(app: str, screen: str, lang: str, site: Path) -> Path:
    _, _, layout = REPOS[app]
    return resolve_repo(app, site) / layout.format(lang=lang) / f"{screen}.png"


def downscale(src: Path, dest: Path) -> None:
    """Copy src to dest at TARGET_HEIGHT. Writes via a temp file so a failed
    resize cannot leave a truncated PNG in the site tree."""
    with tempfile.TemporaryDirectory() as tmp:
        staged = Path(tmp) / dest.name
        shutil.copyfile(src, staged)
        result = subprocess.run(
            ["sips", "--resampleHeight", str(TARGET_HEIGHT), str(staged)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            die(f"sips failed on {src}: {result.stderr.strip()}", 1)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(staged, dest)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lang", default="", help=f"one of {', '.join(LANGUAGES)} (default: all)")
    ap.add_argument("--check", action="store_true",
                    help="report which site images are stale; write nothing")
    args = ap.parse_args()

    site = Path(__file__).resolve().parent.parent
    languages = [args.lang] if args.lang else LANGUAGES
    for lang in languages:
        if lang not in LANGUAGES:
            die(f"unknown language {lang!r} — expected one of {', '.join(LANGUAGES)}")

    exit_code = 0
    for lang in languages:
        print(f"{lang}:")
        for name, (app, screen) in sorted(SCREENS.items()):
            src = source_path(app, screen, lang, site)
            dest = site / "docs" / "assets" / "screens" / lang / f"{name}.png"

            if not src.is_file():
                print(f"  MISSING  {name:18s} ← {app}:{screen} (no {src})",
                      file=sys.stderr)
                exit_code = 1
                continue

            if args.check:
                if not dest.is_file():
                    print(f"  absent   {name:18s} — site has no copy yet")
                    exit_code = 1
                elif dest.stat().st_mtime < src.stat().st_mtime:
                    print(f"  stale    {name:18s} — {app}:{screen} is newer")
                    exit_code = 1
                else:
                    print(f"  ok       {name:18s}")
                continue

            downscale(src, dest)
            w, h = png_size(dest)
            kb = dest.stat().st_size // 1024
            print(f"  {name:18s} ← {app}:{screen}  {w}x{h}, {kb} KB")

    if args.check and exit_code:
        print("\nRun tools/sync_screenshots.py to refresh.", file=sys.stderr)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
