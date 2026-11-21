# Modül 2 — Makine Öğrenmesi Temelleri (3 Hafta)

Tebrikler! Modül 1'i tamamlayarak Makine Öğrenmesi modülüne geçmeye hak kazandınız. 🎉

- **Kaynak:** BTK Akademi — Şadi Evren Şeker, *"Python ile Makine Öğrenmesi"* (ücretsiz)
- **Haftalık yük:** yaklaşık 3-5 saat
- **Teslim:** Her hafta **Cumartesi 23:59**'a kadar GitHub'a Pull Request (PR)

> [!NOTE]
> Bu modülde bilerek **sadece en temel ve en çok kullanılan** konulara odaklanıyoruz: regresyon, lojistik regresyon, karar ağacı / random forest ve model değerlendirme. Amaç çok algoritma görmek değil, **bir modeli baştan sona kurup yorumlayabilmek.**

> [!IMPORTANT]
> **Mezuniyet şartı:** 3 haftanın en az 2'sini tamamlamak **ve** 3. haftadaki bitirme projesini teslim etmek.

---

## Hafta 1: Makine Öğrenmesine Giriş ve Doğrusal Regresyon
- **İzlenecek Bölümler:** 2. Veri Analizi Proje Yönetimi ve Problem Tipleri, 3. Basit Doğrusal Regresyon, 4. Çoklu Doğrusal Regresyon.
- **Görev (PR #1):**
  - Sürekli bir değeri tahmin eden bir veri seti seçin (örn. ev fiyatı veya maaş).
  - Veriyi eğitim/test olarak ayırın (`train_test_split`).
  - Bir **Doğrusal Regresyon** modeli eğitin ve test verisindeki **R² skorunu** yazdırın.
- **Kontrol Sorusu:** Modeli neden tüm veriyle değil de ayrı bir test kümesiyle değerlendiririz?

## Hafta 2: Sınıflandırma ve Model Değerlendirme
- **İzlenecek Bölümler:** 10. Sınıflandırmaya Giriş, 11. Lojistik Regresyon, 19. Sınıflandırma Algoritmalarının Değerlendirilmesi.
- **Görev (PR #2):**
  - Modül 1'de kullandığınız *Titanic* verisiyle hayatta kalmayı tahmin eden bir **Lojistik Regresyon** modeli kurun.
  - **Accuracy** değerini ve **Confusion Matrix**'i yazdırıp kısaca yorumlayın.
- **Kontrol Sorusu:** Accuracy %90 çıktı; bu model her durumda iyi midir? (İpucu: dengesiz veri)

## Hafta 3: Karar Ağacı, Random Forest ve Bitirme Projesi
- **İzlenecek Bölümler:** 16. Karar Ağacı ile Sınıflandırma, 17. Rassal Orman (Random Forest).
- **Bitirme Projesi (PR #3 — Zorunlu):** Bir sınıflandırma veri seti seçin (Titanic de olabilir) ve tek bir notebook'ta:
  1. Veriyi temizleyin ve eğitim/test olarak ayırın.
  2. **Lojistik Regresyon** ve **Random Forest** modellerini eğitin.
  3. İki modelin Accuracy ve Confusion Matrix sonuçlarını karşılaştırın.
  4. Notebook'un başına 3-5 cümlelik özet ekleyin: *"Ne yaptım, hangi model daha iyi, neden?"*
- **Demo Günü:** Bitirme projeleri program sonunda kişi başı 5 dakikalık kısa sunumlarla paylaşılır.

---

## İsteyenler İçin Ekstra (Zorunlu Değil)
Programı bitirip devam etmek isteyenler aynı eğitimden şu bölümlere bakabilir:
- K-NN (K En Yakın Komşu)
- Karar Ağacı ve Random Forest ile Tahmin (regresyon)
- Kümeleme ve K-Means

---

## Ödev Klasör Yapısı

```
01_Takimlar/Takim_XX_MentorAdi/AdinizSoyadiniz/modul2/haftaX/odevX.ipynb
```

Detaylı adımlar için: [Github_Takim_Kullanimi.md](Github_Takim_Kullanimi.md)
