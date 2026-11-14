"""
5 Haftalık Veri Bilimi Mentorluk - Takım Bazlı Takip Excel'i Üretici

Kullanım:
    1. Aşağıdaki TAKIMLAR sözlüğünü gerçek mentor ve menti isimleriyle güncelle.
    2. python excel_script_5_hafta.py
    3. Script hem Excel dosyasını hem de 01_Takimlar altındaki klasör yapısını oluşturur.
"""
import os
import pandas as pd
from xlsxwriter.utility import xl_col_to_name

# =====================================================================
# 1. TAKIM AYARLARI  (Sadece burayı düzenlemen yeterli)
#    Anahtar: Alt mentorun adı  |  Değer: O mentora atanan 2-3 menti
# =====================================================================
TAKIMLAR = {
    "Mentor_1": ["Menti_1A", "Menti_1B", "Menti_1C"],
    "Mentor_2": ["Menti_2A", "Menti_2B", "Menti_2C"],
    "Mentor_3": ["Menti_3A", "Menti_3B"],
    "Mentor_4": ["Menti_4A", "Menti_4B", "Menti_4C"],
    "Mentor_5": ["Menti_5A", "Menti_5B"],
}

HAFTA_SAYISI = 5
MEZUNIYET_MIN_HAFTA = 4  # Mezuniyet için tamamlanması gereken minimum hafta (5. hafta zorunlu)
DOSYA_ADI = "5_Haftalik_Mentorluk_Takip.xlsx"
KLASORLERI_OLUSTUR = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(BASE_DIR)

# =====================================================================
# 2. MÜFREDAT
# =====================================================================
program = pd.DataFrame({
    "Hafta": [f"Hafta {i}" for i in range(1, HAFTA_SAYISI + 1)],
    "Kaynak": ["Atıl S.", "Atıl S.", "Atıl S. + Şadi E. Ş.", "Şadi E. Ş.", "Şadi E. Ş."],
    "Modül Başlığı": [
        "Python Hızlı Başlangıç & GitHub",
        "NumPy & Pandas",
        "EDA, Görselleştirme & Veri Hazırlığı",
        "ML - Tahmin (Regresyon)",
        "Sınıflandırma & Bitirme Projesi",
    ],
    "İzlenecek Konular": [
        "Kurulum, Jupyter, Veri Tipleri, Listeler, Sözlükler, If, Döngüler, Fonksiyonlar",
        "NumPy Dizileri, Pandas Series/DataFrame, Filtreleme, Eksik Veriler, GroupBy",
        "Matplotlib grafikleri, Subplots, Proje Yönetimi & Problem Tipleri, Encoding, Train/Test Split",
        "Basit & Çoklu Doğrusal Regresyon, Karar Ağacı, Random Forest, R² ile Karşılaştırma",
        "Lojistik Regresyon, K-NN, Karar Ağacı & RF Sınıflandırma, Confusion Matrix, Accuracy, Recall",
    ],
    "Görev / Checkpoint": [
        "Öğrenci listesi filtreleme fonksiyonları + ilk PR",
        "Kaggle ham veri setini temizleme + 2 GroupBy analizi",
        "3 yorumlu grafik + encoding + train/test ayrımı",
        "Doğrusal Regresyon vs Random Forest R² karşılaştırması",
        "Uçtan uca sınıflandırma bitirme projesi + Demo günü sunumu",
    ],
    "Teslim": ["Cumartesi 23:59"] * HAFTA_SAYISI,
})

# =====================================================================
# 3. TAKİP VERİSİ (Her menti x her hafta = 1 satır)
# =====================================================================
satirlar = []
for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
    takim = f"Takim_{t_no:02d}"
    for menti in mentiler:
        for h in range(1, HAFTA_SAYISI + 1):
            satirlar.append({
                "Takım": takim,
                "Alt Mentor": mentor,
                "Menti": menti,
                "Hafta": f"Hafta {h}",
                "Durum": "🔴 Başlamadı",
                "PR Onaylandı": "Hayır",
                "Toplantıya Katıldı": "Hayır",
                "Mentor Notu": "",
            })
takip = pd.DataFrame(satirlar)
n_takip = len(takip)

# =====================================================================
# 4. EXCEL
# =====================================================================
cikti = os.path.join(BASE_DIR, DOSYA_ADI)
writer = pd.ExcelWriter(cikti, engine="xlsxwriter")
wb = writer.book

