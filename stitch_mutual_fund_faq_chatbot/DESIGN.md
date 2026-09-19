---
name: Obsidian Emerald Wealth
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bacac1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#85948c'
  outline-variant: '#3c4a43'
  surface-tint: '#2fe0aa'
  primary: '#44edb7'
  on-primary: '#003828'
  primary-container: '#00d09c'
  on-primary-container: '#00533c'
  inverse-primary: '#006c4f'
  secondary: '#c2c6d5'
  on-secondary: '#2b303c'
  secondary-container: '#424753'
  on-secondary-container: '#b0b5c3'
  tertiary: '#9edbff'
  on-tertiary: '#00354a'
  tertiary-container: '#41c3fe'
  on-tertiary-container: '#004e6b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#59fdc5'
  primary-fixed-dim: '#2fe0aa'
  on-primary-fixed: '#002116'
  on-primary-fixed-variant: '#00513b'
  secondary-fixed: '#dee2f1'
  secondary-fixed-dim: '#c2c6d5'
  on-secondary-fixed: '#171c26'
  on-secondary-fixed-variant: '#424753'
  tertiary-fixed: '#c4e7ff'
  tertiary-fixed-dim: '#7bd0ff'
  on-tertiary-fixed: '#001e2c'
  on-tertiary-fixed-variant: '#004c69'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-mobile:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  title-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
  label-sm:
    fontFamily: Inter
    fontSize: 10px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-sm: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system targets modern investors, wealth builders, and financial operators seeking clarity, speed, and institutional trust without administrative friction. The interface marries the clarity of modern fintech with the focused ergonomics of high-performance dark mode platforms.

### Design Movement & Aesthetic
The visual architecture blends **Minimalist Dark Mode** with **Refined Glassmorphism**:
- **Deep Layered Void:** Deep slate and obsidian backdrops create a calm canvas where numerical data and actionable metrics stand forward.
- **Controlled Luminescence:** Restrained use of vibrant emerald and teal draws the eye exclusively to monetary growth, confirmation actions, and critical status changes.
- **Glass & Membrane Surfaces:** Interactive cards leverage ultra-subtle translucent fills, crisp microscopic borders (`rgba(255, 255, 255, 0.08)`), and backdrops with soft diffusion.
- **Institutional Authority:** Micro-copy, regulatory tags, and audit trails feel balanced, precise, and reassuringly compliant.

## Colors

The palette is tuned specifically for low eye-strain during extended market monitoring, high contrast legibility, and unmistakable financial feedback.

### Key Surfaces & Neutral Hierarchy
- **Canvas Base (`#121212`):** Primary background layer for the viewport.
- **Surface Elevation 1 (`#181A20`):** Base container color for side navigation, dashboards, and persistent headers.
- **Surface Elevation 2 (`#1E222B`):** Interactive card backgrounds, module tiles, and standard dropdowns.
- **Surface Border / Divider (`rgba(255, 255, 255, 0.08)`): Crisp structural dividers maintaining division without visual clutter.

### Primary Accents & States
- **Primary Teal (`#00D09C`):** Denotes positive yield, portfolio gains, primary conversions, and active tabs.
- **Primary Hover (`#34D399`):** Brightened emerald state for interaction confirmation.
- **Secondary Slate (`#262B36`):** Chip backgrounds, tertiary actions, and disabled states.
- **Tertiary Cyan (`#38BDF8`):** Informational highlights, benchmark comparisons, and secondary charting metrics.

### Feedback Semantics
- **Negative / Loss (`#F43F5E`):** Bearish movement, errors, down days.
- **Warning / Pending (`#FBBF24`):** Market settlement holds, KYC review notices.
- **Text Primary (`#F8FAFC`):** Display numbers, active balances, headers.
- **Text Secondary (`#94A3B8`):** Metric labels, secondary indicators, disclaimers.

## Typography

Typography relies entirely on **Inter** for its neutral, highly engineered optical metrics, making it optimal for complex tabular figures, dense financial indices, and clear hierarchy.

### Numerical Treatment
- All monetary metrics, portfolio percentages, and price points must use tabular figures (`font-variant-numeric: tabular-nums;`) to prevent layout shift during realtime streaming updates.
- Display and `headline-lg` levels carry tight letter-spacing (`-0.02em` to `-0.01em`) to create a cohesive, authoritative editorial tone.

### Hierarchy & Role Allocation
- **Display & Headline Levels:** Reserved for net worth totals, individual asset current prices, and hero landing statements.
- **Title & Body Levels:** Used for asset descriptions, stock names, fund performance timelines, and input labels.
- **Label Small:** Formats ticker tags (e.g., `NASDAQ: AAPL`), compliance statuses, and mini delta chips. Always set with uppercase tracking when applied to regulatory text.

## Layout & Spacing

The layout is grounded in a 12-column responsive fluid grid designed to display large tranches of market data without crowding.

