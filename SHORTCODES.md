# NOELAC Website: Custom Shortcodes Documentation

This document provides a guide to the custom shortcodes available for managing content on the NOELAC website. These shortcodes allow you to easily embed Cloudinary galleries, single images, local galleries, and specialized UI components.

---

## 1. Cloudinary Integration

### `cloudinary-gallery`
Embeds a dynamic photo gallery pulled directly from Cloudinary based on a tag. Supports smart chronological sorting and branding.

**Usage:**
```markdown
{{< cloudinary-gallery tag="winners-archive" show_captions="true" watermark="true" sort="desc" >}}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tag` | String | `noelac-heritage` | The Cloudinary tag to pull images from. |
| `show_captions` | Boolean | `false` | If `"true"`, displays captions below each image. |
| `watermark` | Boolean | `false` | If `"true"`, displays the club logo watermark in the lightbox. |
| `sort` | String | `desc` | `asc` or `desc`. Sorts by caption using smart year-aware logic (e.g., "2025" > "2014"). |
| `cloud_name` | String | `di1qnuy5r` | The Cloudinary cloud name to use. |

---

### `cloudinary-img`
Embeds a single image from Cloudinary that matches a filename pattern within a specific tag.

**Usage:**
```markdown
{{< cloudinary-img src="champion-dog" caption="Winner of the 2024 Show" align="right" >}}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | String | (Required) | The partial filename to match in Cloudinary. |
| `caption` | String | `""` | Optional text displayed below the image. |
| `align` | String | `right` | `left`, `center`, or `right`. Controls float and wrapping behavior. |
| `alt` | String | (Caption) | Alternative text for accessibility. |
| `tag` | String | `newsletter_images` | The specific tag to search for the matching image. |

---

## 2. Local Image Galleries

### `auto-gallery`
Creates a gallery from local images stored in the project's assets or within a folder adjacent to the content file.

**Usage:**
```markdown
{{< auto-gallery dir="gallery/chshow-2023" show_captions="true" watermark="true" >}}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `dir` | String | (Optional) | Path in `assets` to find images. If empty, uses the current page bundle. |
| `show_captions` | Boolean | `false` | Display captions derived from cleaned-up filenames. |
| `watermark` | Boolean | `true` | Display the NOELAC watermark in the lightbox and on thumbnails. |

---

## 3. UI Components

### `button`
Embeds a styled button with club-specific color palettes.

**Usage:**
```markdown
{{< button href="/membership" color="metallic" size="large" >}}Join NOELAC{{< /button >}}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `href` | String | `""` | The destination URL. |
| `color` | String | `primary` | `primary` (Gold), `metallic` (Silver), or `green`. |
| `outline` | Boolean | `false` | If `"true"`, uses a bordered style instead of a solid fill. |
| `size` | String | `normal` | `small`, `normal`, or `large`. |
| `target` | String | `""` | Browser target (e.g., `_blank` for external links). |

---

### `accordion`
Creates an expandable content block, useful for FAQs or lengthy breed standards.

**Usage:**
```markdown
{{< accordion title="How do I register my puppy?" >}}
Detailed instructions go here. You can use **Markdown** inside!
{{< /accordion >}}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | String | (Required) | The header text that remains visible. |

---

## 4. Automatic Views

These shortcodes are specialized for specific data-driven pages and generally require no parameters as they pull content dynamically from the site structure.

### `committee-view`
Renders the full club committee hierarchy (The High Council, Sentinels, and Watchdogs) with roles and mission statements.
- **Source:** Pulls from `content/committee/` and `data/designations.yaml`.

### `card-view`
Displays a grid of breeders or members, highlighting puppy availability and contact details.
- **Source:** Pulls from `content/breeders/`.

### `calendar`
Embeds the interactive club events calendar.
- **Source:** Managed via Global Settings (`calendar_id` in config).

### `gallery-hub`
Displays a grid of all available photo albums for the archives page.
- **Source:** Pulls from all pages in the `gallery` section.
