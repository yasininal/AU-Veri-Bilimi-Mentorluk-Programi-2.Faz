# Alt Mentor El Kitabı

Tebrikler! Geçen dönem gösterdiğin performans sayesinde bu dönem **alt mentor** olarak seçildin. Artık 4 kişilik bir takımın lideri olacaksın.

> [!NOTE]
> Bir konuyu gerçekten öğrenmenin en iyi yolu onu başkasına anlatmaktır. Mentilerinin kodunu incelerken geçen dönem öğrendiklerini çok daha derinden kavrayacaksın.

Program iki modülden oluşur:
- **Modül 1 — Python ve Veri Analizi** (3 hafta)
- **Modül 2 — Makine Öğrenmesi Temelleri** (3 hafta)

Modül 1'i bitiren menti Modül 2'ye geçmeye hak kazanır. Takımını bu geçişe hazırlamak senin en önemli görevin.

---

## 1. Sorumlulukların

| Ne? | Ne Zaman? | Süre |
| :--- | :--- | :--- |
| Baş mentorla **mentor toplantısına** katılmak | Her modülün başında | ~30 dk |
| Kendi takımınla **takım toplantısı** yapmak | Her modülün başında | ~30 dk |
| Takım grubunda (WhatsApp/Discord) mentilerin sorularını yanıtlamak | Hafta boyunca | — |
| Hafta ortasında kısa bir kontrol mesajı atmak ("Videolar nasıl gidiyor?") | Çarşamba | 2 dk |
| Mentilerin PR'larını incelemek | Pazartesi – Salı (Pazar teslimden sonra) | ~15 dk / menti |
| Takip tablosunda kendi takımının satırlarını güncellemek | PR incelemesinden sonra | 5 dk |

**Toplam haftalık yükün:** yaklaşık 1 saat (modül başı haftalarında toplantılarla birlikte biraz daha fazla).

---

## 2. Toplantılar (Sadece Modül Başlarında)

Toplantılar her hafta tekrarlanmaz. Her modülün başında şu üç toplantı yapılır:

| Toplantı | Katılımcılar | Senin Rolün |
| :--- | :--- | :--- |
| **Mentor Toplantısı** | Baş Mentor + Alt Mentorlar | Modülün içeriğini ve görevleri öğrenmek, sorularını sormak |
| **Genel Açılış Toplantısı** | Baş Mentor + Tüm Mentiler | Katılman önerilir; mentilerin seni tanıması için iyi bir fırsat |
| **Takım Toplantısı** | Sen + Kendi Mentilerin | Toplantıyı sen yönetirsin (aşağıdaki akış) |

### Takım Toplantısı Akışı (~30 dk)
1. **Tanışma (5-10 dk):** Herkes kendini ve programdan beklentisini kısaca anlatır.
2. **Modülün tanıtımı (10 dk):** 3 haftanın konuları, görevler ve **Pazar 23:59** teslim tarihi.
3. **İletişim düzeni (5 dk):** Soruların nereye ve nasıl sorulacağı, ne kadar sürede dönüş yapacağın.
4. **Soru-cevap (5-10 dk):** Kurulum veya GitHub ile ilgili takılan yerler.

---

## 3. Modül Geçişi ve Mezuniyet

| | Şart |
| :--- | :--- |
| **Modül 1 → Modül 2** | Modül 1'in **3 haftasının tamamını** tamamlamak (3. haftadaki mini proje dahil) |
| **Mezuniyet** | Modül 2'nin **3 haftasının tamamını** tamamlamak (3. haftadaki bitirme projesi dahil) |

- Takip tablosu bu şartları **otomatik hesaplar**; sen sadece haftalık durumları doğru girmelisin.
- Modül 1'in sonunda eksiği olan mentiler için **ara hafta** var. Bu haftada onlarla birlikte bir telafi planı yap.
- Geçiş hakkı kazanamayan menti programdan atılmaz; bir sonraki dönemde Modül 1'i tamamlayıp devam edebilir.

---

## 4. Code Review (PR İnceleme) Rehberi

Her PR'da şu 4 soruyu sor:

1. **Çalışıyor mu?** Notebook baştan sona hatasız çalışıyor mu?
2. **Görev tamamlanmış mı?** Haftalık görevdeki tüm maddeler yapılmış mı?
3. **Anlaşılır mı?** Değişken isimleri anlamlı mı, gerekli yerlerde açıklama (markdown hücresi) var mı?
4. **Yorumlanmış mı?** Grafik ve sonuçların altında menti kendi yorumunu yazmış mı? (Sadece kod değil, *düşünce* de görmek istiyoruz.)

### Geri Bildirim Verirken
- **Önce olumlu bir şey söyle**, sonra geliştirme önerisi ver.
- Çözümü doğrudan yazma; **ipucu ver veya soru sor.**
  - ❌ "Burada `fillna(df.mean())` kullanmalısın."
  - ✅ "Bu sütundaki eksik değerleri silmek yerine doldurmayı düşündün mü? Hangi değerle doldurmak mantıklı olur?"

### PR Onay Kriteri
- Görev tamamlanmış ve notebook çalışıyorsa → **Approve** et ve tabloda "PR Onaylandı: Evet" yap.
- Eksik varsa → **Request changes** ile eksikleri belirt, menti düzeltince tekrar bak.
- Baş mentor onaylanmış PR'ları ana repoya birleştirir (merge).

---

## 5. Takip Tablosu Kullanımı

Takip tablosuna online olarak aşağıdaki bağlantıdan erişebilirsiniz:  
👉 **[Canlı Mentorluk Takip Tablosu (Google Sheets)](https://docs.google.com/spreadsheets/d/1F3KPS0Rb9KHA1f6yniS3lq6TCSWQpe-p/edit?usp=sharing&ouid=116002235258411028119&rtpof=true&sd=true)**

Tabloda iki ayrı takip sayfası var: **Modül 1 Takip** ve **Modül 2 Takip**. Her hafta mentilerin için şu sütunları güncelle:

- **Durum:** 🟢 Tamamlandı / 🟡 Devam Ediyor / 🔴 Başlamadı
- **PR Onaylandı:** Evet / Hayır
- **Mentor Notu:** Kısa bir gözlem (örn. "Pandas'ta zorlanıyor, ek kaynak gönderdim")

Modül 2 sayfasında Modül 2'ye geçiş hakkı olmayan mentilerin satırları **gri** görünür; bu satırları doldurmana gerek yok.

---

## 6. Erken Uyarı ve Kopma Riskine Karşı

Modüller kısa ve geçiş için **3 haftanın tamamı** gerektiği için bir haftayı kaçıran mentiyi hemen yakalamak kritik.

- Menti **Pazar 23:59**'a kadar teslim etmediyse Pazartesi günü kibar ve kısa bir mesaj at.
- **2 hafta üst üste** teslim yoksa durumu **baş mentora** bildir.
- Zorlanan mentiye ödevi yarıya düşürmeyi önerebilirsin; tamamen kopmasından iyidir.

---

## 7. Ne Zaman Baş Mentora Danışmalısın?

- Cevabını bilmediğin teknik bir soru geldiğinde (bilmemek normal! "Araştırıp döneceğim" demek yeterli.)
- Bir menti iletişimi tamamen kestiğinde
- Takımda motivasyon ya da iletişim sorunu olduğunda

Başarılar, takım lideri! 🚀
