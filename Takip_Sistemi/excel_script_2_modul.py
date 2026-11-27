"""
2 Modüllü Veri Bilimi Mentorluk - Takım Bazlı Takip Excel'i Üretici
  Modül 1: Python ve Veri Analizi (3 hafta)
  Modül 2: Makine Öğrenmesi Temelleri (3 hafta)
  Modül 1'i geçen menti Modül 2'ye geçiş hakkı kazanır.

Kullanım:
    1. Aşağıdaki TAKIMLAR sözlüğünü gerçek mentor ve menti isimleriyle güncelle.
    2. python excel_script_2_modul.py
    3. Script hem Excel dosyasını hem de 01_Takimlar altındaki klasör yapısını oluşturur.
"""
import os
import pandas as pd

# =====================================================================
# 1. TAKIM AYARLARI  (Sadece burayı düzenlemen yeterli)
#    Anahtar: Mentor adı  |  Değer: O mentora atanan mentiler
# =====================================================================
TAKIMLAR = {
    "Fatma Nur": [
        "Hatice Yıldız",
        "Irmak Turhan",
        "Narin Ece Barut",
        "Nevin Selin Alpay",
    ],
    "Bilgehan": [
        "Serra Seçkin",
        "Ebru Alptekin",
        "Azra Abak",
        "Kıvanç Çelik",
    ],
    "Ali Kemal": [
        "Hamza Demir",
        "Nazif Kılıç",
        "Mustafa Zahid Beşibirlik",
        "Asım Efe Dağ",
    ],
    "Demirhan": [
        "Batuhan Dursun",
        "Yiğit Alperen Bekiroğlu",
        "Zeynep Ayabaktı",
    ],
    "Yasin": [
        "Recep Pişgin",
        "Duru Kaygusuz",
    ],
}

HAFTA_SAYISI = 3         # Her modüldeki hafta sayısı
GECIS_MIN_HAFTA = 3      # Modül 1 -> Modül 2 geçişi: 3 haftanın tamamı (mini proje dahil)
MEZUNIYET_MIN_HAFTA = 3  # Mezuniyet: Modül 2'nin 3 haftasının tamamı (bitirme projesi dahil)
DOSYA_ADI = "Mentorluk_Takip_2_Modul.xlsx"
KLASORLERI_OLUSTUR = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(BASE_DIR)
SON_HAFTA = f"Hafta {HAFTA_SAYISI}"
TAMAM = "🟢 Tamamlandı"

# =====================================================================
# 2. MÜFREDAT
# =====================================================================
program = pd.DataFrame([
    ["Modül 1", "Hafta 1", "Atıl S.", "Python Temelleri & GitHub",
     "Kurulum, Jupyter, Veri Tipleri, Listeler, Sözlükler, If, Döngüler, Fonksiyonlar",
     "Öğrenci listesini filtreleyen fonksiyon + ilk PR"],
    ["Modül 1", "Hafta 2", "Atıl S.", "NumPy & Pandas",
     "NumPy'a kısa giriş, Series/DataFrame, Filtreleme, Eksik Veriler, GroupBy",
     "Titanic verisini temizleme + 1 GroupBy analizi"],
    ["Modül 1", "Hafta 3", "Atıl S.", "Görselleştirme & Mini Proje",
     "Matplotlib: çizgi, bar, scatter, histogram",
     "ZORUNLU mini proje: 3 yorumlu grafik + kısa özet"],
    ["—", "Ara Hafta", "—", "Telafi (Opsiyonel)",
     "Modül 1'de eksiği olanlar için telafi haftası",
     "Eksik ödevleri tamamlayıp Modül 2 geçiş hakkı kazanmak"],
    ["Modül 2", "Hafta 1", "Şadi E. Ş.", "ML'e Giriş & Doğrusal Regresyon",
     "Bölüm 2, 3, 4: Problem Tipleri, Basit ve Çoklu Doğrusal Regresyon",
     "Train/test ayrımı + Doğrusal Regresyon + R² skoru"],
    ["Modül 2", "Hafta 2", "Şadi E. Ş.", "Sınıflandırma & Değerlendirme",
     "Bölüm 10, 11, 19: Sınıflandırmaya Giriş, Lojistik Regresyon, Değerlendirme",
     "Titanic Lojistik Regresyon + Accuracy & Confusion Matrix yorumu"],
    ["Modül 2", "Hafta 3", "Şadi E. Ş.", "Karar Ağacı, RF & Bitirme",
     "Bölüm 16, 17: Karar Ağacı ve Random Forest ile Sınıflandırma",
     "ZORUNLU bitirme projesi: LogReg vs Random Forest + Demo günü"],
], columns=["Modül", "Hafta", "Kaynak", "Başlık", "İzlenecek Konular", "Görev / Checkpoint"])
program["Teslim"] = ["Pazar 23:59"] * 3 + ["Ara hafta sonu"] + ["Pazar 23:59"] * 3

