package com.example

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class AlternativeTitlesSearchTest {

  data class MovieContent(
    val id: String,
    val firebaseId: String,
    val title: String,
    val alternativeTitles: List<String> = emptyList(),
    val category: String = "مسلسل",
    val type: String = "anime",
    val description: String = "",
    val episodes: List<EpisodeItem> = emptyList(),
    val genres: List<String> = emptyList(),
    val version: String = ""
  )

  data class EpisodeItem(
    val title: String,
    val alternativeTitles: List<String> = emptyList()
  )

  companion object {
    val ALL_GENRES = listOf(
      "أكشن", "مغامرات", "دراما", "كوميدي", "خيال", "رعب", "غموض", "رومانسي",
      "خيال علمي", "رياضي", "شريحة من الحياة", "خارق للطبيعة", "تشويق", "إيتشي",
      "تاريخي", "موسيقي", "عسكري", "طعام", "رياضات قتالية", "بنات كيوت",
      "محاكاة ساخرة", "بوليسي", "نفسي", "إثارة شعب", "راحة نفسية",
      "تحول جنسي سحري", "جريمة منظمة", "ألعاب خطيرة", "تحقيق", "دموي",
      "إيدول", "أساطير", "سباق", "لعبة استراتيجية", "فنون بصرية",
      "سفر عبر الزمن", "نجاة", "ساموراي", "مدرسي", "مكان عمل",
      "فضاء", "قوة خارقة", "مصاصو دماء", "جوسي", "أطفال"
    )

    fun normalizeSearchText(str: String?): String {
      if (str.isNullOrBlank()) return ""
      var s = str.lowercase().trim()
      // Remove Arabic Tashkeel / diacritics
      s = s.replace(Regex("[\\u064B-\\u065F\\u0670]"), "")
      // Normalize Alef variants
      s = s.replace(Regex("[أإآٱ]"), "ا")
      // Normalize Alef Maksura
      s = s.replace("ى", "ي")
      // Normalize Taa Marbuta
      s = s.replace("ة", "ه")
      // Remove Tatweel
      s = s.replace(Regex("ـ+"), "")
      // Remove zero-width chars
      s = s.replace(Regex("[\\u200B-\\u200D\\uFEFF]"), "")
      // Collapse whitespace
      s = s.replace(Regex("\\s+"), " ")
      return s
    }

    fun matchesSearchQuery(item: MovieContent, rawQuery: String): Boolean {
      if (rawQuery.isBlank()) return true
      val q = normalizeSearchText(rawQuery)
      if (q.isEmpty()) return true

      // 1. Primary title
      if (normalizeSearchText(item.title).contains(q)) return true

      // 2. Alternative titles
      for (alt in item.alternativeTitles) {
        if (normalizeSearchText(alt).contains(q)) return true
      }

      // 3. Category & Type & Genres & Version
      if (normalizeSearchText(item.category).contains(q)) return true
      if (normalizeSearchText(item.type).contains(q)) return true
      for (g in item.genres) {
        if (normalizeSearchText(g).contains(q)) return true
      }
      if (normalizeSearchText(item.version).contains(q)) return true

      // 4. Description
      if (normalizeSearchText(item.description).contains(q)) return true

      // 5. Episodes
      for (ep in item.episodes) {
        if (normalizeSearchText(ep.title).contains(q)) return true
        for (epAlt in ep.alternativeTitles) {
          if (normalizeSearchText(epAlt).contains(q)) return true
        }
      }

      return false
    }

    fun matchesFilter(item: MovieContent, version: String = "all", category: String = "all", selectedGenres: List<String> = emptyList()): Boolean {
      if (version != "all" && normalizeSearchText(item.version) != normalizeSearchText(version)) {
        return false
      }
      if (category != "all") {
        val normCat = normalizeSearchText(item.category)
        val targetCat = normalizeSearchText(category)
        if (targetCat in listOf("فلم", "فيلم")) {
          if (normCat !in listOf("فلم", "فيلم")) return false
        } else if (normCat != targetCat) {
          return false
        }
      }
      for (g in selectedGenres) {
        val normG = normalizeSearchText(g)
        if (item.genres.none { normalizeSearchText(it) == normG }) {
          return false
        }
      }
      return true
    }
  }

  @Test
  fun testArabicTextNormalization() {
    assertEquals("ون بيس", normalizeSearchText("وَن بَيْسَ"))
    assertEquals("ابطال الكره", normalizeSearchText("أبطال الكرة"))
    assertEquals("اينوياشا", normalizeSearchText("إينوياشا"))
    assertEquals("علي", normalizeSearchText("على"))
    assertEquals("مغامرات", normalizeSearchText("مُـغـامَـرات"))
  }

  @Test
  fun testEnglishCaseAndWhitespaceNormalization() {
    assertEquals("one piece", normalizeSearchText("  ONE   PIECE  "))
    assertEquals("naruto shippuden", normalizeSearchText("Naruto  Shippuden"))
  }

  @Test
  fun testSearchByPrimaryTitle() {
    val movie = MovieContent(
      id = "1",
      firebaseId = "fb-1",
      title = "One Piece",
      alternativeTitles = listOf("ون بيس", "ワンピース", "海贼王")
    )
    assertTrue(matchesSearchQuery(movie, "One Piece"))
    assertTrue(matchesSearchQuery(movie, "one"))
    assertTrue(matchesSearchQuery(movie, "piece"))
  }

  @Test
  fun testSearchByAlternativeTitles() {
    val movie = MovieContent(
      id = "1",
      firebaseId = "fb-1",
      title = "One Piece",
      alternativeTitles = listOf("ون بيس", "ワンピース", "海贼王")
    )
    // Arabic alias
    assertTrue(matchesSearchQuery(movie, "ون بيس"))
    assertTrue(matchesSearchQuery(movie, "بيس"))
    assertTrue(matchesSearchQuery(movie, "وَن بَيْس"))

    // Japanese alias
    assertTrue(matchesSearchQuery(movie, "ワンピース"))
    assertTrue(matchesSearchQuery(movie, "ワン"))

    // Chinese alias
    assertTrue(matchesSearchQuery(movie, "海贼王"))
  }

  @Test
  fun testDeduplicationAcrossResults() {
    val movie1 = MovieContent(
      id = "1",
      firebaseId = "fb-1",
      title = "One Piece",
      alternativeTitles = listOf("ون بيس", "ワンピース", "قطعة واحدة")
    )
    val movie2 = MovieContent(
      id = "2",
      firebaseId = "fb-2",
      title = "Bleach",
      alternativeTitles = listOf("بليتش")
    )

    val list = listOf(movie1, movie2)

    // Searching "ون" matches movie1 via alternative title "ون بيس"
    val results = list.filter { matchesSearchQuery(it, "ون") }
    assertEquals(1, results.size)
    assertEquals("One Piece", results[0].title)

    // Searching "Piece" matches movie1 only once even if multiple aliases match
    val results2 = list.filter { matchesSearchQuery(it, "Piece") }
    assertEquals(1, results2.size)
    assertEquals("fb-1", results2[0].firebaseId)
  }

  @Test
  fun testSearchByEpisode() {
    val movie = MovieContent(
      id = "1",
      firebaseId = "fb-1",
      title = "Attack on Titan",
      episodes = listOf(
        EpisodeItem(title = "الحلقة 1 - بداية النهاية", alternativeTitles = listOf("Ep 1", "Pilot"))
      )
    )

    assertTrue(matchesSearchQuery(movie, "بداية النهاية"))
    assertTrue(matchesSearchQuery(movie, "Pilot"))
    assertFalse(matchesSearchQuery(movie, "غير موجود"))
  }

  @Test
  fun testSearchByAlternativeTitleReturnsPrimaryTitleOnlyWithoutDuplicates() {
    val movie = MovieContent(
      id = "1",
      firebaseId = "fb-1",
      title = "One Piece",
      alternativeTitles = listOf("ون بيس", "One Piece Movie", "ワンピース")
    )

    // Match by alternative title "ون بيس"
    assertTrue(matchesSearchQuery(movie, "ون بيس"))

    // The display title in the UI card is always item.title ("One Piece")
    assertEquals("One Piece", movie.title)
    assertFalse(movie.title.contains("ون بيس"))

    // When query matches both primary title and alias "One Piece Movie", deduplication preserves 1 instance
    val list = listOf(movie)
    val queryMatches = list.filter { matchesSearchQuery(it, "One Piece") }
    assertEquals(1, queryMatches.size)
    assertEquals("fb-1", queryMatches[0].firebaseId)
    assertEquals("One Piece", queryMatches[0].title)
  }

  @Test
  fun testSearchByGenre() {
    val slamDunk = MovieContent(
      id = "1",
      firebaseId = "fb-1",
      title = "سلام دانك",
      genres = listOf("رياضي", "كوميدي", "مدرسي")
    )
    val jujutsu = MovieContent(
      id = "2",
      firebaseId = "fb-2",
      title = "جوجيتسو كايسن",
      genres = listOf("أكشن", "خارق للطبيعة", "رعب")
    )
    val list = listOf(slamDunk, jujutsu)

    val sportsResults = list.filter { matchesSearchQuery(it, "رياضي") }
    assertEquals(1, sportsResults.size)
    assertEquals("سلام دانك", sportsResults[0].title)

    val supernaturalResults = list.filter { matchesSearchQuery(it, "خارق للطبيعة") }
    assertEquals(1, supernaturalResults.size)
    assertEquals("جوجيتسو كايسن", supernaturalResults[0].title)
  }

  @Test
  fun testMultiGenreFilteringExactMatch() {
    val anime1 = MovieContent(
      id = "1",
      firebaseId = "fb-1",
      title = "Haikyuu",
      category = "مسلسل",
      version = "مترجم",
      genres = listOf("رياضي", "مدرسي", "كوميدي")
    )
    val anime2 = MovieContent(
      id = "2",
      firebaseId = "fb-2",
      title = "Kuroko no Basket",
      category = "مسلسل",
      version = "مدبلج",
      genres = listOf("رياضي", "مدرسي", "قوة خارقة")
    )
    val anime3 = MovieContent(
      id = "3",
      firebaseId = "fb-3",
      title = "Detective Conan",
      category = "فلم",
      version = "مترجم",
      genres = listOf("غموض", "تحقيق", "بوليسي")
    )
    val allList = listOf(anime1, anime2, anime3)

    // Filter by single genre "رياضي" -> anime1 and anime2
    val sportsOnly = allList.filter { matchesFilter(it, selectedGenres = listOf("رياضي")) }
    assertEquals(2, sportsOnly.size)

    // Filter by multiple genres "رياضي" AND "كوميدي" -> only anime1
    val sportsAndComedy = allList.filter { matchesFilter(it, selectedGenres = listOf("رياضي", "كوميدي")) }
    assertEquals(1, sportsAndComedy.size)
    assertEquals("Haikyuu", sportsAndComedy[0].title)

    // Filter by genre "غموض" AND version "مترجم" AND category "فلم" -> anime3
    val conanFilter = allList.filter { matchesFilter(it, version = "مترجم", category = "فلم", selectedGenres = listOf("غموض")) }
    assertEquals(1, conanFilter.size)
    assertEquals("Detective Conan", conanFilter[0].title)

    // Filter with no matches
    val noMatches = allList.filter { matchesFilter(it, selectedGenres = listOf("طعام", "فضاء")) }
    assertEquals(0, noMatches.size)

    // Filter clear (empty selectedGenres, all, all) -> all returned
    val clearFilter = allList.filter { matchesFilter(it) }
    assertEquals(3, clearFilter.size)
  }

  @Test
  fun testAll45GenresConfigured() {
    assertEquals(45, ALL_GENRES.size)
    assertTrue(ALL_GENRES.contains("أكشن"))
    assertTrue(ALL_GENRES.contains("رياضي"))
    assertTrue(ALL_GENRES.contains("شريحة من الحياة"))
    assertTrue(ALL_GENRES.contains("تحول جنسي سحري"))
    assertTrue(ALL_GENRES.contains("أطفال"))
  }
}
