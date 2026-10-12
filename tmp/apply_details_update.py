import os
import sys

with open('app/src/main/assets/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. CSS to inject
new_css = """
/* ================= Modern Anime Details Page ================= */
.details-page-wrapper {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background: #0a0a0a;
  color: #fff;
  padding-bottom: 95px;
  direction: rtl;
  text-align: right;
  overflow-x: hidden;
}

.details-panoramic-hero {
  position: relative;
  width: 100%;
  height: 245px;
  background: #111;
  overflow: hidden;
}

.details-panoramic-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
  filter: brightness(0.82);
  display: block;
}

.details-hero-overlay-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 90px;
  background: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, transparent 100%);
  z-index: 2;
  pointer-events: none;
}

.details-hero-overlay-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 140px;
  background: linear-gradient(to top, #0a0a0a 0%, rgba(10,10,10,0.85) 50%, transparent 100%);
  z-index: 2;
  pointer-events: none;
}

.details-top-bar {
  position: absolute;
  top: 14px;
  left: 14px;
  right: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 10;
  direction: rtl;
}

.details-top-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.details-glass-btn {
  background: rgba(0, 0, 0, 0.58);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.18);
  width: 42px;
  height: 42px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 16px;
  transition: transform 0.15s ease, background 0.15s ease;
  outline: none;
  box-shadow: 0 4px 12px rgba(0,0,0,0.5);
}

.details-glass-btn:active {
  transform: scale(0.92);
}

.details-glass-btn.active-fav svg {
  fill: #e50914 !important;
  stroke: #e50914 !important;
}

.details-overlap-container {
  position: relative;
  margin-top: -65px;
  padding: 0 16px;
  z-index: 6;
  display: flex;
  align-items: flex-end;
  gap: 14px;
  direction: rtl;
}

.details-vertical-poster-wrap {
  position: relative;
  width: 115px;
  min-width: 115px;
  aspect-ratio: 2 / 3;
  border-radius: 14px;
  overflow: hidden;
  background: #141414;
  border: 2px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 10px 28px rgba(0,0,0,0.85);
  flex-shrink: 0;
}

.details-vertical-poster {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.details-poster-type-badge {
  position: absolute;
  bottom: 6px;
  right: 6px;
  background: rgba(229, 9, 20, 0.94);
  color: #fff;
  font-size: 10px;
  font-weight: 900;
  padding: 2px 7px;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.6);
  line-height: 1.2;
}

.details-header-meta-col {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  text-align: right;
  gap: 4px;
  padding-bottom: 2px;
}

.details-main-title {
  font-size: 19px;
  font-weight: 900;
  color: #fff;
  line-height: 1.35;
  margin: 0 0 5px 0;
  text-shadow: 0 2px 8px rgba(0,0,0,0.9);
  word-break: break-word;
}

.details-meta-pills-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
}

.details-meta-pill {
  font-size: 11px;
  font-weight: bold;
  padding: 3px 8px;
  border-radius: 8px;
  line-height: 1.2;
  white-space: nowrap;
}

.details-meta-pill.year-pill {
  background: #1a1a1a;
  color: #ddd;
  border: 1px solid #333;
}

.details-meta-pill.type-pill {
  background: rgba(229, 9, 20, 0.15);
  color: #ff4d58;
  border: 1px solid rgba(229, 9, 20, 0.35);
}

.details-meta-pill.status-pill.status-ongoing {
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
  border: 1px solid rgba(34, 197, 94, 0.35);
}

.details-meta-pill.status-pill.status-completed {
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.35);
}

.details-meta-pill.status-pill.status-upcoming {
  background: rgba(251, 191, 36, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(251, 191, 36, 0.35);
}

.details-meta-pill.version-pill {
  background: rgba(15, 28, 36, 0.9);
  color: #38bdf8;
  border: 1px solid #164e63;
}

.details-ep-count-hint {
  font-size: 11.5px;
  color: #aaa;
  margin-top: 2px;
}

.details-cta-section {
  padding: 16px 16px 8px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  direction: rtl;
}

.details-watch-primary-btn {
  background: linear-gradient(135deg, #e50914 0%, #b20710 100%);
  color: #fff;
  border: none;
  padding: 14px 22px;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 800;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 4px 18px rgba(229, 9, 20, 0.5);
  width: 100%;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
  outline: none;
}

.details-watch-primary-btn:active {
  transform: scale(0.97);
}

.details-admin-bar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.details-admin-btn {
  flex: 1;
  min-width: 95px;
  background: #182230;
  color: #38bdf8;
  border: 1px solid #223a54;
  padding: 8px 12px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: bold;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

.details-admin-btn.highlight-admin-btn {
  background: #2b1818;
  color: #ff6b6b;
  border-color: #542222;
}

.details-info-card {
  margin: 10px 16px 20px 16px;
  background: #131313;
  border: 1px solid #242424;
  border-radius: 14px;
  padding: 16px;
  direction: rtl;
  text-align: right;
  box-shadow: 0 4px 14px rgba(0,0,0,0.4);
}

.details-card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 10px;
}

.details-story-body {
  color: #ccc;
  font-size: 13.5px;
  line-height: 1.65;
}

.details-genres-section {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid #222;
}

.details-section-subtitle {
  font-size: 12.5px;
  font-weight: bold;
  color: #888;
  margin-bottom: 8px;
}

.details-genres-chips-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.details-genre-chip {
  background: #1c1c1c;
  color: #e50914;
  border: 1px solid #2e2e2e;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 11.5px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.15s ease;
  user-select: none;
}

.details-genre-chip:active {
  transform: scale(0.95);
  background: #e50914;
  color: #fff;
}

.details-specs-table {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid #222;
}

.details-spec-item {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.spec-label {
  font-size: 11px;
  color: #777;
}

.spec-val {
  font-size: 13px;
  font-weight: bold;
  color: #ddd;
}

.spec-val.status-ongoing { color: #4ade80; }
.spec-val.status-completed { color: #38bdf8; }
.spec-val.status-upcoming { color: #fbbf24; }

/* ================= Episodes Dedicated Page ================= */
.episodes-page-wrapper {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background: #0a0a0a;
  color: #fff;
  padding-bottom: 95px;
  direction: rtl;
  text-align: right;
}

.episodes-top-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  margin-top: 55px;
}

.episodes-anime-summary-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  margin: 0 14px 14px 14px;
  background: #131313;
  border: 1px solid #242424;
  border-radius: 12px;
  direction: rtl;
}

.episodes-anime-thumb {
  width: 44px;
  height: 60px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid #333;
  flex-shrink: 0;
}

.episodes-anime-meta {
  flex: 1;
  min-width: 0;
}

.episodes-anime-title {
  font-size: 14px;
  font-weight: 800;
  color: #fff;
  margin: 0 0 2px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.episodes-anime-count {
  font-size: 11.5px;
  color: #888;
}

.episodes-header-admin-btn {
  background: #182230;
  color: #38bdf8;
  border: 1px solid #223a54;
  padding: 7px 12px;
  border-radius: 8px;
  font-size: 11.5px;
  font-weight: bold;
  cursor: pointer;
  white-space: nowrap;
  flex-shrink: 0;
}

.episodes-list-body {
  padding: 0 14px;
}

.empty-episodes-container {
  padding: 36px 16px;
  text-align: center;
  background: #131313;
  border: 1px solid #242424;
  border-radius: 14px;
  margin: 10px 0;
}

.empty-episodes-icon {
  font-size: 38px;
  margin-bottom: 8px;
}

.empty-episodes-title {
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  margin: 0 0 6px 0;
}

.empty-episodes-desc {
  font-size: 13px;
  color: #888;
  margin: 0 0 16px 0;
}

.empty-add-ep-btn {
  background: #e50914;
  color: #fff;
  border: none;
  padding: 10px 18px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
}

.episodes-cards-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.episode-row-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #141414;
  border: 1px solid #262626;
  border-radius: 12px;
  padding: 10px 12px;
  cursor: pointer;
  direction: rtl;
  transition: transform 0.15s ease, border-color 0.15s ease, background 0.15s ease;
}

.episode-row-card:hover {
  border-color: #383838;
  background: #181818;
}

.episode-row-card.is-watched {
  border-color: rgba(74, 222, 128, 0.3);
  background: rgba(15, 30, 20, 0.4);
}

.episode-row-right {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 0;
}

.episode-play-circle {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: rgba(229, 9, 20, 0.18);
  color: #ff3b47;
  border: 1px solid rgba(229, 9, 20, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  flex-shrink: 0;
}

.episode-info-box {
  flex: 1;
  min-width: 0;
}

.episode-title-line {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.episode-name {
  font-size: 13.5px;
  font-weight: 700;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ep-watched-tag {
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
  border: 1px solid rgba(34, 197, 94, 0.35);
  font-size: 9.5px;
  font-weight: bold;
  padding: 1px 6px;
  border-radius: 6px;
}

.episode-sub-hint {
  font-size: 11px;
  color: #777;
  margin-top: 1px;
}

.episode-row-actions {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-shrink: 0;
}

.ep-action-btn {
  border: none;
  border-radius: 8px;
  font-size: 11.5px;
  font-weight: bold;
  padding: 7px 11px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.12s ease;
}

.ep-action-btn:active {
  transform: scale(0.92);
}

.ep-play-btn {
  background: #e50914;
  color: #fff;
}

.ep-download-btn {
  background: #142838;
  color: #38bdf8;
  border: 1px solid #1e4560;
}

.ep-alt-btn {
  background: #251e12;
  color: #fbbf24;
  border: 1px solid #4a3a1e;
}

.ep-report-btn {
  background: #260a0a;
  color: #ff6b6b;
  border: 1px solid #4a1515;
  padding: 7px 8px;
  font-size: 12px;
}

.ep-edit-btn {
  background: #112233;
  color: #00d2ff;
  border: 1px solid #1a3a5a;
  padding: 7px 8px;
  font-size: 12px;
}

.ep-del-btn {
  background: #250505;
  color: #ff4444;
  border: 1px solid #441111;
  padding: 7px 8px;
  font-size: 12px;
}

/* Light Mode Overrides */
body.light-mode .details-page-wrapper,
body.light-mode .episodes-page-wrapper {
  background: #f4f5f8;
  color: #111;
}

body.light-mode .details-hero-overlay-bottom {
  background: linear-gradient(to top, #f4f5f8 0%, rgba(244,245,248,0.85) 50%, transparent 100%);
}

body.light-mode .details-main-title,
body.light-mode .episodes-anime-title,
body.light-mode .episode-name {
  color: #111;
}

body.light-mode .details-vertical-poster-wrap {
  background: #eef0f4;
  border-color: #dcdfe6;
  box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}

body.light-mode .details-info-card,
body.light-mode .episodes-anime-summary-bar,
body.light-mode .episode-row-card {
  background: #ffffff;
  border-color: #e2e5ec;
  box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

body.light-mode .details-card-header {
  color: #111;
}

body.light-mode .details-story-body {
  color: #444;
}

body.light-mode .spec-val {
  color: #222;
}

body.light-mode .details-genre-chip {
  background: #f0f2f6;
  border-color: #dbe0ea;
}
"""

css_marker = '</style>'
if '.details-page-wrapper' not in text:
    assert css_marker in text, "Could not find </style>"
    text = text.replace(css_marker, new_css + "\n" + css_marker, 1)

# 2. Add functions for details and episodes
functions_code = """
/* ================= Modern Details Page Implementation ================= */
window.renderDetailsPage = function(fid) {
  let item = getItemByFirebaseId(fid);
  if (!item) {
    renderHome();
    return;
  }
  window._lastDetailsFid = fid;
  window.expandedDescriptions[fid] = false;

  let isAnimation = item.type === "animation" || item.type === "arabic" || item.type === "sports";
  let categoryLabel = window.translateCategoryLabel(item.category, isAnimation);
  let isFav = window.isFavorite ? window.isFavorite(item.id) : false;

  // Banner image (Panoramic horizontal poster, fallback to backdrop or poster)
  let bannerImg = (item.banner || item.horizontalPoster || item.backdrop || item.poster || "").trim();
  let posterImg = (item.poster || "").trim();
  let safeTitle = window.escapeDescHtml(item.title || "بدون عنوان");
  let yearText = item.year || 2024;

  // Type badge label
  let isMovie = (item.category === "فيلم" || item.category === "فلم" || item.type === "movies");
  let typeLabel = "مسلسل";
  if (isMovie) {
    typeLabel = "الفيلم";
  } else if (item.category === "أنميشن" || item.type === "animation") {
    typeLabel = "الأنميشن";
  } else if (item.category === "أنمي" || item.type === "anime") {
    typeLabel = "الأنمي";
  } else if (item.category && item.category !== "all") {
    typeLabel = item.category;
  }

  // Work Status (حالة العمل: مستمر / مكتمل / لم يصدر بعد)
  let rawStatus = (item.status || "").trim();
  let statusLabel = rawStatus || (isMovie ? "مكتمل" : "مستمر");
  let statusClass = "status-ongoing";
  if (statusLabel === "مكتمل" || statusLabel.includes("مكتمل")) {
    statusClass = "status-completed";
  } else if (statusLabel === "لم يصدر بعد" || statusLabel.includes("لم يصدر")) {
    statusClass = "status-upcoming";
  }

  // Episodes calculation
  let episodes = Array.isArray(item.episodes) ? item.episodes : (item.video || item.altUrl ? [{ title: "الحلقة 1", video: item.video || "", altUrl: item.altUrl || "" }] : []);

  // Admin action buttons
  let adminActionsHtml = (window.currentUserRole === "ADMIN") ? `
    <div class="details-admin-bar">
      <button type="button" class="details-admin-btn" onclick="openEditPosterModal('${item.firebaseId}')">
        <span>🖼️</span> تعديل البوستر
      </button>
      <button type="button" class="details-admin-btn" onclick="openEditContentModal('${item.firebaseId}')">
        <span>✏️</span> تعديل العمل
      </button>
      ${!isMovie ? `
        <button type="button" class="details-admin-btn highlight-admin-btn" onclick="renderAddEpisodeForm('${item.firebaseId}')">
          <span>➕</span> إضافة حلقة
        </button>
      ` : ''}
    </div>
  ` : "";

  // Genres chips
  let genres = window.getItemGenres(item);
  let genresHtml = (genres.length > 0) ? `
    <div class="details-genres-section">
      <div class="details-section-subtitle">🏷️ التصنيفات</div>
      <div class="details-genres-chips-wrap">
        ${genres.map(g => `
          <button type="button" class="details-genre-chip" onclick="window.filterByGenreFromDetails('${window.escapeDescHtml(g)}')">
            ${window.escapeDescHtml(g)}
          </button>
        `).join("")}
      </div>
    </div>
  ` : "";

  // Description / Story
  let descHtml = window.renderDescriptionHtml(item.firebaseId);

  // Version badge (مترجم / مدبلج)
  let versionBadgeHtml = item.version ? `
    <span class="details-meta-pill version-pill">${window.escapeDescHtml(item.version)}</span>
  ` : "";

  main.innerHTML = `
    <div class="details-page-wrapper">
      <!-- 1. Panoramic Header Section -->
      <div class="details-panoramic-hero">
        <img class="details-panoramic-img" src="${bannerImg}" alt="${safeTitle}" loading="eager" onerror="this.src='${posterImg}'">
        <div class="details-hero-overlay-top"></div>
        <div class="details-hero-overlay-bottom"></div>
        
        <!-- Floating Navigation & Action Bar -->
        <div class="details-top-bar">
          <button type="button" class="details-glass-btn" onclick="goBack()" title="رجوع" aria-label="رجوع">
            <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">
              <line x1="19" y1="12" x2="5" y2="12"></line>
              <polyline points="12 19 5 12 12 5"></polyline>
            </svg>
          </button>
          <div class="details-top-actions">
            <button type="button" class="details-glass-btn ${isFav ? 'active-fav' : ''}" onclick="window.toggleDetailsFavorite('${item.id}', '${item.firebaseId}')" title="${isFav ? 'إزالة من المفضلة' : 'إضافة إلى المفضلة'}" aria-label="المفضلة">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="${isFav ? '#e50914' : 'none'}" stroke="${isFav ? '#e50914' : '#fff'}" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </button>
            <button type="button" class="details-glass-btn" onclick="openReportProblemModal('${item.firebaseId}', -1)" title="الإبلاغ عن مشكلة" aria-label="الإبلاغ عن مشكلة">
              🚩
            </button>
          </div>
        </div>
      </div>

      <!-- 2. Overlapping Poster & Metadata Info -->
      <div class="details-overlap-container">
        <div class="details-vertical-poster-wrap">
          <img class="details-vertical-poster" data-poster-fid="${item.firebaseId}" src="${posterImg}" alt="${safeTitle}" loading="eager">
          <span class="details-poster-type-badge">${window.escapeDescHtml(typeLabel)}</span>
        </div>
        <div class="details-header-meta-col">
          <h1 class="details-main-title">${safeTitle}</h1>
          <div class="details-meta-pills-row">
            <span class="details-meta-pill year-pill">${yearText}</span>
            <span class="details-meta-pill type-pill">${window.escapeDescHtml(typeLabel)}</span>
            <span class="details-meta-pill status-pill ${statusClass}">${window.escapeDescHtml(statusLabel)}</span>
            ${versionBadgeHtml}
          </div>
          ${(!isMovie && episodes.length > 0) ? `
            <div class="details-ep-count-hint">
              <span>🎬 ${episodes.length} حلقة متوفرة</span>
            </div>
          ` : ''}
        </div>
      </div>

      <!-- 3. Primary CTA & Action Buttons -->
      <div class="details-cta-section">
        <button type="button" class="details-watch-primary-btn" onclick="window.handleDetailsWatchClick('${item.firebaseId}')">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
            <polygon points="5 3 19 12 5 21 5 3"></polygon>
          </svg>
          <span>المشاهدة</span>
        </button>
        ${adminActionsHtml}
      </div>

      <!-- 4. Story & Categories Card -->
      <div class="details-info-card">
        <div class="details-card-header">
          <span class="details-card-icon">📖</span>
          <span>قصة العمل</span>
        </div>
        <div class="details-story-body">
          ${descHtml}
        </div>
        ${genresHtml}
        <div class="details-specs-table">
          <div class="details-spec-item">
            <span class="spec-label">النوع:</span>
            <span class="spec-val">${window.escapeDescHtml(typeLabel)}</span>
          </div>
          <div class="details-spec-item">
            <span class="spec-label">سنة الإصدار:</span>
            <span class="spec-val">${yearText}</span>
          </div>
          <div class="details-spec-item">
            <span class="spec-label">الحالة:</span>
            <span class="spec-val ${statusClass}">${window.escapeDescHtml(statusLabel)}</span>
          </div>
          ${(!isMovie && episodes.length > 0) ? `
            <div class="details-spec-item">
              <span class="spec-label">عدد الحلقات:</span>
              <span class="spec-val">${episodes.length} حلقة</span>
            </div>
          ` : ''}
        </div>
      </div>
    </div>
  `;
};

window.toggleDetailsFavorite = function(id, fid) {
  window.toggleFavorite(id);
  window.renderDetailsPage(fid);
};

window.handleDetailsWatchClick = function(fid) {
  let item = getItemByFirebaseId(fid);
  if (!item) return;

  let isMovie = (item.category === "فيلم" || item.category === "فلم" || item.type === "movies");
  let episodes = Array.isArray(item.episodes) ? item.episodes : (item.video || item.altUrl ? [{ title: "الحلقة 1", video: item.video || "", altUrl: item.altUrl || "" }] : []);

  if (isMovie) {
    let hasMovieLink = Boolean((item.video || "").trim() || (item.altUrl || "").trim() || (episodes.length > 0 && (episodes[0].video || episodes[0].altUrl)));
    if (hasMovieLink) {
      window.watchEpisode(fid, 0);
    } else {
      alert("لا يتوفر رابط مشاهدة مضاف حالياً لهذا الفيلم — سيتم إضافته قريباً!");
    }
  } else {
    if (episodes.length === 0 && !item.video && !item.altUrl) {
      alert("لا توجد حلقات مضافة حالياً لهذا العمل — سيتم إضافة الحلقات قريباً!");
    } else {
      window.openEpisodesPage(fid);
    }
  }
};

window.openEpisodesPage = function(fid) {
  let item = getItemByFirebaseId(fid);
  if (!item) return;
  window._lastDetailsFid = fid;
  navigateTo("episodes", () => {
    window.renderEpisodesPage(fid);
  });
};

window.renderEpisodesPage = function(fid) {
  let item = getItemByFirebaseId(fid);
  if (!item) {
    renderHome();
    return;
  }
  window._lastDetailsFid = fid;

  let baseEpisodes = Array.isArray(item.episodes) ? item.episodes : (item.video || item.altUrl ? [{ title: "الحلقة 1", video: item.video || "", altUrl: item.altUrl || "" }] : []);
  let safeTitle = window.escapeDescHtml(item.title || "");
  let isDesc = (window.episodesSortOrder === "desc");

  let mapped = baseEpisodes.map((ep, originalIdx) => ({ ep, originalIdx }));
  let list = isDesc ? [...mapped].reverse() : mapped;

  let sortBtnHtml = baseEpisodes.length > 0 ? `
    <button type="button" class="ep-order-btn ${isDesc ? 'desc' : ''}" onclick="window.toggleEpisodesOrderInPage('${item.firebaseId}')" title="${isDesc ? 'ترتيب تصاعدي' : 'ترتيب تنازلي'}" aria-label="ترتيب الحلقات">
      <span style="font-size:16px;display:inline-block">⇅</span>
      <span style="font-size:12px;font-weight:bold">${isDesc ? `${baseEpisodes.length} ➔ 1` : `1 ➔ ${baseEpisodes.length}`}</span>
    </button>
  ` : "";

  let adminAddBtn = (window.currentUserRole === "ADMIN") ? `
    <button type="button" class="episodes-header-admin-btn" onclick="renderAddEpisodeForm('${item.firebaseId}')">
      ➕ إضافة حلقة
    </button>
  ` : "";

  let episodesListHtml = "";
  if (baseEpisodes.length === 0) {
    episodesListHtml = `
      <div class="empty-episodes-container">
        <div class="empty-episodes-icon">🎬</div>
        <h3 class="empty-episodes-title">لا توجد حلقات مضافة بعد</h3>
        <p class="empty-episodes-desc">سيتم إضافة حلقات هذا العمل قريباً عند توفرها.</p>
        ${(window.currentUserRole === "ADMIN") ? `
          <button type="button" class="empty-add-ep-btn" onclick="renderAddEpisodeForm('${item.firebaseId}')">
            ➕ إضافة أول حلقة الآن
          </button>
        ` : ''}
      </div>
    `;
  } else {
    episodesListHtml = `
      <div class="episodes-cards-list">
        ${list.map(({ ep, originalIdx }) => {
          let epTitle = window.escapeDescHtml(ep.title || `الحلقة ${originalIdx + 1}`);
          let isWatched = window.isEpisodeWatched(item.firebaseId, originalIdx);
          let isVid = Boolean((ep.video || "").trim());
          let isAlt = Boolean((ep.altUrl || item.altUrl || "").trim());
          
          let dlBtn = "";
          let videoUrl = (ep.video || "").trim();
          let altUrl = (ep.altUrl || item.altUrl || "").trim();
          let dlLink = (videoUrl && !videoUrl.includes(".m3u8")) ? videoUrl : (altUrl && (altUrl.includes("pixeldrain.com") || altUrl.endsWith(".mp4") || altUrl.endsWith(".mkv"))) ? altUrl : "";
          if (dlLink) {
            dlBtn = `
              <button type="button" class="ep-action-btn ep-download-btn" onclick="event.stopPropagation();window.openExternalLink('${dlLink}')" title="تحميل الحلقة">
                ⬇ تحميل
              </button>
            `;
          }

          let altBtn = (isAlt && isVid) ? `
            <button type="button" class="ep-action-btn ep-alt-btn" onclick="event.stopPropagation();window.openExternalLink('${altUrl}')" title="سيرفر بديل">
              🔗 بديل
            </button>
          ` : "";

          let adminBtns = (window.currentUserRole === "ADMIN") ? `
            <button type="button" class="ep-action-btn ep-edit-btn" onclick="event.stopPropagation();openEditEpisodeModal('${item.firebaseId}', ${originalIdx})" title="تعديل الرابط">
              ✏️
            </button>
            <button type="button" class="ep-action-btn ep-del-btn" onclick="event.stopPropagation();deleteEpisode('${item.firebaseId}', ${originalIdx})" title="حذف الحلقة">
              🗑️
            </button>
          ` : "";

          return `
            <div class="episode-row-card ${isWatched ? 'is-watched' : ''}" onclick="watchEpisode('${item.firebaseId}', ${originalIdx})">
              <div class="episode-row-right">
                <div class="episode-play-circle">▶</div>
                <div class="episode-info-box">
                  <div class="episode-title-line">
                    <span class="episode-name">${epTitle}</span>
                    ${isWatched ? '<span class="ep-watched-tag">✓ تمت المشاهدة</span>' : ''}
                  </div>
                  <div class="episode-sub-hint">
                    ${isVid ? '⚡ سيرفر سريع' : isAlt ? '🔗 رابط خارجي' : 'قيد التجهيز'}
                  </div>
                </div>
              </div>
              <div class="episode-row-actions" onclick="event.stopPropagation()">
                <button type="button" class="ep-action-btn ep-play-btn" onclick="watchEpisode('${item.firebaseId}', ${originalIdx})">
                  مشاهدة
                </button>
                ${altBtn}
                ${dlBtn}
                <button type="button" class="ep-action-btn ep-report-btn" onclick="openReportProblemModal('${item.firebaseId}', ${originalIdx})" title="إبلاغ عن مشكلة">
                  🚩
                </button>
                ${adminBtns}
              </div>
            </div>
          `;
        }).join("")}
      </div>
    `;
  }

  main.innerHTML = `
    <div class="episodes-page-wrapper">
      <div class="episodes-top-header">
        <button type="button" class="back-btn" style="margin:0" onclick="goBack()">
          ← رجوع للعمل
        </button>
        <div style="display:flex;align-items:center;gap:8px">
          ${sortBtnHtml}
        </div>
      </div>

      <div class="episodes-anime-summary-bar">
        <img class="episodes-anime-thumb" src="${item.poster}" alt="${safeTitle}">
        <div class="episodes-anime-meta">
          <h2 class="episodes-anime-title">${safeTitle}</h2>
          <div class="episodes-anime-count">
            🎬 ${baseEpisodes.length} حلقة متوفرة
          </div>
        </div>
        ${adminAddBtn}
      </div>

      <div class="episodes-list-body">
        ${episodesListHtml}
      </div>
    </div>
  `;
};

window.toggleEpisodesOrderInPage = function(fid) {
  window.episodesSortOrder = (window.episodesSortOrder === "asc") ? "desc" : "asc";
  window.renderEpisodesPage(fid);
};
"""

# Replace openDetails implementation
idx_od = text.find('window.openDetails=(fid)=>{')
idx_we = text.find('window.watchEpisode=(fid,idx)=>{', idx_od)
assert idx_od != -1 and idx_we != -1, "Could not find openDetails slice"

new_open_details = """window.openDetails=(fid)=>{
  window.incrementItemViews(fid);
  let item = getItemByFirebaseId(fid);
  if (!item) return;
  window._lastDetailsFid = fid;
  window.episodesSortOrder = "asc";
  window.expandedDescriptions[fid] = false;
  navigateTo("details", () => {
    window.renderDetailsPage(fid);
  });
};
""" + functions_code + "\n"

text = text[:idx_od] + new_open_details + text[idx_we:]

# Replace openDetailsBack implementation
idx_odb = text.find('window.openDetailsBack=()=>{')
idx_osb = text.find('window.openSearchBack=()=>{', idx_odb)
assert idx_odb != -1 and idx_osb != -1, "Could not find openDetailsBack slice"

new_open_details_back = """window.openDetailsBack=()=>{
  let fid = window._lastDetailsFid;
  let item = getItemByFirebaseId(fid);
  if (!item) { renderHome(); return; }
  currentPage = "details";
  window.renderDetailsPage(fid);
  window.scrollTo(0, 0);
};
"""

text = text[:idx_odb] + new_open_details_back + text[idx_osb:]

# Update window.goBack
old_goback_needle = 'else if(prev==="details"&&window._lastDetailsFid)openDetailsBack();'
new_goback_needle = '''else if(prev==="details"&&window._lastDetailsFid)openDetailsBack();
  else if(prev==="episodes"&&window._lastDetailsFid)openEpisodesPage(window._lastDetailsFid);'''

assert old_goback_needle in text, "old_goback_needle not found"
text = text.replace(old_goback_needle, new_goback_needle, 1)

# Add banner and status inputs to editContentModal
old_edit_modal_marker = '<select id="editContentTypeSelect" class="input" style="margin:0">'
idx_marker = text.find(old_edit_modal_marker)
assert idx_marker != -1, "Could not find editContentTypeSelect in editContentModal"
idx_end_select = text.find('</select>', idx_marker) + len('</select>')
idx_end_div = text.find('</div>', idx_end_select) + len('</div>')

new_modal_banner_fields = """
        <!-- Horizontal Poster (Panoramic Banner) & Status -->
        <div>
          <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">رابط البوستر الأفقي (بانوراما في صفحة التفاصيل):</label>
          <input id="editContentBannerInput" class="input" style="margin:0" placeholder="https://... رابط صورة البوستر الأفقي العريض">
        </div>
        <div>
          <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">حالة العمل:</label>
          <select id="editContentStatusSelect" class="input" style="margin:0">
            <option value="مستمر">مستمر (Ongoing)</option>
            <option value="مكتمل">مكتمل (Completed)</option>
            <option value="لم يصدر بعد">لم يصدر بعد (Upcoming)</option>
          </select>
        </div>"""

text = text[:idx_end_div] + new_modal_banner_fields + text[idx_end_div:]

# Update openEditContentModal to populate banner and status
old_open_edit_needle = 'const descInput = document.getElementById("editContentDescInput");\n  if (descInput) descInput.value = item.description || "";'
new_open_edit_needle = '''const descInput = document.getElementById("editContentDescInput");\n  if (descInput) descInput.value = item.description || "";
  const bannerInput = document.getElementById("editContentBannerInput");  if (bannerInput) bannerInput.value = item.banner || item.horizontalPoster || "";
  const statusSelect = document.getElementById("editContentStatusSelect");  if (statusSelect) statusSelect.value = item.status || (item.category === "فيلم" || item.category === "فلم" ? "مكتمل" : "مستمر");'''

assert old_open_edit_needle in text, "old_open_edit_needle not found"
text = text.replace(old_open_edit_needle, new_open_edit_needle, 1)

# Update saveContentFromModal to save banner and status
old_save_read_needle = 'const newDesc = (document.getElementById("editContentDescInput")?.value || item.description || "بدون وصف").trim();'
new_save_read_needle = '''const newDesc = (document.getElementById("editContentDescInput")?.value || item.description || "بدون وصف").trim();
  const newBanner = (document.getElementById("editContentBannerInput")?.value || item.banner || "").trim();
  const newStatus = (document.getElementById("editContentStatusSelect")?.value || item.status || "مستمر").trim();'''

assert old_save_read_needle in text, "old_save_read_needle not found"
text = text.replace(old_save_read_needle, new_save_read_needle, 1)

old_save_updatedoc_needle = 'description: newDesc,\n      adminKey: "hamza2009",'
new_save_updatedoc_needle = '''description: newDesc,
      banner: newBanner,
      status: newStatus,
      adminKey: "hamza2009",'''

assert old_save_updatedoc_needle in text, "old_save_updatedoc_needle not found"
text = text.replace(old_save_updatedoc_needle, new_save_updatedoc_needle, 1)

old_save_item_needle = 'item.description = newDesc;'
new_save_item_needle = '''item.description = newDesc;
    item.banner = newBanner;
    item.status = newStatus;'''

assert old_save_item_needle in text, "old_save_item_needle not found"
text = text.replace(old_save_item_needle, new_save_item_needle, 1)

# Update renderAddPage with addBanner and addStatus inputs
old_add_poster_needle = '<input id="addPoster" class="input" placeholder="رابط بوستر العمل">'
new_add_poster_needle = '''<input id="addPoster" class="input" placeholder="رابط بوستر العمل (العمودي)">
<input id="addBanner" class="input" placeholder="رابط البوستر الأفقي (بانوراما في صفحة التفاصيل - اختياري)">
<select id="addStatus" class="input" style="cursor:pointer">
  <option value="مستمر">حالة العمل: مستمر (Ongoing)</option>
  <option value="مكتمل">حالة العمل: مكتمل (Completed)</option>
  <option value="لم يصدر بعد">حالة العمل: لم يصدر بعد (Upcoming)</option>
</select>'''

assert old_add_poster_needle in text, "old_add_poster_needle not found"
text = text.replace(old_add_poster_needle, new_add_poster_needle, 1)

# Update addNewContent to read and store banner and status
old_add_new_read_needle = 'desc=document.getElementById("addDesc").value.trim()||"بدون وصف";'
new_add_new_read_needle = '''desc=document.getElementById("addDesc").value.trim()||"بدون وصف";
  let banner=(document.getElementById("addBanner")?document.getElementById("addBanner").value.trim():"");
  let status=(document.getElementById("addStatus")?document.getElementById("addStatus").value.trim():"")||"مستمر";'''

assert old_add_new_read_needle in text, "old_add_new_read_needle not found"
text = text.replace(old_add_new_read_needle, new_add_new_read_needle, 1)

old_add_new_doc_needle = 'description:desc,poster,video:video,'
new_add_new_doc_needle = 'description:desc,poster,banner:banner,status:status,video:video,'

assert old_add_new_doc_needle in text, "old_add_new_doc_needle not found"
text = text.replace(old_add_new_doc_needle, new_add_new_doc_needle, 1)

with open('app/src/main/assets/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Details and episodes update applied cleanly!")
