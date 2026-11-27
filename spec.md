# PlayPrint Product Specification & Feature Roadmap

A comprehensive backlog and feature specification list for the **PlayPrint** game scoring, reviewing, tier list, and personal gaming journal web app.

---

## 1. Core Review & Scoring Engine

- [ ] **Custom Category Weight Presets**: Allow users to save named weighting presets (e.g., "Story-Rich RPG", "Competitive Shooter", "Retro Arcade", "Casual Cozy") rather than just one global weight profile.
- [ ] **Custom Category Sub-items**: Enable users to add custom sub-items beyond the default 6 per category (or rename existing sub-items per review).
- [ ] **Multi-point Rating Scale Granularity**: Option for 0–10 or 0–5 with half-stars (0.5 increments) in addition to the standard 0–5 integer system.
- [ ] **Score Breakdown Explanations**: Hover or tap on the final 0–100 score to show an interactive tooltip/popover calculating exact point contributions from Gameplay, Content, Presentation, and Bonus Stars.
- [ ] **Multiple Bonus Awards**: Configurable bonus point allowances (0–5 bonus stars instead of hardcoded 2) for recognizing standout achievements.
- [ ] **Platform / Version Tagging**: Tag which platform (PC, PS5, Switch, Xbox, Steam Deck, Mobile) and game version/patch was played when logging a review.
- [ ] **Playtime & Completion Status**: Track hours played, completion status (Beaten, 100% Completed, Dropped, Ongoing, Endless), and completion date.
- [ ] **Difficulty Setting Recorded**: Note the difficulty mode played on (Easy, Normal, Hard, Permadeath) and whether accessibility assists were enabled.
- [ ] **Re-review & Review History**: Maintain versioned history when a user updates their review over time after DLCs or major updates, showing score progression graphs.

---

## 2. Tier Lists & Ranking Tools

- [ ] **Drag-and-Drop Tier Sorting**: Intuitive touch-and-pointer drag-and-drop mechanics to reorder games inside and across tier rows (S, A, B, C, D, F).
- [ ] **Customizable Tier Rows**: Add, delete, rename, re-color, and re-order tier labels (e.g., "Masterpiece", "Great", "Mid", "Garbage", or custom tier letters).
- [ ] **Multi-Tier List Collections**: Create and manage multiple distinct tier lists (e.g., "Best RPGs of All Time", "2024 GOTY Contenders", "Zelda Franchises Ranked").
- [ ] **High-Resolution Tier List Export**: Export tier lists as polished PNG/JPEG images or SVG graphics with custom watermarks, titles, and layout options for social sharing.
- [ ] **Auto-Generated Tiers based on Score**: One-click generation of tier lists segmented automatically by score thresholds (e.g., 90–100 = S, 80–89 = A, etc.).
- [ ] **Head-to-Head Comparison Mode**: Compare two games side-by-side with radar charts highlighting category strengths and weaknesses.
- [ ] **Sub-category Leaderboards**: Filter rankings strictly by individual items (e.g., highest rated for "Music", "Art Direction", or "Controls").

---

## 3. Game Database & Metadata Integration

- [ ] **IGDB / RAWG / Steam API Integration**: Autocomplete game search with official box art, release dates, developer/publisher info, genres, and metadata.
- [ ] **Custom Cover Art Upload & Crop**: Let users upload custom box covers, select screenshots, or paste image URLs with built-in crop and focal point adjusters.
- [ ] **Franchise / Series Grouping**: Automatically organize games into series/franchises (e.g., FromSoftware Soulsborne, Final Fantasy, Super Mario).
- [ ] **Genre & Tag Taxonomy**: Comprehensive tagging system (Roguelike, Metroidvania, Deckbuilder, Narrative, Open World, Indie, AAA).
- [ ] **Release Year & Era Filters**: Filter and rank games by release year, console generation, or release decade.

---

## 4. Gaming Journal, Backlog & Activity Tracking

