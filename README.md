# AU Veri Bilimi Mentorluk Programı — 5 Haftalık Takım Sistemi

Bu depo, Veri Bilimi topluluğumuzun **5 haftalık uçtan uca "Python, Veri Analizi ve Makine Öğrenmesi"** mentorluk programının tüm kaynaklarını, müfredatını ve ödevlerini barındırır.

## Sistem Nasıl İşliyor? (Birbirini Besleyen Model)

```
Baş Mentor (Koordinatör)
   └── Alt Mentorlar (geçen dönemin başarılı katılımcıları)
          └── Her alt mentora 2-3 menti
```

- **Baş Mentor:** Programı ve müfredatı yönetir, haftalık olarak alt mentorlarla senkronizasyon toplantısı yapar, PR'ları son kez kontrol edip birleştirir.
- **Alt Mentor:** Kendi 2-3 mentisiyle iletişimde kalır, PR'larını inceler (code review) ve takip tablosunu günceller.
- **Menti:** Haftalık videoları izler, ödevini yapar ve PR açar.

Bu dönemi başarıyla tamamlayan mentiler, **bir sonraki dönem alt mentor** olma ve **proje ekibinde** yer alma hakkı kazanır. Sistem her dönem kendini büyütür.

## Proje Yapısı

- `00_Mufredat_ve_Kilavuzlar/`
  - `5_Haftalik_Mufredat_Kilavuzu.md`: Haftalık konular, kaynaklar ve görevler (mentiler için).
  - `Alt_Mentor_El_Kitabi.md`: Alt mentorların sorumlulukları, code review rehberi.
  - `Github_Takim_Kullanimi.md`: Fork, PR açma ve PR inceleme adımları.
- `01_Takimlar/`: Her takımın klasörü. Yapı: `Takim_XX_MentorAdi/MentiAdi/haftaX/`
- `Takip_Sistemi/`: Takip Excel'ini üreten script ve Excel dosyası.

## Haftalık Ritim

| Gün | Ne Oluyor? |
| :--- | :--- |
| Pazartesi | Baş Mentor + Alt Mentorlar senkronizasyon toplantısı (20 dk) |
| Pazartesi – Cumartesi | Mentiler videoları izler ve ödevini yapar, takıldığında önce kendi alt mentoruna sorar |
| **Cumartesi 23:59** | Haftalık ödevin son PR teslim saati |
| Pazar | Alt mentor PR'ları inceler, takımıyla 20-30 dk toplantı yapar, tabloyu günceller |

## Mezuniyet Kriterleri

- 5 haftalık ödevden **en az 4'ünü** zamanında teslim etmek
- **5. hafta bitirme projesini** (zorunlu) teslim etmek
- Takım toplantılarının çoğuna katılmak
