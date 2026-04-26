# Phase 2: Landing Page — Conversion-Optimized

## Purpose
High-converting landing page for Sovereign layer. Optimized for visitor-to-lead conversion.

## Output: Conversion-optimized landing page

---

## File Structure

```
phase-2_landing-page/
├── public/
│   ├── index.html
│   ├── styles.css
│   └── scripts.js
├── src/
│   ├── templates/
│   │   ├── hero.html
│   │   ├── features.html
│   │   ├── proof.html
│   │   ├── cta.html
│   │   └── footer.html
│   └── components/
│       ├── navbar.js
│       ├── scroll-reveal.js
│       └── lead-capture.js
├── content/
│   ├── hero.md
│   ├── features.md
│   ├── testimonials.md
│   └── cta.md
├── deploy.sh
└── README.md
```

---

## Content: Hero Section

```markdown
# The Layer Above Hokage

**Sovereign** — the observatory that sees what your executors miss.

Every Hokage action radiates vacuum in all directions. Sovereign detects the seams before they calcify.

### For Operators Who:
- Run multi-domain systems and lose visibility at the seams
- Need cross-domain pattern detection that scales
- Want governance that earns authority by demonstration, not declaration

[Book a Demo] — [Read the Architecture]

---
```

## Content: Features

```markdown
## What Sovereign Observes

1. **Vacuum Radiation Detection**
   - Every domain action leaves unsaid gaps
   - Sovereign maps the radiation before it calcifies

2. **Cross-Domain Seam Mapping**
   - See where domains overlap before conflicts emerge
   - Portfolio-level resource arbitration

3. **Reflexive Self-Auditing**
   - The layer that audits its own governance
   - Terminated by your explicit acceptance or rejection

4. **Escalation Routing**
   - Systemic vs. local — defined and enforced
   - No more silent drops or flood-ups
```

## Content: Proof

```markdown
## Early Validation

> "The four operators existed on paper for months. Sovereign gave them implementation — now we see what we couldn't before."
> — Hokage Operator

### Current Coverage
- 37 repositories mapped
- 10 organizational organs monitored
- 4 operators implemented, 0 still theoretical
```

## Content: CTA

```markdown
## Start Observing

**Phase 1**: Lean MVP deploys in <4 hours

[Deploy Sovereign] — [Read the Spec]

or explore deeper:

- [Technical Spec] — [Research Atlas] — [Pitch Deck]
```

---

## JavaScript: Lead Capture

```javascript
// src/components/lead-capture.js
const CAPTURE_FORM = {
  fields: ['email', 'role', 'domain_count'],
  cta: 'Get Early Access',
  success: 'Welcome to the observatory.',
  integration: 'mailchimp' // or your CRM
};

function captureLead(data) {
  // Store to: INTEGRATION_ENDPOINT
  return fetch('/api/leads', {
    method: 'POST',
    body: JSON.stringify(data)
  });
}
```

---

## CSS: Conversion Styling

```css
/* styles.css */
:root {
  --primary: #0D0D0D;
  --accent: #FF4D00;
  --surface: #1A1A1A;
  --text: #E5E5E5;
  --muted: #808080;
}

.hero {
  min-height: 90vh;
  display: grid;
  place-items: center;
  text-align: center;
}

.cta-button {
  background: var(--accent);
  color: var(--primary);
  padding: 1rem 2rem;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
}

.cta-button:hover {
  transform: scale(1.05);
}

.proof-ticker {
  display: flex;
  gap: 2rem;
  justify-content: center;
}
```

---

## Decision Log

| Decision | Rationale |
|---|---|
| Dark theme | Matches operator aesthetic |
| Single CTA path | Reduce friction |
| Lead capture | Build pipeline |
| Minimal copy | Let architecture speak |