- [ ] **Session Play Logs**: Quick journal entries with timestamps, current mood, progress milestones, and notes during playthroughs.
- [ ] **Backlog & Wishlist Manager**: Categorized backlog pipeline (Up Next, Playing, Paused, Backlog, Wishlist, Dropped, Abandoned).
- [ ] **Priority Queue & "What to Play Next" Selector**: Weighted randomizer or recommendation assistant that suggests what to play next based on backlog priority and mood.
- [ ] **Screenshot & Memory Gallery**: Attach gameplay screenshots, photo-mode captures, and memorable quotes to review summaries.
- [ ] **Achievement & Milestone Tracker**: Checklists for in-game achievements, trophies, or personal self-imposed challenges (e.g., SL1 runs, Nuzlocke).

---

## 5. Visualizations, Analytics & Statistics

- [ ] **Radar / Spider Charts**: Multi-axis radar chart mapping out a game's profile across all 18 evaluated sub-criteria.
- [ ] **Personal Taste Radar (Gamer DNA)**: Aggregate overview showing which aspects you value most vs. score highest on average (e.g., "Art & Soundtrack connoisseur").
- [ ] **Annual Gaming Recap ("Year in Review")**: Spotify Wrapped-style visual summary of total games played, average rating, highest rated genres, and monthly play streaks.
- [ ] **Rating Distribution Bell Curve**: Histogram chart of your score distributions (identifying rating bias or score inflation).
- [ ] **Developer & Publisher Scorecards**: Aggregate rankings showing your favorite studios and publishers ranked by average review score.
- [ ] **Interactive Timeline**: Timeline view showing your gaming journey mapped across weeks, months, and years.

---

## 6. Social, Sharing & Community Features

- [ ] **Shareable Review Cards**: Generate sleek, social-media ready cards (Instagram story, Twitter/X, Discord embed format) featuring box art, score badge, and pull-quote.
- [ ] **Public Profile Webpage**: Optional vanity URL or public view for sharing your library, top 10, and tier lists with friends.
- [ ] **Followers & Friend Activity Feed**: Activity feed showing friends' recent ratings, mini-reviews, and backlog updates.
- [ ] **Community Consensus vs. Your Score**: Compare your personal score directly against the community average or OpenCritic / Metacritic scores.
- [ ] **Collaborative Tier Lists**: Invite friends to vote on, rank, or collectively build a shared tier list.
- [ ] **Discussion & Comments Section**: Threaded comment discussions under reviews with markdown support and spoiler tags.

---

## 7. Data Management, Privacy & Offline Support

- [ ] **Full JSON Export / Import**: Easily backup and restore your complete library, reviews, tier lists, and journal entries.
- [ ] **CSV / Excel Spreadsheet Export**: Export clean table data formatted for spreadsheet lovers and data analysts.
- [ ] **Import from Backloggd / HowLongToBeat / Letterboxd / Steam**: One-click migration tools to import existing backlogs and ratings from other services.
- [ ] **Cloud Sync & Account Authentication**: Optional multi-device synchronization (Google Auth, Apple ID, Email) while preserving local-first storage.
- [ ] **Full Offline PWA (Progressive Web App)**: Installable PWA with Service Worker offline caching for writing reviews completely offline (planes, travels, Steam Deck).
- [ ] **Local-First Privacy Guarantee**: Explicit zero-tracking mode where all data stays strictly in local browser storage without requiring an account.

---

## 8. UI, Accessibility & User Experience

- [ ] **Theme Customizer & Dynamic Accent Colors**: Expanded color palette choices, custom HEX pickers, and OLED true-black mode.
- [ ] **Game-Adaptive Theming**: Dynamically tint review backgrounds and accent colors based on the dominant colors of the game's box art.
- [ ] **Compact vs. Expanded List Views**: Toggle between visual cover grid, compact table view, detailed card view, and minimalist text list.
- [ ] **Full Keyboard Navigation & Hotkeys**: Power-user keyboard shortcuts for quick rating (keys 0–5), navigation (arrows/WASD), search (`/`), and review submission (`Cmd+Enter`).
- [ ] **Screen Reader & ARIA Enhancements**: Complete ARIA landmarks, roles, live regions for score changes, and high-contrast accessibility compliance.
- [ ] **Haptic Feedback**: Subtle vibration feedback on mobile touch devices when rating, awarding bonus stars, and locking in tiers.
- [ ] **Multi-language Support (i18n)**: Localization for Spanish, Japanese, French, German, Portuguese, and Simplified Chinese.
