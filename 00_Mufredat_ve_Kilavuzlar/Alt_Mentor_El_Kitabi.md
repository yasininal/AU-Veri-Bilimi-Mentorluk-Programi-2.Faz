# Alt Mentor El Kitabı

Tebrikler! Geçen dönem gösterdiğin performans sayesinde bu dönem **alt mentor** olarak seçildin. Artık 2-3 kişilik bir takımın lideri olacaksın.

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
| Baş mentorla senkronizasyon toplantısına katılmak | Pazartesi | ~20 dk |
| Takım grubunda (WhatsApp/Discord) mentilerin sorularını yanıtlamak | Hafta boyunca | — |
| Hafta ortasında kısa bir kontrol mesajı atmak ("Videolar nasıl gidiyor?") | Çarşamba | 2 dk |
| Mentilerin PR'larını incelemek ve yorum yazmak | Pazar | ~15 dk / menti |
| Takımla haftalık değerlendirme toplantısı yapmak | Pazar | 20-30 dk |
| Takip tablosunda kendi takımının satırlarını güncellemek | Pazar | 5 dk |

**Toplam haftalık yükün:** yaklaşık 1,5-2 saat.

---

## 2. Modül Geçişi ve Mezuniyet

| | Şart |
| :--- | :--- |
| **Modül 1 → Modül 2** | 3 haftanın en az 2'sini tamamlamak **ve** 3. haftadaki mini projeyi teslim etmek |
| **Mezuniyet** | Modül 2'de 3 haftanın en az 2'sini tamamlamak **ve** bitirme projesini teslim etmek |

- Takip tablosu bu şartları **otomatik hesaplar**; sen sadece haftalık durumları doğru girmelisin.
- Modül 1'in sonunda eksiği olan mentiler için **ara hafta** var. Bu haftada onlarla birlikte bir telafi planı yap.
- Geçiş hakkı kazanamayan menti programdan atılmaz; bir sonraki dönemde Modül 1'i tamamlayıp devam edebilir.

---

## 3. Code Review (PR İnceleme) Rehberi

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
- Her PR'a **en az bir yorum** yaz; menti emeğinin görüldüğünü hissetmeli.

### PR Onay Kriteri
- Görev tamamlanmış ve notebook çalışıyorsa → **Approve** et ve tabloda "PR Onaylandı: Evet" yap.
- Eksik varsa → **Request changes** ile eksikleri belirt, menti düzeltince tekrar bak.
- Baş mentor onaylanmış PR'ları ana repoya birleştirir (merge).

---

## 4. Takım Toplantısı Akışı (20-30 dk)

1. **Tur (5 dk):** Herkes bu hafta ne yaptığını ve nerede zorlandığını kısaca anlatır.
2. **Kod incelemesi (10-15 dk):** Bir mentinin ekranını paylaşıp ödevini birlikte gözden geçirin. Her hafta farklı bir menti.
3. **Kontrol sorusu (5 dk):** Modül kılavuzundaki haftanın kontrol sorusunu takımla tartışın.
4. **Gelecek hafta (2 dk):** Yeni haftanın konusunu ve teslim tarihini hatırlat.

---

## 5. Takip Tablosu Kullanımı

Tabloda iki ayrı takip sayfası var: **Modül 1 Takip** ve **Modül 2 Takip**. Her hafta mentilerin için şu sütunları güncelle:

- **Durum:** 🟢 Tamamlandı / 🟡 Devam Ediyor / 🔴 Başlamadı
- **PR Onaylandı:** Evet / Hayır
- **Toplantıya Katıldı:** Evet / Hayır
- **Mentor Notu:** Kısa bir gözlem (örn. "Pandas'ta zorlanıyor, ek kaynak gönderdim")

Modül 2 sayfasında Modül 2'ye geçiş hakkı olmayan mentilerin satırları **gri** görünür; bu satırları doldurmana gerek yok.

---

## 6. Erken Uyarı ve Kopma Riskine Karşı

Modüller kısa olduğu için **bir haftayı kaçıran mentiyi hemen yakalamak** kritik.

- Menti **Cumartesi** teslim etmediyse Pazar günü kibar ve kısa bir mesaj at.
- **2 hafta üst üste** teslim yoksa durumu **baş mentora** bildir.
- Zorlanan mentiye ödevi yarıya düşürmeyi önerebilirsin; tamamen kopmasından iyidir.

---

## 7. Ne Zaman Baş Mentora Danışmalısın?

- Cevabını bilmediğin teknik bir soru geldiğinde (bilmemek normal! "Araştırıp döneceğim" demek yeterli.)
- Bir menti iletişimi tamamen kestiğinde
- Takımda motivasyon ya da iletişim sorunu olduğunda

Başarılar, takım lideri! 🚀
