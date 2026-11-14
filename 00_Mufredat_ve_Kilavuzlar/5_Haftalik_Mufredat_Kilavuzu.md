# Mentorluk Programına Hoş Geldiniz!

Veri Bilimi topluluğumuzun **5 haftalık uçtan uca "Python, Veri Analizi ve Makine Öğrenmesi"** programına hoş geldiniz. Bu dönem her biriniz **2-3 kişilik bir takımda**, size özel bir **alt mentorla** birlikte ilerleyeceksiniz.

Temel kaynaklarımız BTK Akademi'deki ücretsiz eğitimler:
- **Atıl Samancıoğlu — "Veri Bilimi için Python ve Tensorflow"** (1-3. haftalar)
- **Şadi Evren Şeker — "Python ile Makine Öğrenmesi"** (3-5. haftalar)

## Program İşleyişi
1. Her hafta belirlenen modülleri izleyip kendi bilgisayarınızda (veya Google Colab'da) uygulayacaksınız.
2. Ödevinizi **Cumartesi 23:59'a kadar** GitHub'a Pull Request (PR) olarak göndereceksiniz.
3. Alt mentorunuz PR'ınızı inceleyecek ve Pazar günü takımınızla kısa bir değerlendirme toplantısı yapacak.
4. Takıldığınız yerde **önce alt mentorunuza** sorun. O da çözemezse soru baş mentora iletilir.

> [!TIP]
> Program bilerek kısa tutuldu: 5 hafta boyunca haftada yaklaşık **4-6 saat** ayırmanız yeterli. Önemli olan her hafta küçük ama düzenli bir adım atmak.

---

# 5 Haftalık Program

## 1. Hafta: Python Hızlı Başlangıç ve GitHub
- **Kaynak:** Atıl Samancıoğlu
- **İzlenecek Konular:** Anaconda / Jupyter Notebook kurulumu, Değişkenler, Veri Tipleri, Listeler, Sözlükler, If kontrolleri, Döngüler (For/While), Fonksiyonlar.
- **Haftalık Görev (PR #1):**
  - Çalışma ortamını kurun ve programın GitHub reposunu fork'layın.
  - Bir öğrenci listesini (isim, not, bölüm içeren sözlüklerden oluşan bir liste) alıp **notu belirli bir değerin üzerindeki öğrencileri filtreleyen** ve **bölümlere göre not ortalamasını hesaplayan** fonksiyonlar yazın.
  - İlk PR'ınızı açın.
- **Kontrol Sorusu:** Liste ile sözlük arasındaki fark nedir, hangi durumda hangisini kullanırsınız?

## 2. Hafta: Verinin Matematiği ve Manipülasyonu (NumPy & Pandas)
- **Kaynak:** Atıl Samancıoğlu
- **İzlenecek Konular:** NumPy dizileri, matris işlemleri, Pandas Series & DataFrame, indeksleme, filtreleme, eksik veriler, GroupBy.
- **Haftalık Görev (PR #2):**
  - Kaggle'dan ham bir veri seti indirin (öneri: *Titanic*, *House Prices* veya ilginizi çeken herhangi bir set).
  - Veriyi Pandas ile okuyun, `info()` / `describe()` ile inceleyin.
  - Eksik verileri tespit edip **neden o yöntemi seçtiğinizi açıklayarak** doldurun veya silin.
  - En az 2 farklı `groupby` analizi yapın.
- **Kontrol Sorusu:** Eksik bir değeri ortalama ile doldurmak ne zaman yanıltıcı olabilir?

## 3. Hafta: Keşifsel Veri Analizi (EDA), Görselleştirme ve Veri Hazırlığı
- **Kaynak:** Atıl Samancıoğlu (Matplotlib) + Şadi Evren Şeker (Veri Analizi Proje Yönetimi ve Problem Tipleri, Veri Ön İşleme)
- **İzlenecek Konular:** Matplotlib ile çizgi, bar, scatter, histogram grafikleri; subplots; kategorik verileri sayısallaştırma (encoding); eğitim/test ayırma (`train_test_split`).
- **Haftalık Görev (PR #3):**
  - 2. haftada temizlediğiniz veri setinden **en az 3 farklı grafik** çizin ve her birinin altına **1-2 cümlelik yorum** yazın.
  - Kategorik sütunları encode edin ve veriyi eğitim/test olarak ayırın.
- **Kontrol Sorusu:** Modeli neden tüm veriyle değil de ayrı bir test kümesiyle değerlendiririz?

## 4. Hafta: Makine Öğrenmesi — Tahmin (Regresyon)
- **Kaynak:** Şadi Evren Şeker
- **İzlenecek Konular:** Basit Doğrusal Regresyon, Çoklu Doğrusal Regresyon, Karar Ağacı ile Tahmin, Rassal Orman (Random Forest) ile Tahmin, Değerlendirme ve Metotların Karşılaştırılması (R², hata metrikleri).
- **Haftalık Görev (PR #4):**
  - Sürekli bir değeri (örn. ev fiyatı, maaş) tahmin eden bir problem seçin.
  - **Doğrusal Regresyon** ve **Random Forest** modellerini eğitip R² skorlarını karşılaştırın.
  - Hangi modelin neden daha iyi çalıştığını kısaca yorumlayın.
- **Kontrol Sorusu:** R² skoru 0.95 çıktı; bu modelin kesinlikle iyi olduğu anlamına gelir mi?

## 5. Hafta: Sınıflandırma ve Bitirme Projesi
- **Kaynak:** Şadi Evren Şeker
- **İzlenecek Konular:** Sınıflandırmaya Giriş, Lojistik Regresyon, K-NN, Karar Ağacı ve Random Forest ile Sınıflandırma, Sınıflandırma Algoritmalarının Değerlendirilmesi (Accuracy, Precision, Recall, Confusion Matrix).
- **Bitirme Projesi (PR #5 — Zorunlu):** Bir sınıflandırma veri seti seçin (örn. Titanic hayatta kalma, hastalık tespiti, spam/phishing tespiti) ve **uçtan uca** bir notebook hazırlayın:
  1. Veri okuma ve temizleme
  2. En az 3 grafikle keşifsel analiz
  3. Encoding ve eğitim/test ayrımı
  4. **En az 2 farklı sınıflandırma modeli** (örn. Lojistik Regresyon ve Random Forest)
  5. Confusion Matrix, Accuracy ve Recall değerlerinin yorumlanması
  6. Notebook başında 3-5 cümlelik bir özet: *"Ne yaptım, ne buldum?"*
- **Mezuniyet:** Projeler son hafta yapılacak kısa bir **demo gününde** (kişi başı 5 dk) sunulur.

---

## Ödev Klasör Yapısı

Ödevlerinizi şu klasöre yükleyin:

```
01_Takimlar/Takim_XX_MentorAdi/AdinizSoyadiniz/haftaX/odevX.ipynb
```

Detaylı adımlar için: [Github_Takim_Kullanimi.md](Github_Takim_Kullanimi.md)