header = wb.add_format({"bold": True, "text_wrap": True, "valign": "vcenter", "align": "center",
                        "bg_color": "#1F4E78", "font_color": "white", "border": 1})
cell = wb.add_format({"text_wrap": True, "valign": "vcenter", "border": 1})
center = wb.add_format({"text_wrap": True, "valign": "vcenter", "align": "center", "border": 1})
pct = wb.add_format({"num_format": "0%", "align": "center", "valign": "vcenter", "border": 1})
title = wb.add_format({"bold": True, "font_size": 14, "align": "center", "valign": "vcenter",
                       "border": 1, "bg_color": "#DDEBF7"})
green = wb.add_format({"bg_color": "#C6EFCE", "font_color": "#006100"})
yellow = wb.add_format({"bg_color": "#FFEB9C", "font_color": "#9C5700"})
red = wb.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006"})


def renklendir(ws, r1, c1, r2, c2, kurallar):
    for deger, fmt in kurallar:
        ws.conditional_format(r1, c1, r2, c2, {"type": "cell", "criteria": "==",
                                               "value": f'"{deger}"', "format": fmt})


# ---- Sayfa 1: Program ----
program.to_excel(writer, sheet_name="Program", index=False)
ws = writer.sheets["Program"]
for i, w in enumerate([10, 18, 30, 55, 45, 16]):
    ws.set_column(i, i, w, center if i in (0, 1, 5) else cell)
for c, v in enumerate(program.columns):
    ws.write(0, c, v, header)
for r in range(1, HAFTA_SAYISI + 1):
    ws.set_row(r, 50)
ws.freeze_panes(1, 0)

# ---- Sayfa 2: Haftalık Takip ----
takip.to_excel(writer, sheet_name="Haftalık Takip", index=False)
ws = writer.sheets["Haftalık Takip"]
for i, w in enumerate([11, 16, 18, 10, 18, 14, 18, 40]):
    ws.set_column(i, i, w, cell if i == 7 else center)
for c, v in enumerate(takip.columns):
    ws.write(0, c, v, header)

ws.data_validation(1, 4, n_takip, 4, {"validate": "list",
                                       "source": ["🟢 Tamamlandı", "🟡 Devam Ediyor", "🔴 Başlamadı"]})
renklendir(ws, 1, 4, n_takip, 4, [("🟢 Tamamlandı", green), ("🟡 Devam Ediyor", yellow), ("🔴 Başlamadı", red)])
for col in (5, 6):
    ws.data_validation(1, col, n_takip, col, {"validate": "list", "source": ["Evet", "Hayır"]})
    renklendir(ws, 1, col, n_takip, col, [("Evet", green), ("Hayır", red)])

ws.autofilter(0, 0, n_takip, len(takip.columns) - 1)  # Mentorlar kendi takımını filtreleyebilir
ws.freeze_panes(1, 4)

T = "'Haftalık Takip'"
rng = lambda col: f"{T}!${col}$2:${col}${n_takip + 1}"  # noqa: E731
R_TAKIM, R_MENTI, R_HAFTA, R_DURUM, R_PR, R_TOPL = (rng(c) for c in "ACDEFG")

# ---- Sayfa 3: Menti Özeti ----
ws = wb.add_worksheet("Menti Özeti")
ws.merge_range(0, 0, 0, 8, "AKDENİZ ÜNİVERSİTESİ - 5 HAFTALIK VERİ BİLİMİ MENTORLUK / MENTİ ÖZETİ", title)
basliklar = ["Takım", "Alt Mentor", "Menti", "Tamamlanan Hafta", "İlerleme",
             "Onaylı PR", "Toplantı Katılımı", "Bitirme Projesi", "Mezuniyet"]
for c, v in enumerate(basliklar):
    ws.write(1, c, v, header)
for i, w in enumerate([11, 16, 18, 16, 12, 12, 16, 16, 18]):
    ws.set_column(i, i, w)

