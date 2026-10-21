# Privacy Policy — Frameworthy

**Effective date:** 2026-10-20
**Developer:** Matthias Morath

Frameworthy is a Mac app that processes the videos you open in it —
**entirely on your Mac**.

!!! note "In short"
    No account, no server, no analytics, no advertising, no tracking. Your
    videos, audio and text never leave your Mac. The app's only own network
    connection is the one-time download of the speaker models from Hugging Face,
    and it carries no user data.

## What we collect

**Nothing.** The app has **no backend**, sends data to **no server** and contains
**no analytics, advertising or tracking**. The developer receives no data from the app.

## What the app processes, on your Mac

- **Videos you open** — read from disk, converted and written to the output folder
  you choose (default: `Movies/Frameworthy`). The app runs in the macOS App
  Sandbox: it can only open the files and folders you choose, and it remembers that
  permission so queued videos continue after a restart.
- **Spoken text** — recognized with Apple's on-device speech recognition. Audio never
  leaves your Mac. macOS may download a speech model for the chosen language once;
  that download contains no user data.
- **Corrections and chapter titles** — produced on-device by Apple Intelligence.
  No text is sent to a cloud model.
- **Translations** — on-device with Apple's Translation framework; macOS may download
  language packs once, after you confirm.
- **Speakers** — told apart on-device. The speaker models are downloaded once from
  Hugging Face (`FluidInference/speaker-diarization-coreml`); that download sends no
  user data. It is the only network connection the app itself makes.
- **Transcripts, subtitles and chapters** — saved next to your converted videos.

## What the app stores

Everything stays in the app's container on your Mac
(`~/Library/Containers/com.mmorath.frameworthy`): your settings, the job queue and
a local log file with file paths and processing details. Nothing of it is uploaded.
Deleting the app removes the container.

## Sharing

None. The app shares no data with the developer or any third party.

## Children

The app collects no data from anyone, including children.

## Changes

If the app's data handling changes, this page is updated and the effective date
changes.

## Contact

See [Support](../support/index.md).