# =====================================================================
# 3. EXCEL BİÇİMLERİ
# =====================================================================
cikti = os.path.join(BASE_DIR, DOSYA_ADI)
writer = pd.ExcelWriter(cikti, engine="xlsxwriter")
wb = writer.book

header = wb.add_format({"bold": True, "text_wrap": False, "valign": "vcenter", "align": "center",
                        "bg_color": "#1F4E78", "font_color": "white", "border": 1})
cell = wb.add_format({"text_wrap": False, "valign": "vcenter", "border": 1})
center = wb.add_format({"text_wrap": False, "valign": "vcenter", "align": "center", "border": 1})
cell_end = wb.add_format({"text_wrap": False, "valign": "vcenter", "border": 1,
                          "bottom": 5, "bottom_color": "#1F4E78"})
center_end = wb.add_format({"text_wrap": False, "valign": "vcenter", "align": "center", "border": 1,
                            "bottom": 5, "bottom_color": "#1F4E78"})
pct = wb.add_format({"num_format": "0%", "align": "center", "valign": "vcenter", "border": 1})
pct_end = wb.add_format({"num_format": "0%", "align": "center", "valign": "vcenter", "border": 1,
                         "bottom": 5, "bottom_color": "#1F4E78"})
title = wb.add_format({"bold": True, "font_size": 14, "align": "center", "valign": "vcenter",
                       "border": 1, "bg_color": "#DDEBF7"})
green = wb.add_format({"bg_color": "#C6EFCE", "font_color": "#006100"})
yellow = wb.add_format({"bg_color": "#FFEB9C", "font_color": "#9C5700"})
red = wb.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006"})
blue = wb.add_format({"bg_color": "#DDEBF7", "font_color": "#1F4E78"})
grey = wb.add_format({"bg_color": "#E7E6E6", "font_color": "#7F7F7F"})


def renklendir(ws, r1, c1, r2, c2, kurallar):
    for deger, fmt in kurallar:
        ws.conditional_format(r1, c1, r2, c2, {"type": "cell", "criteria": "==",
                                               "value": f'"{deger}"', "format": fmt})


def basliklari_yaz(ws, row, basliklar, genislikler):
    for c, (v, w) in enumerate(zip(basliklar, genislikler)):
        ws.write(row, c, v, header)
        ws.set_column(c, c, w)


# =====================================================================
# 4. SAYFA: Program
# =====================================================================
program.to_excel(writer, sheet_name="Program", index=False)
ws = writer.sheets["Program"]
for i, w in enumerate([10, 11, 12, 30, 55, 50, 16]):
    ws.set_column(i, i, w, cell if i in (3, 4, 5) else center)
for c, v in enumerate(program.columns):
    ws.write(0, c, v, header)
for r in range(1, len(program) + 1):
    ws.set_row(r, 45)
renklendir(ws, 1, 0, len(program), 0, [("Modül 1", green), ("Modül 2", blue)])
ws.freeze_panes(1, 0)

