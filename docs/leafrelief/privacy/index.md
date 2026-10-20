# Privacy Policy — Leaf Relief

**Effective date:** 2026-10-21
**Developer:** Matthias Morath

Leaf Relief is a Mac app for a paperless archive. It processes your documents
**entirely on your Mac**.

## What we collect

**Nothing.** The app has **no backend**, **no account**, and contains **no analytics,
advertising or tracking**. The developer receives no data from the app.

## What the app processes, on your Mac

- **Documents** in the archive folder and the inbox folder you choose. The app runs in
  the macOS App Sandbox: it can only open the folders you chose, and it remembers that
  permission.
- **Scans** from a scanner you choose (USB, or AirScan on your local network). The page
  images stay in the app's cache for 14 days so a failed step can be repeated.
- **Text recognition** with Apple's Vision framework, on your Mac.
- **Suggestions** (type, sender, date, amount, deadline …) with Apple Intelligence,
  on-device. No text is sent to a cloud model.
- **Search** with an index in the app's container.
- **Spotlight:** titles, senders, types, tags and text are in this Mac's Spotlight index.
- **Reminders** for deadlines are created only when you click "Create Reminder"; macOS
  asks for permission once.
- **Change log:** changes to documents are signed with a key in this Mac's Secure Enclave
  and recorded in the index and at the file.

## Network

- **Scanners on your local network** (AirScan) are found via Bonjour; macOS asks for
  local network permission.
- **Time stamps (optional, off by default):** if you switch them on, only a checksum
  (SHA-256) of each change-log entry is sent to the time stamping service freetsa.org —
  never the content of a document.

The app makes no other connections.

## Sharing

A document or the log leaves your Mac only when you share it yourself ("Share",
"Send by Email"). The copy carries no tags or types. The log contains steps and file
names, no document content; your home folder, email addresses and keys are replaced on
export.

## Deleting

When you delete the app, macOS removes its container (index, settings, cache). Your
documents in the archive folder stay where they are.

## Contact

Questions: `kubisch-gemacht3p@icloud.com`
