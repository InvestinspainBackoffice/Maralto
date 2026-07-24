# Design — Maralto Estepona

<!-- impeccable:design-schema 1 -->

## Direction

**The Architect's Folio** — seed `e89ed262`, position 5/7.

This surface presents Maralto the way an architect would present to a private client: dark-ground precision that lets the developer renders burn bright. It refuses the category's scrolling photo gallery with sidebar specs and competing popups. The visitor scrolls through the building — entrance, interiors, terraces, twilight pool — and at the natural pause, the form appears. One action, no friction.

Mode: **Persuade** — the visitor decides and acts; design is the product.

## Palette

| Token | Value | Usage |
|---|---|---|
| `--bg` | `#0E1318` | Deep charcoal ground |
| `--bg-el` | `#131920` | Elevated surface (contact section) |
| `--text` | `#EDE8E0` | Warm parchment body text |
| `--text-muted` | `#8A96A3` | Secondary text, labels |
| `--gold` | `#C4A97D` | MARALTO wordmark, heading accents, icon strokes |
| `--gold-dim` | `#9E8968` | Annotation lines, trust badge, subtle gold |
| `--line` | `#1F2830` | Structural ruled lines, borders |
| `--line-light` | `#2A3644` | Form input borders |
| `--cta` | `#2D6A7A` | Primary call-to-action (teal) |
| `--cta-hover` | `#387F91` | CTA hover state |
| `--white` | `#FEFCF9` | CTA button text |

## Typography

**Family:** Sora (Google Fonts) — geometric sans, variable weight 300–600.

| Role | Weight | Size | Tracking |
|---|---|---|---|
| Display (MARALTO) | 300 | `clamp(2.8rem, 10vw, 7rem)` | `0.25em` |
| Section heading | 300 | `clamp(1.6rem, 4vw, 2.8rem)` | `-0.01em` |
| Body | 300 | `clamp(0.9rem, 1.8vw, 1.05rem)` | normal |
| Label / annotation | — | `0.6–0.7rem` | `0.15–0.35em` |
| Stats value | 400 | `clamp(1.4rem, 3.5vw, 2.2rem)` | `-0.02em` |

Heading accents use `<em>` styled with `color: var(--gold)`, no italic.

## Layout

- Mobile-first, single column
- `max-width: 720px` for content blocks; `1100px` for wide grids (amenities, contact)
- Full-bleed images at 100% width, tall variants at `clamp(50vh, 70vw, 80vh)`
- Image pairs: single column on mobile, `1fr 1fr` grid at 768px+
- Stats row: always 3 columns with 1px gap borders
- Amenities: 2-column grid on mobile, 3-column at 600px+
- Contact section: stacked on mobile, `1fr 1fr` at 768px+
- Location facts: stacked on mobile, `1fr 1fr` at 768px+
- Thin 1px border frame (fixed, `inset: 0`) frames the viewport

## Spacing

Spacer system using `clamp()` for fluid scaling:
- Default: `clamp(4rem, 10vw, 8rem)`
- Small: `clamp(2rem, 5vw, 4rem)`
- Large: `clamp(6rem, 14vw, 12rem)`

Content padding: `clamp(1.5rem, 5vw, 3rem)` horizontal.

## Motion

- Hero entrance: background image scales from 1.06 to 1.0 with fade (2s), then staggered fade-up for price, name, location, line, scroll cue
- Scroll reveal: `IntersectionObserver` with threshold 0.1, rootMargin `-40px` bottom
  - `.reveal`: `translateY(30px)` → 0 + opacity, 0.9s
  - `.reveal-image`: `scale(1.04) blur(4px)` → natural, 1.2s
  - Both fire once (unobserved after triggering)
- Frame border: fades in at 0.8s delay
- WhatsApp FAB: fade-up at 2.5s delay
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` — fast entry, smooth settle

## Structural motifs

- **Architectural lines:** thin 0.5–1px ruled lines as structural elements, not decoration. Used for frame border, stats borders, amenity grid gaps, location facts, form inputs, agent card details.
- **Gold annotation labels:** uppercase tracked labels with a leading horizontal rule (`::before` pseudo-element), evoking plan-table annotations.
- **Dark ground:** the charcoal surface recedes, making the high-resolution developer renders the dominant visual presence.

## Imagery

10 developer renders from `investinspain.be/wp-content/uploads/2025/08/`:

| File | Subject | Usage |
|---|---|---|
| `Maralto-Estepona-9.png` | Exterior front facade | Hero background |
| `Maralto-Estepona.png` | Entrance with wood + gardens | Full bleed |
| `Maralto-Estepona-1.png` | Interior with spiral stair | Image pair left |
| `Maralto-Estepona-8.png` | Living room + kitchen | Image pair right |
| `Maralto-Estepona-4.png` | Bedroom with wood headboard | Full bleed |
| `Maralto-Estepona-3.png` | Terrace sea view | Image pair left |
| `Maralto-Estepona-2.png` | Terrace mountain view, pergola | Image pair right |
| `Maralto-Estepona-7.png` | Terrace sunset / Africa coast | Full bleed |
| `Maralto-Estepona-5.png` | Infinity pool at twilight | Full bleed |
| `Maralto-Estepona-6.png` | Indoor spa pool | Full bleed |

All images use `loading="lazy"`, `width="1110"`, `height="623"`.

## Components

### Form (blueprint / plan table)
- Ruled-line inputs with floating labels (absolute positioned, animated on focus/fill)
- Belgian phone prefix (`🇧🇪 +32`) fixed left of phone input
- Custom checkbox (16px, gold fill on check)
- Privacy consent with linked terms
- Submit button: teal background, white text, uppercase tracked
- Success state: form fades out (400ms), checkmark + confirmation message fades in

### Agent card
- Name, role, contact links (phone, email, office) with gold SVG icons
- Trust badge: shield icon + "Uw inspectiereis naar Estepona wordt 100% vergoed door ons"

### WhatsApp FAB
- Fixed bottom-right, green circle, pre-filled Dutch message
- Delayed entrance animation (2.5s)

### IIS bar
- Centered SVG key icon + "INVESTINSPAIN.BE" in tracked uppercase
- Sits between contact section and footer

## Accessibility

- WCAG 2.1 AA contrast on all text over dark backgrounds
- `role="img"` + `aria-label` on hero CSS background
- Alt text on all `<img>` elements (Dutch, descriptive)
- `aria-hidden="true"` on decorative elements (frame, rule lines, scroll cue)
- Form inputs with proper `<label>` associations and `autocomplete` attributes
- Focus states via native browser outlines
- `noopener` on all external links
