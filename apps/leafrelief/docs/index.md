---
hide:
  - toc
---

# Leaf Relief

*A paperless archive for your Mac*

**Coming soon to the Mac App Store.**

Leaf Relief turns paper into an archive you can search – no account, no cloud,
**entirely on your Mac**. Scan paper or drop files into an inbox folder: the app
recognises the text, files each document under a name you choose, suggests title,
type, sender, date, amount and tags, and finds everything again by full text,
natural language or meaning.

## In one minute

- **Scan or import.** AirScan scanners on your network and USB scanners with a
  macOS driver scan straight into the app; any other scanner, downloads or photos
  go through the inbox folder.
- **Searchable PDFs.** Pages are turned upright, the text is recognised and
  written into the PDF as a searchable layer.
- **Filed your way.** Ordinary PDF files in your own folder, sorted into the
  subfolders and file names you set up; tags and types as Finder tags.
- **Suggestions on the device.** Apple Intelligence suggests type, sender, title,
  date, amount, deadline, IBAN and tags – on your Mac. Nothing is applied until
  you click.
- **Found again.** Full text, natural language (“invoices last year over $100”),
  search by meaning, Spotlight and Shortcuts.
- **Evidence.** Every filing and every page change is logged and signed with a key
  in the Secure Enclave.
- **No account, no cloud, no tracking.** The developer receives no data from the
  app.

## Screenshots

<div class="shots">
  <figure class="wide"><img src="/leafrelief/assets/screens/en/light.png" alt="Leaf Relief in light mode: sidebar with inbox, types and tags, the list of demo documents, the preview of an invoice with highlighted fields, and suggestions for type, sender and tags"><figcaption>Light</figcaption></figure>
  <figure class="wide"><img src="/leafrelief/assets/screens/en/dark.png" alt="Leaf Relief in dark mode: the archive with demo documents, the preview, and suggestions for type, sender and tags"><figcaption>Dark</figcaption></figure>
</div>

*The screenshots show a demo archive with invented documents.*

## The problem

Paper arrives every week – invoices, contracts, payslips, letters from the tax
office – and most of it has to be kept for years.

### Paper piles

Folders and boxes fill up. Finding last year's insurance letter means leafing
through all of them.

### Scattered PDFs

What already is digital lies in Downloads, on the desktop and in mail
attachments, under names like `scan0042.pdf`.

### No search

A scanned page is just a picture. Without a text layer, neither the Finder nor
Spotlight can find a single word in it.

### Cloud services that read your documents

Many archive services solve this by uploading your documents and analysing them
on their servers – your bank statements, medical letters and contracts included.

---

### In short

| Pain | |
| --- | --- |
| Paper piles | finding one letter means searching every folder |
| Scattered PDFs | files everywhere, under meaningless names |
| No search | scanned pages are pictures without text |
| Manual filing | every document needs a name, a folder and tags by hand |
| Cloud services | your most private documents end up on someone else's server |

