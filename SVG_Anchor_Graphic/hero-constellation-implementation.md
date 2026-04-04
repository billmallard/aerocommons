# Hero Constellation — Implementation Instructions

## Step 1 — Copy SVG to static assets

Copy `hero-constellation.svg` into your Hugo static directory:

```
static/images/hero-constellation.svg
```

Hugo serves everything in `/static/` at the root. The file will be
available at `https://aerocommons.org/images/hero-constellation.svg`.

## Step 2 — Find the hero right column in layouts/index.html

The hero section has a two-column grid. Look for the right column —
it currently contains the stat cards (2 Active Projects, 100% Open Source, etc).
It will look something like:

```html
<div class="hero-right">
  <div class="hero-stats">
    <!-- stat cards -->
  </div>
</div>
```

## Step 3 — Add the image above the stat cards

Insert the `<img>` tag as the first element inside `.hero-right`,
above the stats grid:

```html
<div class="hero-right">

  <img
    src="/images/hero-constellation.svg"
    alt="AeroCommons open source aviation project network"
    class="hero-constellation"
    width="520"
    height="480"
  />

  <div class="hero-stats">
    <!-- existing stat cards unchanged -->
  </div>

</div>
```

## Step 4 — Add CSS

Add to your stylesheet (wherever the hero styles live):

```css
.hero-constellation {
  width: 100%;
  max-width: 480px;
  height: auto;
  display: block;
  margin: 0 auto 2rem;
  opacity: 0.92;
}

@media (max-width: 768px) {
  .hero-constellation {
    max-width: 320px;
    margin-bottom: 1.5rem;
  }
}
```

The `opacity: 0.92` gives it a very slight softness so it
doesn't compete with the headline — adjust to taste (0.85–1.0 all work).

## Step 5 — If the right column has no vertical space for both

If the stat cards + image feel crowded, you have two clean options:

**Option A — Image replaces the stats entirely**
The hub-level stats (2 projects, 100% open source) are less
compelling than the illustration. Remove the stat cards and let
the constellation fill the right column alone.

**Option B — Stats move below the hero**
Move the stat cards into the mission band section just below
the hero, displayed as a horizontal row of four. The image
takes the full right column height.

## Notes

- The SVG has a transparent background — it will sit perfectly
  on any dark background without any CSS background-color needed.
- The font (`Barlow Condensed`) is already loaded by the page,
  so the labels will render in the correct typeface automatically.
- The SVG is fully scalable — no pixel density issues on retina displays.
- "Your project?" node is intentional — it's an invitation, not a placeholder.
  Leave it as-is.