# =====================================================================
# 5. SAYFALAR: Modül 1 Takip / Modül 2 Takip
#    Sütunlar: A Takım | B Alt Mentor | C Menti | D Hafta | E Durum
#              F PR Onaylandı | G Mentor Notu | (H Modül 2 Hakkı)
# =====================================================================
satirlar = []
for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
    for menti in mentiler:
        for h in range(1, HAFTA_SAYISI + 1):
            satirlar.append([f"Takim_{t_no:02d}", mentor, menti, f"Hafta {h}",
                             "🔴 Başlamadı", "Hayır", ""])
kolonlar = ["Takım", "Alt Mentor", "Menti", "Hafta", "Durum", "PR Onaylandı", "Mentor Notu"]
N = len(satirlar)


def aralik(sayfa, col):
    return f"'{sayfa}'!${col}$2:${col}${N + 1}"


M1 = {k: aralik("Modül 1 Takip", c) for k, c in zip(["takim", "menti", "hafta", "durum"], "ACDE")}
M2 = {k: aralik("Modül 2 Takip", c) for k, c in zip(["takim", "menti", "hafta", "durum"], "ACDE")}


def gecis_formulu(menti_hucre):
    return (f'IF(AND(COUNTIFS({M1["menti"]},{menti_hucre},{M1["durum"]},"{TAMAM}")>={GECIS_MIN_HAFTA},'
            f'COUNTIFS({M1["menti"]},{menti_hucre},{M1["hafta"]},"{SON_HAFTA}",{M1["durum"]},"{TAMAM}")>0),'
            f'"✅ Var","🔒 Yok")')


mentor_bitis_satirlari = set()
current_row = 0
for mentor, mentiler in TAKIMLAR.items():
    current_row += len(mentiler) * HAFTA_SAYISI
    mentor_bitis_satirlari.add(current_row)

for sayfa, modul2 in (("Modül 1 Takip", False), ("Modül 2 Takip", True)):
    ws = wb.add_worksheet(sayfa)
    ws.set_default_row(22)
    ws.set_row(0, 26)

    genislikler = [14, 16, 28, 12, 18, 16, 30]
    for i, w in enumerate(genislikler):
        ws.set_column(i, i, w)
    for c, v in enumerate(kolonlar):
        ws.write(0, c, v, header)

    for r, satir in enumerate(satirlar, start=1):
        is_end = (r in mentor_bitis_satirlari)
        f_center = center_end if is_end else center
        f_cell = cell_end if is_end else cell
        ws.set_row(r, 22)
        for c, val in enumerate(satir):
            ws.write(r, c, val, f_cell if c == 6 else f_center)

    son_kolon = 6
    if modul2:
        ws.write(0, 7, "Modül 2 Hakkı", header)
        ws.set_column(7, 7, 16)
        for r in range(1, N + 1):
            is_end = (r in mentor_bitis_satirlari)
            f_center = center_end if is_end else center
            ws.write_formula(r, 7, "=" + gecis_formulu(f"$C{r + 1}"), f_center)
        # Geçiş hakkı olmayan mentilerin satırları gri (ilk eklenen kural öncelikli)
        ws.conditional_format(1, 0, N, 6, {"type": "formula", "criteria": '=$H2="🔒 Yok"', "format": grey})
        renklendir(ws, 1, 7, N, 7, [("✅ Var", green), ("🔒 Yok", grey)])
        son_kolon = 7

    ws.data_validation(1, 4, N, 4, {"validate": "list", "source": [TAMAM, "🟡 Devam Ediyor", "🔴 Başlamadı"]})
    renklendir(ws, 1, 4, N, 4, [(TAMAM, green), ("🟡 Devam Ediyor", yellow), ("🔴 Başlamadı", red)])
    ws.data_validation(1, 5, N, 5, {"validate": "list", "source": ["Evet", "Hayır"]})
    renklendir(ws, 1, 5, N, 5, [("Evet", green), ("Hayır", red)])
    ws.autofilter(0, 0, N, son_kolon)  # Mentorlar kendi takımını filtreleyebilir
    ws.freeze_panes(1, 4)

