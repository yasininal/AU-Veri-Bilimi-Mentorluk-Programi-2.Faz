# GitHub Kullanım Kılavuzu (Takım Sistemi) 🚀

Bu kılavuz, ödevlerinizi teslim etmeniz (**mentiler**) ve PR incelemeniz (**alt mentorlar**) için gereken temel GitHub adımlarını içerir.

---

## Bölüm A — Mentiler İçin

### 1. İlk Kurulum (Bir Kez)

Git'i kurduktan sonra terminalde (veya Git Bash'te):

```bash
git config --global user.name "Adınız Soyadınız"
git config --global user.email "eposta@ornek.com"
```

### 2. Repoyu Fork'lamak ve İndirmek

1. Program reposunun ana sayfasında **"Fork"** butonuna basın.
2. Kendi kopyanızda yeşil **"Code"** butonundan linki kopyalayın:

```bash
git clone https://github.com/kullanici-adiniz/AU-Veri-Bilimi-Mentorluk-Programi-2.Faz.git
cd AU-Veri-Bilimi-Mentorluk-Programi-2.Faz
```

### 3. Haftalık Teslim

**Adım 1 — Dosyanızı doğru klasöre koyun:**

```
01_Takimlar/Takim_XX_MentorAdi/AdinizSoyadiniz/hafta1/odev1.ipynb
```

**Adım 2 — Kaydedin ve gönderin:**

```bash
git add .
git commit -m "Hafta 1: Ad Soyad"
git push origin main
```

**Adım 3 — Pull Request açın:**
1. GitHub'daki kendi fork sayfanıza gidin.
2. **"Contribute" → "Open Pull Request"** butonuna basın.
3. Başlık: `[Takim_XX] Hafta 1 - Ad Soyad`
4. Açıklamaya kısaca ne yaptığınızı ve zorlandığınız yeri yazın.

### 4. Mentorunuz Değişiklik İsterse

Dosyanızı düzeltip aynı şekilde `add → commit → push` yapın. **Yeni PR açmanıza gerek yok**, mevcut PR otomatik güncellenir.

> [!IMPORTANT]
> Sadece kendi klasörünüzdeki dosyaları değiştirin. Başka klasörlerdeki dosyalara dokunmayın.

### 5. Fork'unuzu Güncel Tutmak

Ana repoda değişiklik olduysa GitHub'daki fork sayfanızda **"Sync fork" → "Update branch"** butonuna basın, sonra:

```bash
git pull origin main
```

---

## Bölüm B — Alt Mentorlar İçin

### PR İnceleme Adımları

1. Ana repoda **"Pull requests"** sekmesine gidin.
2. Başlığında kendi takım numaranız (`[Takim_XX]`) olan PR'ları açın.
3. **"Files changed"** sekmesinde notebook'u inceleyin.
   - Notebook'u daha rahat görmek için dosyayı indirip kendi bilgisayarınızda çalıştırabilir veya Colab'da açabilirsiniz.
4. Satıra yorum eklemek için satırın yanındaki **"+"** işaretine tıklayın.
5. Sağ üstteki **"Review changes"** butonundan:
   - **Comment:** Sadece yorum
   - **Approve:** Ödev tamam
   - **Request changes:** Düzeltme gerekiyor
6. Onayladığınız PR'ları takip tablosunda işaretleyin. Birleştirme (merge) işlemini baş mentor yapar.

Anlamadığınız bir yer olursa önce takım grubunuza yazın. Başarılar!
