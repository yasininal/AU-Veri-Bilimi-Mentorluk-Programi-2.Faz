# AU Veri Bilimi Mentorluk Programı — 2. Faz (2 Modüllü Takım Sistemi)

Bu repo, Veri Bilimi topluluğumuzun **iki modüllü** mentorluk programının tüm kaynaklarını, müfredatını ve ödevlerini barındırır.

| Modül | Süre | Konu | Kaynak (BTK Akademi) |
| :--- | :--- | :--- | :--- |
| **Modül 1** | 3 hafta | Python ve Veri Analizi | Atıl Samancıoğlu — *Veri Bilimi için Python* |
| **Modül 2** | 3 hafta | Makine Öğrenmesi Temelleri | Kaan Can Yılmaz — *Makine Öğrenmesi* |

> **Modül 1'i başarıyla bitiren menti, Modül 2'ye (Makine Öğrenmesi) geçmeye hak kazanır.**
> Haftalar bilerek hafif tutuldu: haftada yaklaşık **3-5 saat** ayırmak yeterli.

## Sistem Nasıl İşliyor? (Birbirini Besleyen Model)

```
Baş Mentor (Koordinatör)
   └── Alt Mentorlar (geçen dönemin başarılı katılımcıları)
          └── Her alt mentora 4 menti
```

- **Baş Mentor:** Programı ve müfredatı yönetir, modül başı toplantılarını yapar, PR'ları son kez kontrol edip birleştirir.
- **Alt Mentor:** Kendi 4 mentisiyle iletişimde kalır, PR'larını inceler (code review) ve takip tablosunu günceller.
- **Menti:** Haftalık videoları izler, ödevini yapar ve PR açar.

Programı tamamlayan mentiler, **bir sonraki dönem alt mentor** olma ve **proje ekibinde** yer alma hakkı kazanır. Sistem her dönem kendini büyütür.

## Takımlar ve Mentor Dağılımı

| Takım | Mentor | Mentiler |
| :--- | :--- | :--- |
| **Takım 1** | Fatma Nur | Hatice Yıldız, Irmak Turhan, Narin Ece Barut, Nevin Selin Alpay |
| **Takım 2** | Bilgehan | Serra Seçkin, Ebru Alptekin, Azra Abak, Kıvanç Çelik |
| **Takım 3** | Ali Kemal | Hamza Demir, Nazif Kılıç, Mustafa Zahid Beşibirlik, Asım Efe Dağ |
| **Takım 4** | Demirhan | Yiğit Alperen Bekiroğlu, Zeynep Ayabaktı |
| **Takım 5** | Yasin (Baş Mentor) | Batuhan Dursun, Recep Pişgin, Duru Kaygusuz |

## Program Akışı

```
Modül 1 (3 hafta)  →  Ara Hafta (telafi)  →  Modül 2 (3 hafta)  →  Demo Günü & Mezuniyet
```

- **Ara Hafta (opsiyonel):** Modül 1'de eksiği kalanlar bu haftada telafi edip Modül 2'ye geçiş hakkı kazanabilir.

## Geçiş ve Mezuniyet Kriterleri

| | Şart |
| :--- | :--- |
| **Modül 1 → Modül 2 geçişi** | Modül 1'in **3 haftasının tamamını** tamamlamak (3. haftadaki mini proje dahil) |
| **Program mezuniyeti** | Modül 2'nin **3 haftasının tamamını** tamamlamak (3. haftadaki bitirme projesi dahil) |

## Toplantılar (Sadece Modül Başlarında)

Toplantılar her hafta tekrarlanmaz; **her modülün başında** bir kez yapılır:

| Toplantı | Katılımcılar | Amaç |
| :--- | :--- | :--- |
| **Mentor Toplantısı** | Baş Mentor + Alt Mentorlar | Modülün içeriği, görevler ve dikkat edilecek noktalar |
| **Genel Açılış Toplantısı** | Baş Mentor + Tüm Mentiler | Modülün tanıtımı, beklentiler ve takvim |
| **Takım Toplantısı** | Alt Mentor + Kendi Mentileri | Takımla tanışma, iletişim düzeni ve soru-cevap |

Bunların dışında iletişim takım gruplarında (WhatsApp/Discord) ve PR yorumları üzerinden yürür.

## Haftalık Ritim

| Gün | Ne Oluyor? |
| :--- | :--- |
| Pazartesi – Pazar | Mentiler videoları izler ve ödevini yapar, takıldığında önce kendi alt mentoruna sorar |
| **Pazar 23:59** | Haftalık ödevin son teslim tarihi (PR) |
| Pazartesi – Salı | Alt mentor teslim edilen PR'ları inceler ve takip tablosunu günceller |

## Proje Yapısı

- `00_Mufredat_ve_Kilavuzlar/`
  - `Modul_1_Python_Kilavuzu.md`: Modül 1 haftalık konular ve görevler.
  - `Modul_2_Makine_Ogrenmesi_Kilavuzu.md`: Modül 2 haftalık konular ve görevler.
  - `Alt_Mentor_El_Kitabi.md`: Alt mentorların sorumlulukları, code review rehberi.
  - `Github_Takim_Kullanimi.md`: Fork, PR açma ve PR inceleme adımları.
- `01_Takimlar/`: Her takımın klasörü. Yapı: `Takim_XX_MentorAdi/MentiAdi/modulX/haftaX/`
- `Takip_Sistemi/`: Takip Excel'ini üreten script ve Excel dosyası.