[:octicons-arrow-right-24: How Leaf Relief solves each of these](#what-leaf-relief-does)

## What Leaf Relief does

Leaf Relief does the whole path from paper to a searchable archive in one Mac
app – and keeps every step on your Mac.

### Scan or import

- **Scan** with AirScan scanners on your network and USB scanners with a macOS
  driver – the ones macOS itself knows. Feeder before flatbed, double-sided when
  the feeder can, 300 dpi, colour mode *Automatic*: pages without noticeable
  colour are saved in greyscale.
- **Follow every step**: Scan → Text → File → Index, with the page count. You can
  cancel at any time.
- **Import** from the inbox folder: any other scanner, downloads or photos – drop
  them in and Leaf Relief files them. PDF, JPEG, PNG, HEIC and TIFF are accepted;
  PDFs that already contain text are taken over unchanged, images and image-only
  PDFs get a text layer.
- **Text recognition** runs with Apple's Vision framework in German, English,
  French and Spanish. Pages are turned upright first; the invisible text layer sits
  exactly over the image, so selecting and copying in Preview hits the word.

### File it your way

- **Subfolders** by year, year and month, type, or year and type – or none.
- **File names** from date, type, a name suffix and the page count; a name that
  already exists gets `-2`, `-3` …
- **Ordinary PDF files** in your own folder. Tags and types are Finder tags, the
  fields travel with the file. The app's index is only an index – the PDF is the
  source.
- **Your own types** with name, colour and symbol, next to the built-in ones.

### Suggestions on the device

- **Apple Intelligence** reads the document and suggests type, sender, title,
  date, amount, deadline, file reference, IBAN, a summary and tags – on your Mac,
  in the language of the document. No text is sent to a cloud model.
- **Without Apple Intelligence**, simple rules suggest what they can: dates,
  amounts, IBANs with checksum, customer, invoice and contract numbers, and
  legal forms such as GmbH, Ltd or Inc. The rules understand German and English documents.
- **You decide.** Suggestions are stored, never applied by themselves. Recognised
  fields are highlighted in the preview; one click applies them.

### Find it again

- **Full text** across the whole archive.
- **Natural language** – “invoices last year over $100” becomes filters for type,
  sender, period and amount.
- **Search by meaning**, for when you remember what a document was about but not
  its words. Natural-language search and search by meaning understand German and
  English.
- **Spotlight** finds your documents too; a hit opens the document in the app.
- **Shortcuts and Siri:** “Scan Document”, “Find Document”, “Open Last Scan”.
- **Files only in iCloud** are not downloaded; they are indexed from their name,
  fields and tags.

### Evidence: a signed change log

- **Every filing, import and page change** – and changes made outside the app,
  for example in Preview – is recorded as an entry of a hash chain, signed with a
  key in this Mac's Secure Enclave.
- **A seal** on each document says what is known: *Unchanged since scan*,
  *Edited (n×), chain valid*, or *Verification failed* with the reason.
- **Export** a verification report and the public key.
- **Time stamps (optional, off by default):** switched on, only a checksum
  (SHA-256) of each entry goes to a time stamping service – never the document.

### Editing pages

- **Rotate, move and delete pages** – with undo.
- **The original is kept.** Every edit is built from the original, so deleted
  pages can come back.
- **Fix Orientation Automatically** turns crooked pages upright with the same
  recognition used during scanning.

### Deadlines and sharing

- **Deadlines as reminders** – created only when you click “Create Reminder”.
- **Share and send by email** as a copy named after the title, without your
  private tags and types.
- **A menu bar icon** shows scanning, progress and the inbox count.

---

### How it solves each pain point

| Pain | How Leaf Relief solves it |
| --- | --- |
| Paper piles | Scan with the scanner macOS already knows, straight into the archive |
| Scattered PDFs | One inbox folder for everything else; filed automatically |
| No search | A text layer in every PDF; full text, natural language and meaning |
| Manual filing | Folders and names from your own pattern; suggestions for type, sender and tags |
| Cloud services | Recognition, suggestions and search run on your Mac; no account, no server |

## Privacy

Leaf Relief has **no backend, no account, no analytics, no advertising and no
tracking**. Your documents stay in the folders you choose; they leave your Mac
only when you share them yourself. Details in the
[privacy policy](privacy/index.md).

## Requirements

- macOS 26 or newer on a Mac with Apple silicon.
- For suggestions with Apple Intelligence: Apple Intelligence turned on. Without
  it, simple rules suggest.
- A scanner is optional: AirScan on your network or USB with a macOS driver; any
  other scanner works through the inbox folder.
- In English, German, French and Spanish. Simple rules and natural-language search
  understand German and English documents.
- Leaf Relief writes standard PDFs with a searchable text layer – no PDF/A.
- One-time purchase, no in-app purchases. Coming soon to the Mac App Store.

---

[Privacy policy](privacy/index.md) · [Support](support/index.md)