r = 2
for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
    for menti in mentiler:
        x = r + 1
        ws.write(r, 0, f"Takim_{t_no:02d}", center)
        ws.write(r, 1, mentor, center)
        ws.write(r, 2, menti, center)
        ws.write_formula(r, 3, f'=COUNTIFS({R_MENTI},C{x},{R_DURUM},"🟢 Tamamlandı")', center)
        ws.write_formula(r, 4, f"=D{x}/{HAFTA_SAYISI}", pct)
        ws.write_formula(r, 5, f'=COUNTIFS({R_MENTI},C{x},{R_PR},"Evet")', center)
        ws.write_formula(r, 6, f'=COUNTIFS({R_MENTI},C{x},{R_TOPL},"Evet")&"/{HAFTA_SAYISI}"', center)
        ws.write_formula(r, 7, f'=IF(COUNTIFS({R_MENTI},C{x},{R_HAFTA},"Hafta {HAFTA_SAYISI}",'
                               f'{R_DURUM},"🟢 Tamamlandı")>0,"Evet","Hayır")', center)
        ws.write_formula(r, 8, f'=IF(AND(D{x}>={MEZUNIYET_MIN_HAFTA},H{x}="Evet"),'
                               f'"🎓 Mezun","⏳ Devam")', center)
        r += 1
son = r - 1
ws.conditional_format(2, 4, son, 4, {"type": "2_color_scale", "min_color": "#FFFFFF", "max_color": "#63BE7B",
                                     "min_type": "num", "min_value": 0, "max_type": "num", "max_value": 1})
renklendir(ws, 2, 7, son, 7, [("Evet", green), ("Hayır", red)])
renklendir(ws, 2, 8, son, 8, [("🎓 Mezun", green), ("⏳ Devam", yellow)])
ws.freeze_panes(2, 3)

# ---- Sayfa 4: Takım Özeti (Baş Mentor paneli) ----
ws = wb.add_worksheet("Takım Özeti")
ws.merge_range(0, 0, 0, 5, "TAKIM ÖZETİ - BAŞ MENTOR PANELİ", title)
for c, v in enumerate(["Takım", "Alt Mentor", "Menti Sayısı", "Tamamlanan Görev",
                       "Takım İlerlemesi", "Onaylı PR"]):
    ws.write(1, c, v, header)
for i, w in enumerate([11, 16, 14, 18, 16, 12]):
    ws.set_column(i, i, w)

r = 2
for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
    x = r + 1
    ws.write(r, 0, f"Takim_{t_no:02d}", center)
    ws.write(r, 1, mentor, center)
    ws.write(r, 2, len(mentiler), center)
    ws.write_formula(r, 3, f'=COUNTIFS({R_TAKIM},A{x},{R_DURUM},"🟢 Tamamlandı")', center)
    ws.write_formula(r, 4, f"=D{x}/(C{x}*{HAFTA_SAYISI})", pct)
    ws.write_formula(r, 5, f'=COUNTIFS({R_TAKIM},A{x},{R_PR},"Evet")', center)
    r += 1
x = r + 1
ws.write(r, 0, "TOPLAM", header)
ws.write(r, 1, "", header)
ws.write_formula(r, 2, f"=SUM(C3:C{r})", header)
ws.write_formula(r, 3, f"=SUM(D3:D{r})", header)
ws.write_formula(r, 4, f"=D{x}/(C{x}*{HAFTA_SAYISI})", wb.add_format(
    {"num_format": "0%", "bold": True, "align": "center", "bg_color": "#1F4E78", "font_color": "white", "border": 1}))
ws.write_formula(r, 5, f"=SUM(F3:F{r})", header)
ws.conditional_format(2, 4, r - 1, 4, {"type": "data_bar", "bar_color": "#63BE7B",
                                       "min_type": "num", "min_value": 0, "max_type": "num", "max_value": 1})

writer.close()
print(f"✅ {cikti} oluşturuldu ({len(TAKIMLAR)} takım, {sum(map(len, TAKIMLAR.values()))} menti).")

# =====================================================================
# 5. KLASÖR YAPISI (01_Takimlar/Takim_XX_Mentor/Menti/haftaX)
# =====================================================================
if KLASORLERI_OLUSTUR:
    for t_no, (mentor, mentiler) in enumerate(TAKIMLAR.items(), start=1):
        for menti in mentiler:
            for h in range(1, HAFTA_SAYISI + 1):
                yol = os.path.join(REPO_DIR, "01_Takimlar", f"Takim_{t_no:02d}_{mentor}", menti, f"hafta{h}")
                os.makedirs(yol, exist_ok=True)
                gk = os.path.join(yol, ".gitkeep")
                if not os.path.exists(gk):
                    open(gk, "w").close()
    print("✅ 01_Takimlar klasör yapısı oluşturuldu.")
