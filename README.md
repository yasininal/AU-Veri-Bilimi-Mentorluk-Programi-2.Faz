# AU Veri Bilimi Mentorluk Programı — 2. Faz (2 Modüllü Takım Sistemi)

Bu repo, Veri Bilimi topluluğumuzun **iki modüllü** mentorluk programının tüm kaynaklarını, müfredatını ve ödevlerini barındırır.

| Modül | Süre | Konu | Kaynak (BTK Akademi) |
| :--- | :--- | :--- | :--- |
| **Modül 1** | 3 hafta | Python ve Veri Analizi | Atıl Samancıoğlu — *Veri Bilimi için Python* |
| **Modül 2** | 3 hafta | Makine Öğrenmesi Temelleri | Şadi Evren Şeker — *Python ile Makine Öğrenmesi* |

> **Modül 1'i başarıyla bitiren menti, Modül 2'ye (Makine Öğrenmesi) geçmeye hak kazanır.**
> Haftalar bilerek hafif tutuldu: haftada yaklaşık **3-5 saat** ayırmak yeterli.

## Sistem Nasıl İşliyor? (Birbirini Besleyen Model)

```
Baş Mentor (Koordinatör)
   └── Alt Mentorlar (geçen dönemin başarılı katılımcıları)
          └── Her alt mentora 2-3 menti
```

- **Baş Mentor:** Programı ve müfredatı yönetir, haftalık olarak alt mentorlarla senkronizasyon toplantısı yapar, PR'ları son kez kontrol edip birleştirir.
- **Alt Mentor:** Kendi 2-3 mentisiyle iletişimde kalır, PR'larını inceler (code review) ve takip tablosunu günceller.
- **Menti:** Haftalık videoları izler, ödevini yapar ve PR açar.

Programı tamamlayan mentiler, **bir sonraki dönem alt mentor** olma ve **proje ekibinde** yer alma hakkı kazanır. Sistem her dönem kendini büyütür.

## Program Akışı

```
Modül 1 (3 hafta)  →  Ara Hafta (telafi)  →  Modül 2 (3 hafta)  →  Demo Günü & Mezuniyet
```

- **Ara Hafta (opsiyonel):** Modül 1'de eksiği kalanlar bu haftada telafi edip Modül 2'ye geçiş hakkı kazanabilir.

## Geçiş ve Mezuniyet Kriterleri

| | Şart |
| :--- | :--- |
| **Modül 1 → Modül 2 geçişi** | 3 haftanın en az 2'sini tamamlamak **ve** 3. haftadaki mini projeyi (zorunlu) teslim etmek |
| **Program mezuniyeti** | Modül 2'de 3 haftanın en az 2'sini tamamlamak **ve** bitirme projesini (zorunlu) teslim etmek |

## Proje Yapısı

- `00_Mufredat_ve_Kilavuzlar/`
  - `Modul_1_Python_Kilavuzu.md`: Modül 1 haftalık konular ve görevler.
  - `Modul_2_Makine_Ogrenmesi_Kilavuzu.md`: Modül 2 haftalık konular ve görevler.
  - `Alt_Mentor_El_Kitabi.md`: Alt mentorların sorumlulukları, code review rehberi.
  - `Github_Takim_Kullanimi.md`: Fork, PR açma ve PR inceleme adımları.
- `01_Takimlar/`: Her takımın klasörü. Yapı: `Takim_XX_MentorAdi/MentiAdi/modulX/haftaX/`
- `Takip_Sistemi/`: Takip Excel'ini üreten script ve Excel dosyası.

## Haftalık Ritim

| Gün | Ne Oluyor? |
| :--- | :--- |
| Pazartesi | Baş Mentor + Alt Mentorlar senkronizasyon toplantısı (20 dk) |
| Pazartesi – Cumartesi | Mentiler videoları izler ve ödevini yapar, takıldığında önce kendi alt mentoruna sorar |
| **Cumartesi 23:59** | Haftalık ödevin son PR teslim saati |
| Pazar | Alt mentor PR'ları inceler, takımıyla 20-30 dk toplantı yapar, tabloyu günceller |
