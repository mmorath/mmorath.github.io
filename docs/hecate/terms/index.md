# Terms of use

*Hecate is a product of MMM Software & Consulting. This page states in plain
words what applies to your use of the Hecate apps — and which text is the one
that legally governs.*

!!! note "German original"
    This page is a courtesy translation. The legally binding version is the
    German [Nutzungsbedingungen](/de/hecate/terms/){ hreflang="de" }.

## What Hecate is

Hecate is a family of apps for iPhone, iPad and Apple TV that captures physical
objects against a configurable **profile**, places them on the map, and streams
them over **MQTT** to a broker of your choice.

There is no backend, no account and no service of ours behind it: the apps talk
only to the broker you enter yourself.

## Which licence applies

Use of the Hecate apps is governed by **Apple's standard end user licence
agreement**:

[Apple — Licensed Application End User License
Agreement](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)

We deliberately write **no licence of our own**. One we wrote ourselves would
not supplement Apple's, it would compete with it — and it would need a lawyer's
review before it improved anything. The custom EULA field in App Store Connect
is therefore left empty; that is precisely when Apple's standard agreement
applies. **This page explains, it replaces nothing.**

## The free tier

The free tier is **a real product, not a trial**: it never expires, and nothing
you have captured is held back from you. What is limited is *quantity* — 10
captures per calendar day, one stored profile, one published profile at a time,
one broker configuration, profiles of up to five building blocks.

Exactly what those limits count, and what else the free tier includes, is set
out in full under [Free & Pro](../plans/index.md) — there and only there, so
the same statement cannot drift apart in two places.

## The subscription

!!! info "The subscription is not on sale yet"

    The apps shipping today are the **free tier only**. There is no purchase
    inside them and no price to pay. What follows applies as soon as a
    subscription is offered.

The subscription will be offered **monthly or yearly**, billed through your
Apple account, and it **renews automatically** until you cancel it. Cancelling
happens in Apple's subscription settings; you are never committed for longer
than one billing period.

**We are not naming a price here yet.** The products are not created, and a
price that still changes before release would have stood on the web as a false
statement. When the time comes it will be on [Free & Pro](../plans/index.md),
openly and in full — exactly where we said it would be.

When a subscription lapses you lose nothing. Everything you have captured lives
on your broker and on your device and stays there. The app falls back to the
free tier — it deletes nothing and locks nothing you have already created.

## Who you are buying from

The Hecate apps are distributed exclusively through the **App Store**.
A purchase or subscription is concluded there with **Apple**, not with us.
Billing, invoices, withdrawal and cancellation therefore run through your Apple
account. Questions about the product itself are welcome at the address below.

## Cancelling

You cancel a subscription in your Apple account's subscription settings:

[apps.apple.com/account/subscriptions](https://apps.apple.com/account/subscriptions)

Cancellation takes effect at the end of the current billing period; until then
the subscription stays active. We can neither see a subscription nor cancel one
for you.

## Refunds

Purchases go entirely through Apple, so only Apple can refund them — through
the usual route:

[reportaproblem.apple.com](https://reportaproblem.apple.com)

**Whether a refund is granted is Apple's decision, not ours.** We hold neither
your payment details nor any way to reverse a payment. Write to us anyway if
something is wrong: we can fix the fault even when we cannot move the money.

## If this project ends

Hecate is a small project, and we don't hide it. Should development end, we
will say so, stop selling new subscriptions, and let running ones expire.

You keep everything. Your data already lives on your own broker, the profile
format is open, documented JSON, and profiles can be published without this
app. There is nothing to export and nothing to migrate — which is exactly why
the monthly subscription is the main product: you are never committed for more
than thirty days.

## What we run — and what we don't

Hecate runs no servers. There is no backend, no account, and no service
standing between you and your data. The app talks only to the MQTT broker you
enter yourself.

That puts the operation in your hands: the broker, the network, the
certificates, the devices. If the broker is unreachable, a certificate has
expired, or a management policy is set wrong, the app can neither detect nor
repair it — it shows you, and keeps your capture on the device until it can be
delivered.

Verify important data at its destination. This app is a tool for capturing, not
a proof of where a message ended up.

What goes into profiles and captures is yours to decide. The app checks a
profile's structure, not its content — whether a field is sensible, permitted
or lawful is a judgement only the operator can make. The same goes for the apps
as a whole: they are tools for capturing in your own operation; using them
against applicable rules or the rights of others is misuse, not purpose.

And: these apps run on platforms we do not own. When Apple, Google or a device
maker restricts an interface with an update — camera, Bluetooth, printing
services, background operation — a feature may be limited or may disappear
without us being able to prevent it. We adapt where we can; no claim arises
that every feature persists under every future OS version.

## Contact

**MMM Software & Consulting**, owner: Matthias Morath<br>
E-mail: [info@hecateapps.com](mailto:info@hecateapps.com)

The full provider details are in the [legal
notice](../impressum/index.md); what the apps do with data is described under
[Privacy](../privacy/index.md).
