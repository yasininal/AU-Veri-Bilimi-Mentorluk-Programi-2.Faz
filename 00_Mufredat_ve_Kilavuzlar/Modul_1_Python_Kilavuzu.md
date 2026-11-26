# Modül 1 — Python ve Veri Analizi (3 Hafta)

Mentorluk programına hoş geldiniz! Bu dönem her biriniz **4 kişilik bir takımda**, size özel bir **alt mentorla** birlikte ilerleyeceksiniz.

- **Kaynak:** BTK Akademi — Atıl Samancıoğlu, *"Veri Bilimi için Python ve Tensorflow"* (ücretsiz)
- **Haftalık yük:** yaklaşık 3-5 saat
- **Teslim:** Her hafta **Pazar 23:59**'a kadar GitHub'a Pull Request (PR)

> [!IMPORTANT]
> **Modül 2'ye (Makine Öğrenmesi) geçiş şartı:** Modül 1'in **3 haftasının tamamını** tamamlamak (3. haftadaki mini proje dahil). Eksiği kalanlar modül sonrasındaki **ara haftada** telafi edebilir.

## Program İşleyişi
1. **Modül başında** baş mentorla genel açılış toplantısı, ardından alt mentorunuzla takım toplantısı yapılır. Toplantılar her hafta tekrarlanmaz.
2. Her hafta belirlenen videoları izleyip kendi bilgisayarınızda (veya Google Colab'da) uygulayın.
3. Ödevinizi **Pazar 23:59**'a kadar PR olarak gönderin.
4. Alt mentorunuz PR'ınızı inceleyip geri bildirim verir.
5. Takıldığınız yerde **önce alt mentorunuza** takım grubunuzdan sorun.

---

## Hafta 1: Python Temelleri ve GitHub
- **İzlenecek Konular:** Anaconda / Jupyter Notebook kurulumu, Değişkenler, Veri Tipleri, Listeler, Sözlükler, If kontrolleri, Döngüler, Fonksiyonlar.
- **Görev (PR #1):**
  - Çalışma ortamını kurun ve programın GitHub reposunu fork'layın.
  - Öğrenci bilgilerini (isim, not, bölüm) içeren bir liste oluşturun; **notu belirli bir değerin üzerindeki öğrencileri döndüren** bir fonksiyon yazın.
  - İlk PR'ınızı açın.
- **Kontrol Sorusu:** Liste ile sözlük arasındaki fark nedir, hangi durumda hangisini kullanırsınız?

## Hafta 2: NumPy ve Pandas ile Veri İşleme
- **İzlenecek Konular:** NumPy'a kısa giriş (diziler), Pandas Series & DataFrame, veri okuma, filtreleme, eksik veriler, GroupBy.
- **Görev (PR #2):**
  - Kaggle'dan bir veri seti indirin (öneri: *Titanic*).
  - Veriyi Pandas ile okuyup `info()` ve `describe()` ile inceleyin.
  - Eksik verileri bulun ve **neden o yöntemi seçtiğinizi açıklayarak** doldurun veya silin.
  - 1 tane `groupby` analizi yapın (örn. cinsiyete göre hayatta kalma oranı).
- **Kontrol Sorusu:** Eksik bir değeri ortalama ile doldurmak ne zaman yanıltıcı olabilir?

## Hafta 3: Veri Görselleştirme ve Modül 1 Mini Projesi
- **İzlenecek Konular:** Matplotlib ile çizgi, bar, scatter ve histogram grafikleri.
- **Mini Proje (PR #3 — Zorunlu):** 2. haftada temizlediğiniz veri setiyle küçük bir analiz notebook'u hazırlayın:
  1. **3 farklı grafik** çizin.
  2. Her grafiğin altına **1-2 cümlelik yorum** yazın.
  3. Notebook'un başına 2-3 cümlelik bir özet ekleyin: *"Bu veride ne buldum?"*
- **Kontrol Sorusu:** Hangi tür veri için bar grafiği, hangisi için histogram uygundur?

---

## Ödev Klasör Yapısı

```
01_Takimlar/Takim_XX_MentorAdi/AdinizSoyadiniz/modul1/haftaX/odevX.ipynb
```

Detaylı adımlar için: [Github_Takim_Kullanimi.md](Github_Takim_Kullanimi.md)

Modül 1'i tamamlayınca sizi [Modül 2 — Makine Öğrenmesi](Modul_2_Makine_Ogrenmesi_Kilavuzu.md) bekliyor! 🚀
