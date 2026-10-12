import re

with open('app/src/main/assets/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS Styles
new_css = """
/* ================= Filters & Genres System ================= */
.filter-choice-chip {
  background: #181818;
  color: #bbb;
  border: 1px solid #2e2e2e;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.15s ease;
  min-height: 38px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  user-select: none;
}
.filter-choice-chip:active {
  transform: scale(0.96);
}
.filter-choice-chip.active {
  background: #e50914;
  color: #fff;
  border-color: #ff3b47;
  box-shadow: 0 2px 10px rgba(229, 9, 20, 0.45);
}
.filter-genre-pill {
  background: #161616;
  color: #c0c0c0;
  border: 1px solid #2a2a2a;
  padding: 7px 14px;
  border-radius: 20px;
  font-size: 12px;
  cursor: pointer;
  user-select: none;
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 34px;
}
.filter-genre-pill:active {
  transform: scale(0.96);
}
.filter-genre-pill.active {
  background: #e50914;
  color: #fff;
  border-color: #ff4d4d;
  font-weight: bold;
  box-shadow: 0 2px 8px rgba(229, 9, 20, 0.45);
}
.filter-genre-pill.active::before {
  content: "✓";
  font-size: 11px;
  font-weight: 900;
}
.genre-pill-badge {
  display: inline-flex;
  align-items: center;
  background: #161616;
  color: #00d2ff;
  border: 1px solid #1a3a4a;
  padding: 5px 12px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.15s ease;
  gap: 4px;
}
.genre-pill-badge:hover, .genre-pill-badge:active {
  background: #00d2ff;
  color: #000;
  border-color: #00d2ff;
}
.admin-genre-chip {
  background: #0f1c24;
  color: #38bdf8;
  border: 1px solid #164e63;
  padding: 2px 7px;
  border-radius: 10px;
  font-size: 10px;
  font-weight: bold;
  display: inline-block;
}
.filter-trigger-btn {
  background: #1c1c1c;
  color: #fff;
  border: 1px solid #333;
  padding: 8px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}
.filter-trigger-btn.has-filters {
  background: #e50914;
  border-color: #ff4d4d;
  color: #fff;
  box-shadow: 0 2px 10px rgba(229,9,20,0.4);
}
"""

if "/* ================= Filters & Genres System ================= */" not in content:
    content = content.replace("</style>", new_css + "\n</style>", 1)

# 2. Add Top-bar Filter Button next to search
old_topbar = """  <header class="top-bar">
    <button id="topSearchBtn" onclick="openSearch()" style="background:none;border:none;font-size:22px;cursor:pointer" title="بحث" aria-label="بحث">🔍</button>
    <button id="topSettingsBtn" onclick="openSettings()" style="background:none;border:none;font-size:22px;cursor:pointer" title="الإعدادات" aria-label="الإعدادات">⚙️</button>
  </header>"""

new_topbar = """  <header class="top-bar">
    <div style="display:flex;align-items:center;gap:6px">
      <button id="topSearchBtn" onclick="openSearch()" style="background:none;border:none;font-size:22px;cursor:pointer" title="بحث" aria-label="بحث">🔍</button>
      <button id="topFilterBtn" onclick="window.openFilterModal()" style="background:none;border:none;cursor:pointer;position:relative;display:flex;align-items:center;justify-content:center;color:#fff;padding:4px" title="تصفية المحتوى" aria-label="تصفية المحتوى">
        <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>
        </svg>
        <span id="topFilterBadge" style="display:none;position:absolute;top:0;right:0;background:#e50914;color:#fff;font-size:10px;font-weight:bold;width:15px;height:15px;border-radius:50%;align-items:center;justify-content:center;line-height:1">0</span>
      </button>
    </div>
    <button id="topSettingsBtn" onclick="openSettings()" style="background:none;border:none;font-size:22px;cursor:pointer" title="الإعدادات" aria-label="الإعدادات">⚙️</button>
  </header>"""

if old_topbar in content:
    content = content.replace(old_topbar, new_topbar, 1)

# 3. Add Modals: contentFilterModal & editContentModal
new_modals = """
  <!-- Content Filter Modal (Anime & Animation) -->
  <div id="contentFilterModal" class="ad-overlay" style="display:none;z-index:3800">
    <div class="ad-popup-card" style="max-width:480px;width:94%;background:#141414;border:1px solid #333;border-radius:20px;padding:20px 16px;text-align:right;color:#fff;direction:rtl;max-height:88vh;display:flex;flex-direction:column;box-shadow:0 10px 40px rgba(0,0,0,0.8)">
      <!-- Header -->
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;border-bottom:1px solid #242424;padding-bottom:10px;flex-shrink:0">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="font-size:20px;color:#e50914">🌪️</span>
          <h3 id="filterModalTitle" style="margin:0;font-size:18px;font-weight:900;color:#fff">تصفية الأنمي</h3>
        </div>
        <button type="button" onclick="window.closeFilterModal()" style="background:none;border:none;color:#aaa;font-size:22px;cursor:pointer;padding:4px 8px;line-height:1" title="إلغاء">✕</button>
      </div>

      <!-- Scrollable Filter Body -->
      <div style="overflow-y:auto;padding-right:4px;display:flex;flex-direction:column;gap:16px;flex:1">
        
        <!-- 1. Version (النسخة) -->
        <div>
          <label style="font-size:13px;font-weight:bold;color:#ddd;display:block;margin-bottom:8px">🎙️ النسخة:</label>
          <div id="filterVersionChips" style="display:flex;gap:8px;flex-wrap:wrap">
            <button type="button" class="filter-choice-chip active" data-val="all" onclick="window.selectFilterVersion('all')">الكل</button>
            <button type="button" class="filter-choice-chip" data-val="مترجم" onclick="window.selectFilterVersion('مترجم')">مترجم</button>
            <button type="button" class="filter-choice-chip" data-val="مدبلج" onclick="window.selectFilterVersion('مدبلج')">مدبلج</button>
          </div>
        </div>

        <!-- 2. Type / Category (نوع العمل / نوع الأنمي) -->
        <div>
          <label style="font-size:13px;font-weight:bold;color:#ddd;display:block;margin-bottom:8px">📺 نوع العمل:</label>
          <div id="filterCategoryChips" style="display:flex;gap:8px;flex-wrap:wrap">
            <button type="button" class="filter-choice-chip active" data-val="all" onclick="window.selectFilterCategory('all')">الكل</button>
            <button type="button" class="filter-choice-chip" data-val="مسلسل" onclick="window.selectFilterCategory('مسلسل')">مسلسل</button>
            <button type="button" class="filter-choice-chip" data-val="فلم" onclick="window.selectFilterCategory('فلم')">فيلم</button>
            <button type="button" class="filter-choice-chip" data-val="أوفا" onclick="window.selectFilterCategory('أوفا')">أوفا</button>
            <button type="button" class="filter-choice-chip" data-val="خاصة" onclick="window.selectFilterCategory('خاصة')">خاصة</button>
          </div>
        </div>

        <!-- 3. Year (السنة) -->
        <div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
            <label style="font-size:13px;font-weight:bold;color:#ddd">📅 سنة الإنتاج:</label>
            <span id="selectedYearDisplay" style="font-size:11px;color:#00d2ff">الكل</span>
          </div>
          <select id="filterYearSelect" class="input" style="margin:0;padding:10px 12px;background:#1a1a1a;border:1px solid #333;color:#fff;border-radius:10px;font-size:13px" onchange="window.onFilterYearChanged(this.value)">
            <option value="all">جميع السنوات</option>
            <option value="2026">2026</option>
            <option value="2025">2025</option>
            <option value="2024">2024</option>
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
            <option value="2017">2017</option>
            <option value="2016">2016</option>
            <option value="2015">2015</option>
            <option value="before_2015">قبل 2015</option>
          </select>
        </div>

        <!-- 4. Genres (التصنيفات) -->
        <div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
            <label style="font-size:13px;font-weight:bold;color:#ddd">🏷️ التصنيفات:</label>
            <div style="display:flex;align-items:center;gap:6px">
              <span id="filterSelectedGenresCount" style="font-size:11px;background:#222;color:#00d2ff;border:1px solid #333;padding:2px 8px;border-radius:12px">0 محدد</span>
              <button type="button" onclick="window.clearFilterModalGenresOnly()" style="background:none;border:none;color:#ff6b6b;font-size:11px;cursor:pointer;text-decoration:underline">إلغاء التحديد</button>
            </div>
          </div>
          <input id="filterGenreSearchInput" class="input" style="padding:8px 12px;margin-bottom:10px;font-size:12px;background:#181818;border:1px solid #282828" placeholder="🔍 ابحث عن تصنيف سريعاً (مثال: رياضي، أكشن، كوميدي...)" oninput="window.filterModalGenreList(this.value)">
          <div id="filterModalGenresGrid" style="display:flex;flex-wrap:wrap;gap:7px;max-height:220px;overflow-y:auto;padding:4px;border:1px solid #222;border-radius:12px;background:#0d0d0d"></div>
        </div>

      </div>

      <!-- Sticky Action Buttons -->
      <div style="display:flex;gap:8px;margin-top:14px;padding-top:12px;border-top:1px solid #242424;flex-shrink:0">
        <button type="button" onclick="window.applyContentFilters()" style="flex:2;background:linear-gradient(135deg,#e50914,#b80610);color:#fff;border:none;padding:12px 14px;border-radius:12px;font-weight:bold;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:6px;box-shadow:0 4px 15px rgba(229,9,20,0.35)">
          <span>✓ تطبيق</span>
        </button>
        <button type="button" onclick="window.resetContentFilters()" style="flex:1.2;background:#1e1e1e;color:#ff8080;border:1px solid #3a2222;padding:12px 10px;border-radius:12px;font-size:13px;font-weight:bold;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:4px">
          <span>مسح الفلاتر</span>
        </button>
        <button type="button" onclick="window.closeFilterModal()" style="flex:1;background:#181818;color:#aaa;border:1px solid #2c2c2c;padding:12px 10px;border-radius:12px;font-size:13px;cursor:pointer">
          <span>إلغاء</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Complete Edit Content & Genres Modal (Admin Only) -->
  <div id="editContentModal" class="ad-overlay" style="display:none;z-index:3750">
    <div class="ad-popup-card" style="max-width:480px;width:92%;background:#141414;border:1px solid #333;border-radius:18px;padding:18px 16px;text-align:right;color:#fff;direction:rtl;max-height:90vh;display:flex;flex-direction:column;box-shadow:0 10px 40px rgba(0,0,0,0.85)">
      <!-- Header -->
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;border-bottom:1px solid #242424;padding-bottom:10px;flex-shrink:0">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="font-size:20px;color:#00d2ff">✏️</span>
          <h3 style="margin:0;font-size:17px;font-weight:900;color:#fff">تعديل العمل والتصنيفات</h3>
        </div>
        <button type="button" onclick="window.closeEditContentModal()" style="background:none;border:none;color:#aaa;font-size:22px;cursor:pointer;padding:4px 8px;line-height:1">✕</button>
      </div>

      <!-- Scrollable Body -->
      <div style="overflow-y:auto;padding-right:4px;display:flex;flex-direction:column;gap:12px;flex:1">
        <div>
          <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">الاسم الأساسي للعمل:</label>
          <input id="editContentTitleInput" class="input" style="margin:0" placeholder="اسم العمل">
        </div>

        <!-- Alternative Titles -->
        <div style="background:#0e0e0e;border:1px solid #242424;border-radius:10px;padding:10px;display:flex;flex-direction:column;gap:6px">
          <label style="font-size:12px;font-weight:bold;color:#00d2ff">🏷️ الأسماء البديلة للبحث:</label>
          <div style="display:flex;gap:6px">
            <input id="editContentNewAltInput" class="input" style="flex:1;margin:0" placeholder="أدخل اسماً بديلاً ثم اضغط إضافة" onkeydown="if(event.key==='Enter'){event.preventDefault();window.addEditModalAltTitle();}">
            <button type="button" onclick="window.addEditModalAltTitle()" style="background:#00d2ff;color:#000;border:none;padding:8px 12px;border-radius:8px;font-size:12px;font-weight:bold;cursor:pointer">➕ إضافة</button>
          </div>
          <div id="editContentAltsContainer" style="display:flex;flex-wrap:wrap;gap:6px;min-height:24px;margin-top:4px"></div>
        </div>

        <!-- Section: نوع الأنمي & النسخة -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
          <div>
            <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">نوع العمل (نوع الأنمي):</label>
            <select id="editContentCategorySelect" class="input" style="margin:0">
              <option value="مسلسل">مسلسل</option>
              <option value="فلم">فلم</option>
              <option value="أوفا">أوفا</option>
              <option value="خاصة">خاصة</option>
              <option value="أونا">أونا</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">النسخة:</label>
            <select id="editContentVersionSelect" class="input" style="margin:0">
              <option value="مترجم">مترجم</option>
              <option value="مدبلج">مدبلج</option>
              <option value="">غير محدد</option>
            </select>
          </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
          <div>
            <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">السنة:</label>
            <input id="editContentYearInput" type="number" class="input" style="margin:0" placeholder="السنة (مثال: 2024)">
          </div>
          <div>
            <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">القسم (anime/animation):</label>
            <select id="editContentTypeSelect" class="input" style="margin:0">
              <option value="anime">أنمي</option>
              <option value="animation">أنميشن</option>
            </select>
          </div>
        </div>

        <!-- Section: التصنيفات (Genres) -->
        <div style="background:#0e0e0e;border:1px solid #242424;border-radius:10px;padding:10px;display:flex;flex-direction:column;gap:8px">
          <div style="display:flex;align-items:center;justify-content:space-between">
            <label style="font-size:12px;font-weight:bold;color:#00d2ff">🏷️ التصنيفات (اضغط لتحديد أو إلغاء أي تصنيف):</label>
            <span id="editContentGenresCount" style="font-size:11px;color:#888">0 محدد</span>
          </div>
          <input id="editContentGenreFilterInput" class="input" style="padding:6px 10px;margin:0;font-size:11px;background:#181818;border:1px solid #282828" placeholder="🔍 فلتر قائمة التصنيفات..." oninput="window.filterEditContentGenreChips(this.value)">
          <div id="editContentGenresList" style="display:flex;flex-wrap:wrap;gap:6px;max-height:180px;overflow-y:auto;padding:4px"></div>
        </div>

        <!-- Description -->
        <div>
          <label style="font-size:12px;color:#aaa;display:block;margin-bottom:4px">الوصف / القصة:</label>
          <textarea id="editContentDescInput" class="input" rows="3" style="margin:0;resize:vertical;min-height:70px" placeholder="وصف العمل"></textarea>
        </div>

        <div id="editContentStatusMsg" style="font-size:12px;color:#aaa;text-align:center;min-height:16px"></div>
      </div>

      <!-- Actions -->
      <div style="display:flex;gap:8px;margin-top:12px;padding-top:10px;border-top:1px solid #242424;flex-shrink:0">
        <button id="saveEditContentBtn" type="button" onclick="window.saveContentFromModal()" style="flex:1;background:linear-gradient(135deg,#e50914,#b80610);color:#fff;border:none;padding:12px;border-radius:10px;font-weight:bold;font-size:14px;cursor:pointer">💾 حفظ التعديلات والتصنيفات</button>
        <button type="button" onclick="window.closeEditContentModal()" style="background:#1c1c1c;color:#aaa;border:1px solid #333;padding:12px 18px;border-radius:10px;cursor:pointer;font-size:13px">إلغاء</button>
      </div>
    </div>
  </div>
"""

if 'id="contentFilterModal"' not in content:
    # Insert right before <script type="module">
    target_insert = '<script type="module">'
    content = content.replace(target_insert, new_modals + "\n" + target_insert, 1)

with open('app/src/main/assets/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Modals and CSS injected successfully!')
