# Support — Leaf Relief

Help for [Leaf Relief](../index.md), the paperless archive for your Mac. Found a bug
or have a question? Here's how to get in touch.

## Contact

!!! note "Contact address"
    **Email:** `kubisch-gemacht3p@icloud.com` (subject starting with “Leaf Relief”)

When reporting a problem, the quickest way is to **attach the log** (see
[Where is the log?](#where-is-the-log)) and add a line on what you did and what you
expected to happen.

## Requirements

- macOS 26 or newer on a Mac with Apple silicon.
- For suggestions with **Apple Intelligence**: turned on in System Settings › Apple
  Intelligence & Siri. Without it, simple rules suggest; the app says when it is off.

## Getting started

1. On first launch, choose a folder as the **archive** – for example a new folder
   “Archive” in Documents.
2. Optionally choose a second folder as the **inbox folder**.
3. Scan, or drop a PDF or a photo of a document into the inbox folder. Within a few
   seconds it is filed into the archive with a searchable text layer and appears in
   the **Inbox** list.
4. Select it, click **Suggest**, check the suggestions and click **Done**.

## Frequently asked questions

### My scanner does not show up.
Leaf Relief uses the scanners macOS knows itself: AirScan scanners on the same network
and USB scanners with a macOS driver (the same ones Image Capture shows). If yours is
not listed, let its own software save PDFs into the **inbox folder** you set in
Leaf Relief — every file there is filed automatically.

### Which files does the inbox folder accept?
PDF, JPEG, PNG, HEIC and TIFF. PDFs that already contain text are taken over
unchanged; images and image-only PDFs get a searchable text layer. A file that cannot
be read stays where it is and is noted in the log.

### Where are my documents?
In the archive folder you chose, sorted into the subfolders and file names you set up
(File › Set Up Filing). The files are ordinary PDFs; tags are Finder tags.

### The app says it lost access to a folder.
macOS only lets the app open folders you chose. If a folder was renamed, moved, or its
disk is not connected, click “Choose Again” in the window or in Settings.

### Which languages does Leaf Relief understand?
The app and text recognition work in English, German, French and Spanish. Apple
Intelligence answers in the language of the document. The simple rules (used without
Apple Intelligence) and natural-language search understand German and English
documents.

### Does Leaf Relief need the internet?
No. Everything runs on your Mac. The app only connects to scanners on your local
network and — if you switch them on — to the time stamping service freetsa.org, which
receives a checksum, never a document. See the [privacy policy](../privacy/index.md).

### Can I use my documents from the previous version (Scan-Zentrale)?
Yes. In File › Set Up Filing, “Data from Scan-Zentrale” takes over change logs,
suggestions, types, signing key and settings once. The old data stays unchanged.

### Is PDF/A supported?
No. Leaf Relief writes standard PDFs with a searchable text layer.

### Where is the log?
Help › Log. “Send Log” creates a ZIP without document content; your home folder, email
addresses, keys and passwords are replaced.

## Third-party components

Help › Acknowledgements in the app lists every component with its license.

---

See also the [privacy policy](../privacy/index.md).