### Grid Architecture & Breakpoints
- **Desktop (≥1280px):** 12 columns, `margin: 2rem`, `gutter: 1.5rem`. Max-width content bound at `1440px`.
- **Tablet (768px - 1279px):** 8 columns, `margin: 1.5rem`, `gutter: 1rem`. Primary dashboard switches to stacked summaries.
- **Mobile (<768px):** 4 columns, `margin-sm: 1rem`, `gutter-sm: 1rem`. Secondary analytical charts collapse into horizontal swipe rails.

### Spacing Application
- `space-xs` (4px): Inner badge padding, space between icon and inline ticker.
- `space-sm` (8px): Gaps between inline tags, row padding in compact financial tables.
- `space-md` (16px): Internal container padding for cards, form field vertical margins.
- `space-lg` (24px): Structural gaps between distinct card modules and dashboard widgets.
- `space-xl` (40px): Section breaks between portfolio overviews and detailed ledger views.

## Elevation & Depth

Visual hierarchy uses tonal surface layering coupled with dark ambient diffusion rather than stark white drop shadows.

### Elevation Levels
1. **Layer 0 (Canvas):** Pure `#121212`. The receding baseline.
2. **Layer 1 (Panels & Navbars):** Surface `#181A20` with a subtle bottom border (`1px solid rgba(255, 255, 255, 0.06)`).
3. **Layer 2 (Content Cards):** Surface `#1E222B` framed by `1px solid rgba(255, 255, 255, 0.08)` and an ambient shadow: `0 8px 24px rgba(0, 0, 0, 0.45)`.
4. **Layer 3 (Overlays & Dialogs):** Surface `#1E222B` backed by `backdrop-filter: blur(16px)` and `0 20px 40px rgba(0, 0, 0, 0.65)`.

### Accent Luminescence (Glow)
- Interactive states (e.g., Primary CTA, active investment inputs) trigger an emerald luminescence: `box-shadow: 0 0 20px rgba(0, 208, 156, 0.15)`.
- Critical growth cards feature an extremely soft internal gradient highlight: `linear-gradient(180deg, rgba(0, 208, 156, 0.04) 0%, rgba(30, 34, 43, 0) 100%)`.

## Shapes

The design uses pill shapes and rounded corners to soften analytical data displays, creating a modern and consumer-accessible look.

### Geometry Rules
- **Pill Elements (`border-radius: 9999px`):** Used universally for primary buttons, ticker status badges, filter chips, search bars, and transaction action pills.
- **Card Enclosures (`rounded-lg` / 32px):** Applied to major dashboard modules and summary widgets.
- **Inputs & Small Dropdowns (`rounded` / 16px):** Offers structural stability within forms while matching the softness of nearby pill buttons.

## Components

### Buttons
- **Primary Button:** Pill-shaped, background `#00D09C`, text `#121212` (bold 600). Hover shifts to `#34D399` with a subtle teal glow (`0 0 16px rgba(0, 208, 156, 0.25)`).
- **Secondary Button:** Pill-shaped, background `#262B36`, text `#F8FAFC`, border `1px solid rgba(255, 255, 255, 0.08)`. Hover transitions border to `rgba(255, 255, 255, 0.16)`.
- **Ghost Action:** Transparent background, text `#00D09C`, padding reduced; for quick buy/sell toggles.

### Chips & Filters
- Compact pill height (28px - 32px).
- Default: `#181A20` fill, `#94A3B8` text, `1px solid rgba(255, 255, 255, 0.08)`.
- Active: `#262B36` fill, `#00D09C` text, `1px solid #00D09C`.

### Cards & Data Panels
- Background: `#1E222B` with a top-to-bottom subtle luminance fade.
- Border: `1px solid rgba(255, 255, 255, 0.08)`.
- Padding: `1.5rem`.
- Micro-interaction: Hover yields a `1px solid rgba(0, 208, 156, 0.3)` border and smooth 2px translation along the Y-axis.

### Input Fields
- Fill: `#181A20`.
- Border: `1px solid rgba(255, 255, 255, 0.12)`.
- Text: `#F8FAFC` with placeholder `#94A3B8`.
- Focus State: Border snaps to `#00D09C` accompanied by an emerald aura ring (`box-shadow: 0 0 0 3px rgba(0, 208, 156, 0.12)`).

### Compliance & Regulatory Badges
- Small-scale pill badge (`padding: 2px 8px`).
- Background: `rgba(255, 255, 255, 0.04)`.
- Border: `1px solid rgba(255, 255, 255, 0.08)`.
- Typography: `label-sm`, uppercase tracking, `#94A3B8`. Used for SEBI/FINRA notices, verified clearing tags, and risk disclosures.

### Lists & Ledger Rows
- Separated by `1px solid rgba(255, 255, 255, 0.04)` borders.
- Hover background: `rgba(255, 255, 255, 0.02)`.
- Left: Asset icon (36px circular avatar in `#262B36`), stock name, sub-label ticker.
- Right: Current value (`#F8FAFC`, tabular numerals) and dynamic delta pill (green for gain, red for loss).