# =====================================================================
# 6. SAYFA: Menti Özeti
#    A Takım | B Mentor | C Menti | D M1 Tamamlanan | E M1 Mini Proje | F Modül 2 Hakkı
#    G M2 Tamamlanan | H M2 Bitirme Projesi | I Genel Durum
# =====================================================================
ws = wb.add_worksheet("Menti Özeti")
ws.set_default_row(22)
ws.set_row(0, 30)
ws.set_row(1, 26)
ws.merge_range(0, 0, 0, 8, "AKDENİZ ÜNİVERSİTESİ - VERİ BİLİMİ MENTORLUK / MENTİ ÖZETİ", title)

basliklar = ["Takım", "Alt Mentor", "Menti", f"M1 Tamamlanan (/{HAFTA_SAYISI})", "M1 Mini Proje",
             "Modül 2 Hakkı", f"M2 Tamamlanan (/{HAFTA_SAYISI})", "M2 Bitirme Projesi", "Genel Durum"]
genislikler_ozet = [14, 16, 28, 18, 16, 16, 18, 18, 18]
for c, (v, w) in enumerate(zip(basliklar, genislikler_ozet)):
    ws.write(1, c, v, header)
    ws.set_column(c, c, w)


def proje_formulu(m, menti_hucre):
    return (f'=IF(COUNTIFS({m["menti"]},{menti_hucre},{m["hafta"]},"{SON_HAFTA}",{m["durum"]},"{TAMAM}")>0,'
            f'"Evet","Hayır")')


menti_ozet_mentor_bitis = set()
curr = 1
for mentor, mentiler in TAKIMLAR.items():
    curr += len(mentiler)
    menti_ozet_mentor_bitis.add(curr)

r = 2
for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
    for menti in mentiler:
        x = r + 1
        is_end = (r in menti_ozet_mentor_bitis)
        f_c = center_end if is_end else center
        f_p = pct_end if is_end else pct
        ws.set_row(r, 22)
        ws.write(r, 0, f"Takim_{t_no:02d}", f_c)
        ws.write(r, 1, mentor, f_c)
        ws.write(r, 2, menti, f_c)
        ws.write_formula(r, 3, f'=COUNTIFS({M1["menti"]},C{x},{M1["durum"]},"{TAMAM}")', f_c)
        ws.write_formula(r, 4, proje_formulu(M1, f"C{x}"), f_c)
        ws.write_formula(r, 5, "=" + gecis_formulu(f"C{x}"), f_c)
        ws.write_formula(r, 6, f'=COUNTIFS({M2["menti"]},C{x},{M2["durum"]},"{TAMAM}")', f_c)
        ws.write_formula(r, 7, proje_formulu(M2, f"C{x}"), f_c)
        ws.write_formula(r, 8, f'=IF(F{x}="✅ Var",IF(AND(G{x}>={MEZUNIYET_MIN_HAFTA},H{x}="Evet"),'
                               f'"🎓 Mezun","📘 Modül 2\'de"),"📗 Modül 1\'de")', f_c)
        r += 1
son = r - 1
renklendir(ws, 2, 4, son, 4, [("Evet", green), ("Hayır", red)])
renklendir(ws, 2, 7, son, 7, [("Evet", green), ("Hayır", red)])
renklendir(ws, 2, 5, son, 5, [("✅ Var", green), ("🔒 Yok", grey)])
renklendir(ws, 2, 8, son, 8, [("🎓 Mezun", green), ("📘 Modül 2'de", blue), ("📗 Modül 1'de", yellow)])
ws.freeze_panes(2, 3)

# =====================================================================
# 7. SAYFA: Takım Özeti (Baş Mentor paneli)
# =====================================================================
ws = wb.add_worksheet("Takım Özeti")
ws.set_default_row(22)
ws.set_row(0, 30)
ws.set_row(1, 26)
ws.merge_range(0, 0, 0, 6, "TAKIM ÖZETİ - BAŞ MENTOR PANELİ", title)

