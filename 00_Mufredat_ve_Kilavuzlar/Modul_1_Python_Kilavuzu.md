# Modül 1 — Python ve Veri Analizi (3 Hafta)

Mentorluk programına hoş geldiniz! Bu dönem her biriniz **küçük bir takımda**, size özel bir mentorla birlikte ilerleyeceksiniz.

- **Kaynak:** BTK Akademi — Atıl Samancıoğlu, *"Veri Bilimi için Python ve Tensorflow"* (ücretsiz)
- **Haftalık video yükü:** Yaklaşık 1.5 – 2 saat (seçilen kritik videolar)
- **Teslim:** Her hafta **Pazar 23:59**'a kadar GitHub'a Pull Request (PR)

> [!IMPORTANT]
> **Modül 2'ye (Makine Öğrenmesi) geçiş şartı:** Modül 1'in **3 haftasının tamamını** tamamlamak (3. haftadaki mini proje dahil). Eksiği kalanlar modül sonrasındaki **ara haftada** telafi edebilir.

## Program İşleyişi
1. **Modül başında** baş mentorla genel açılış toplantısı, ardından alt mentorunuzla takım toplantısı yapılır. Toplantılar her hafta tekrarlanmaz.
2. Aşağıda her hafta için listelenen **zorunlu videoları** izleyip kendi bilgisayarınızda (veya Google Colab'da) uygulayın. Opsiyonel/atlanabilecek videoları izlemenize gerek yoktur.
3. Ödevinizi **Pazar 23:59**'a kadar PR olarak gönderin.
4. Alt mentorunuz PR'ınızı inceleyip geri bildirim verir.
5. Takıldığınız yerde **önce mentorunuza** takım grubunuzdan sorun.

---

## 1. Hafta: Python Temelleri ve GitHub

Bu haftanın hedefi: Python ortamını kurmak, temel veri yapılarını kavramak, fonksiyon yazmak ve ilk GitHub PR'ını açmak.

### 🎬 İzlenecek Zorunlu Videolar (~1 saat 45 dk)
BTK Akademi — **Bölüm 3 (Python Temelleri)** altından:
- `3.2` Jupyter Notebook Kullanımı *(15 dk)* — Çalışma ortamı
- `3.3` Değişkenler *(7 dk)*
- `3.6` String & `3.7` Slicing *(30 dk)* — Metinler ve veri dilimleme mantığı
- `3.9` Listelere Giriş & `3.10` Liste Metodları *(18 dk)* — En sık kullanılan veri yapısı
- `3.12` Sözlükler Giriş *(15 dk)* — Key-Value (anahtar-değer) mantığı
- `3.15` Bool & `3.16` Kıyaslamalar *(15 dk)* — True/False mantığı ve karşılaştırmalar
- `3.17` Eğer Kontrolleri (If-Else) *(10 dk)* — Koşullu yapılar
- `3.20` For Döngüsü Giriş *(10 dk)* — Veri üzerinde dönme
- `3.24` Veri Bilimi Önemli Metodlar *(10 dk)* — `range`, `enumerate`, `zip` vb.
- `3.27` Fonksiyonlar & `3.28` Girdi Çıktı (`return`) *(20 dk)* — Kod bloklarını fonksiyonlaştırma

> [!TIP]
> **Atlayabileceğiniz / Opsiyonel Videolar:** `3.4 - 3.5` (Sayılar detayları), `3.11` (İleri Seviye Listeler), `3.13` (Set), `3.14` (Tuple), `3.18 - 3.19` (Eğer detayları), `3.21 - 3.23` (While detayları), `3.25 - 3.26` (Random / İleri Seviye), `3.29` (*args, **kwargs), `3.30 - 3.31` (Kapsam/Scope), `3.32 - 3.33` (Hesap Makinesi & Hata Yönetimi). Bunları izlemenize gerek yoktur.

### 📝 Görev (PR #1)
- Çalışma ortamını kurun ve programın GitHub reposunu fork'layın.
- Öğrenci bilgilerini (isim, not, bölüm) içeren bir liste oluşturun; **notu belirli bir değerin üzerindeki öğrencileri döndüren** ve **bölümlere göre ortalama hesaplayan** bir fonksiyon yazın.
- İlk PR'ınızı açın.

### ❓ Kontrol Sorusu
Liste ile sözlük arasındaki temel fark nedir, hangi durumda hangisini tercih edersiniz?

---

## 2. Hafta: NumPy ve Pandas ile Veri İşleme

Bu haftanın hedefi: Tablolu verileri Pandas ile okumak, filtrelemek, eksik verileri temizlemek ve özet istatistikler (`groupby`) çıkarmak.

### 🎬 İzlenecek Zorunlu Videolar (~1 saat 30 dk)
BTK Akademi — **Bölüm 5 (NumPy) & Bölüm 6 (Pandas)** altından:
- **NumPy (Özet):**
  - `5.1` NumPy Giriş & `5.2` NumPy Başlangıç *(11 dk)*
  - `5.3` NumPy Methodlar *(10 dk)* — `arange`, `zeros`, `linspace`
  - `5.6` NumPy İndeksler *(11 dk)*
  - `5.8` NumPy Operasyonlar *(8 dk)* — Vektörel işlemler
- **Pandas (Ana Odak):**
  - `6.1` Pandas Giriş & `6.2` Series *(12 dk)*
  - `6.4` Data Frame Nedir? *(10 dk)* — Tablo yapısı
  - `6.5` Data Frame İndeksler *(13 dk)* — Sütun seçme ve koşullu filtreleme
  - `6.8` Eksik Veriler (`dropna`, `fillna`) *(11 dk)* — Veri temizleme
  - `6.9` Gruplandırmak (`groupby`) *(9 dk)* — Kategori bazlı özet çıkarma
  - `6.13` Excelle / CSV ile Çalışmak *(9 dk)* — Veri seti yükleme

> [!TIP]
> **Atlayabileceğiniz / Opsiyonel Videolar:** `5.4 - 5.5` (Dizi metodları devamı), `5.7` (Matrix İndeksler), `6.3` (Series Özellikleri), `6.6` (İndeks Değiştirme), `6.7` (Multi İndeks — kesinlikle atlayın, kafa karıştırır), `6.10 - 6.11` (Concat & Merge), `6.12` (İleri Operasyonlar).

### 📝 Görev (PR #2)
- Kaggle'dan bir veri seti indirin (öneri: *Titanic*).
- Veriyi Pandas ile okuyup `info()` ve `describe()` ile inceleyin.
- Eksik verileri bulun ve **neden o yöntemi seçtiğinizi açıklayarak** doldurun veya silin.
- En az 1 tane anlamlı `groupby` analizi yapın (örn. cinsiyete göre hayatta kalma oranı).

### ❓ Kontrol Sorusu
Eksik bir değeri ortalama ile doldurmak ne zaman yanıltıcı olabilir?

---

## 3. Hafta: Veri Görselleştirme ve Modül 1 Mini Projesi

Bu haftanın hedefi: Temel grafikleri çizip yorumlamak ve Modül 1'i uçtan uca bir mini analiz projesiyle tamamlamak.

### 🎬 İzlenecek Zorunlu Videolar (~40 dk)
BTK Akademi — **Bölüm 7 (Matplotlib)** altından:
- `7.1` Matplotlib Giriş & `7.2` Matplotlib Başlangıç *(14 dk)* — `plt.plot()`, `plt.show()`
- `7.3` Özelleştirme *(15 dk)* — Eksen isimlendirme, başlık, renkler ve etiketler
- `7.5` Subplots *(5 dk)* — Yan yana birden fazla grafik yerleştirme
- `7.8` Farklı Grafik Çeşitleri *(6 dk)* — Bar, Scatter ve Histogram grafikleri

> [!TIP]
> **Atlayabileceğiniz / Opsiyonel Videolar:** `7.4` (İç İçe Grafikler), `7.6` (Görsel Geliştirmeler), `7.7` (Görsellik İleri Seviye).

### 📝 Mini Proje (PR #3 — ZORUNLU)
Bu hafta video süresi bilerek kısa tutulmuştur. Kalan sürenizi 2. haftada temizlediğiniz veri setiyle hazırlayacağınız **Mini Proje Notebook'una** ayırın:
1. **3 farklı grafik** çizin (örn. dağılım için histogram, kategorik için bar chart, ilişki için scatter plot).
2. Her grafiğin altına **1-2 cümlelik çıkarım/yorum** yazın.
3. Notebook'un başına 2-3 cümlelik bir özet ekleyin: *"Bu veri setinde ne inceledim ve ne buldum?"*

### ❓ Kontrol Sorusu
Hangi tür veri için bar grafiği, hangisi için histogram uygundur?

---

## Ödev Klasör Yapısı

```
01_Takimlar/Takim_XX_MentorAdi/Adiniz_Soyadiniz/modul1/haftaX/odevX.ipynb
```

Detaylı adımlar için: [Github_Takim_Kullanimi.md](Github_Takim_Kullanimi.md)

Modül 1'in 3 haftasını eksiksiz tamamlayanlar [Modül 2 — Makine Öğrenmesi](Modul_2_Makine_Ogrenmesi_Kilavuzu.md) aşamasına geçmeye hak kazanır! 🚀