basliklar_takim = ["Takım", "Alt Mentor", "Menti Sayısı", "Modül 1 İlerlemesi",
                   "Modül 2'ye Geçen", "Modül 2 İlerlemesi", "Mezun"]
genislikler_takim = [14, 16, 14, 18, 18, 18, 14]
for c, (v, w) in enumerate(zip(basliklar_takim, genislikler_takim)):
    ws.write(1, c, v, header)
    ws.set_column(c, c, w)

MO = "'Menti Özeti'"
MO_TAKIM, MO_HAK, MO_DURUM = (f"{MO}!${c}$3:${c}${son + 1}" for c in "AFI")

r = 2
for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
    x = r + 1
    ws.set_row(r, 22)
    ws.write(r, 0, f"Takim_{t_no:02d}", center)
    ws.write(r, 1, mentor, center)
    ws.write(r, 2, len(mentiler), center)
    ws.write_formula(r, 3, f'=COUNTIFS({M1["takim"]},A{x},{M1["durum"]},"{TAMAM}")/(C{x}*{HAFTA_SAYISI})', pct)
    ws.write_formula(r, 4, f'=COUNTIFS({MO_TAKIM},A{x},{MO_HAK},"✅ Var")', center)
    ws.write_formula(r, 5, f'=IFERROR(COUNTIFS({M2["takim"]},A{x},{M2["durum"]},"{TAMAM}")/(E{x}*{HAFTA_SAYISI}),0)', pct)
    ws.write_formula(r, 6, f'=COUNTIFS({MO_TAKIM},A{x},{MO_DURUM},"🎓 Mezun")', center)
    r += 1

x = r + 1
ws.set_row(r, 24)
pct_toplam = wb.add_format({"num_format": "0%", "bold": True, "align": "center",
                            "bg_color": "#1F4E78", "font_color": "white", "border": 1})
ws.write(r, 0, "TOPLAM", header)
ws.write(r, 1, "", header)
ws.write_formula(r, 2, f"=SUM(C3:C{r})", header)
ws.write_formula(r, 3, f'=COUNTIFS({M1["durum"]},"{TAMAM}")/(C{x}*{HAFTA_SAYISI})', pct_toplam)
ws.write_formula(r, 4, f"=SUM(E3:E{r})", header)
ws.write_formula(r, 5, f'=IFERROR(COUNTIFS({M2["durum"]},"{TAMAM}")/(E{x}*{HAFTA_SAYISI}),0)', pct_toplam)
ws.write_formula(r, 6, f"=SUM(G3:G{r})", header)
for col in (3, 5):
    ws.conditional_format(2, col, r - 1, col, {"type": "data_bar", "bar_color": "#63BE7B",
                                               "min_type": "num", "min_value": 0, "max_type": "num", "max_value": 1})

writer.close()
print(f"✅ {cikti} oluşturuldu ({len(TAKIMLAR)} takım, {sum(map(len, TAKIMLAR.values()))} menti).")

# =====================================================================
# 8. KLASÖR YAPISI (01_Takimlar/Takim_XX_Mentor/Menti/modulX/haftaX)
# =====================================================================
if KLASORLERI_OLUSTUR:
    for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
        mentor_klasor = mentor.replace(' ', '_')
        for menti in mentiler:
            menti_klasor = menti.replace(' ', '_')
            for m in (1, 2):
                for h in range(1, HAFTA_SAYISI + 1):
                    yol = os.path.join(REPO_DIR, "01_Takimlar", f"Takim_{t_no:02d}_{mentor_klasor}",
                                       menti_klasor, f"modul{m}", f"hafta{h}")
                    os.makedirs(yol, exist_ok=True)
                    gk = os.path.join(yol, ".gitkeep")
                    if not os.path.exists(gk):
                        open(gk, "w").close()
    print("✅ 01_Takimlar klasör yapısı oluşturuldu.")
