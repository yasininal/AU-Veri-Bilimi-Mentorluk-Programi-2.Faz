# Modül 2 — Makine Öğrenmesi Temelleri (3 Hafta)

Tebrikler! Modül 1'i tamamlayarak Makine Öğrenmesi modülüne geçmeye hak kazandınız. 🎉

- **Kaynak:** BTK Akademi — Kaan Can Yılmaz, *"Makine Öğrenmesi"* (ücretsiz)
- **Haftalık video yükü:** Yaklaşık 1.5 saat (seçilen kritik videolar)
- **Teslim:** Her hafta **Pazar 23:59**'a kadar GitHub'a Pull Request (PR)
- **Toplantılar:** Modül başında baş mentorla genel açılış toplantısı ve mentorunuzla takım toplantısı (her hafta tekrarlanmaz)

> [!NOTE]
> Bu modülde bilerek **en temel ve sektörde en çok kullanılan** konulara odaklanıyoruz: Veri ön işleme, Regresyon, Lojistik Regresyon, KNN, Karar Ağaçları, Random Forest ve Değerlendirme Metrikleri (Confusion Matrix vb.). Amaç tüm algoritmaları ezberlemek değil, **bir problemi uçtan uca çözebilecek yetkinliğe ulaşmaktır.**

> [!IMPORTANT]
> **Mezuniyet şartı:** Modül 2'nin **3 haftasının tamamını** tamamlamak (3. haftadaki bitirme projesi dahil).

---

## 1. Hafta: ML Süreci, Veri Ön İşleme ve Regresyon (Sayısal Tahmin)

Bu haftanın hedefi: Veriyi makine öğrenmesine hazırlamak (`train_test_split`, `encoding`), ilk doğrusal regresyon modelini eğitmek ve $R^2$ / MSE ile model başarısını ölçmek.

### 🎬 İzlenecek Zorunlu Videolar (~1 saat 45 dk)
BTK Akademi — **Kaan Can Yılmaz / Makine Öğrenmesi** eğitimi altından:
- `2.1` Makine Öğrenmesi Temel Kavramlar & `2.4` Makine Öğrenmesi Süreci *(18 dk)* — Temel mantık ve iş akışı
- `3.1` Veri Ön İşleme & `3.3` Veri Tipleri ve Dönüşümleri *(45 dk)* — Eksik veri, One-Hot/Label Encoding, train/test mantığı
- `5.18` & `5.19` Lineer Regresyon 1 ve 2 *(28 dk)* — Basit ve çoklu regresyon modelleri
- `9.2` Regresyon için Değerlendirme Metrikleri *(14 dk)* — $R^2$, MSE, RMSE ve MAE skorları

> [!TIP]
> **Atlayabileceğiniz / Opsiyonel Videolar:**
> - `Bölüm 4` Matematik ve İstatistik (Lineer Cebir, Kalkülüs) — *Menteelerin matematik teorisine boğulmasına gerek yoktur.*
> - `5.20 - 5.21` Çoklu ve Polinom Regresyon detayları
> - `3.2` & `3.4` Öznitelik Mühendisliği & Aykırı Değer detayları

### 📝 Görev (PR #1)
- Sürekli bir hedef değişkeni olan bir veri seti seçin (ev/araba fiyatı veya maaş tahmini).
- Veriyi eğitim ve test olarak ayırın (`train_test_split`).
- Bir `LinearRegression` modeli eğitin ve test verisindeki $R^2$ ve MSE skorlarını yazdırıp yorumlayın.
- İlk PR'ınızı açın.

### ❓ Kontrol Sorusu
Modeli neden tüm veriyle değil de ayrı bir test kümesiyle (`X_test`, `y_test`) değerlendiririz?

---

## 2. Hafta: Sınıflandırma Temelleri ve Model Başarı Metrikleri

Bu haftanın hedefi: Evet/Hayır (0/1) tipi kategorik problemleri çözmek; Confusion Matrix, Accuracy, Precision ve Recall değerlerini okumayı öğrenmek.

### 🎬 İzlenecek Zorunlu Videolar (~1 saat 30 dk)
- `5.1` Gözetimli Öğrenme Giriş *(8 dk)*
- `5.10` & `5.11` Lojistik Regresyon 1 ve 2 *(50 dk)* — Sınıflandırmanın temel taşı
- `5.2` K-En Yakın Komşu (KNN) 1 *(21 dk)* — Komşuluk bazlı sezgisel model
- `9.1` Sınıflandırma için Değerlendirme Metrikleri *(18 dk)* — **Bu haftanın en kritik konusu:** Confusion Matrix, Accuracy, Precision, Recall, F1 Score

> [!TIP]
> **Atlayabileceğiniz / Opsiyonel Videolar:**
> - `5.12 - 5.13` Lojistik Regresyon ileri detaylar
> - `5.3` KNN 2
> - `5.14 - 5.15` Destek Vektör Makineleri (SVM)
> - `5.16 - 5.17` Naive Bayes

### 📝 Görev (PR #2)
- Modül 1'de incelediğiniz *Titanic* veri setini (veya benzeri bir sınıflandırma veri setini) kullanın.
- Lojistik Regresyon ve KNN modelleri kurup eğitin.
- Her iki modelin Accuracy skorunu ve Confusion Matrix'ini yazdırıp karşılaştırın.

### ❓ Kontrol Sorusu
Bir modelin Accuracy değeri %95 çıktığında bu model her senaryoda mükemmel midir? Dengesiz veri setlerinde (örn. kanser tespiti veya dolandırıcılık) neden Precision ve Recall'a bakarız?

---

## 3. Hafta: Ağaç Tabanlı Modeller ve Bitirme Projesi

Bu haftanın hedefi: Sektörün en popüler ve güçlü modelleri olan Karar Ağaçları ve Random Forest'ı öğrenip 3 haftalık süreci uçtan uca bir bitirme projesiyle tamamlamak.

### 🎬 İzlenecek Zorunlu Videolar (~50 dk)
- `5.4` & `5.5` Karar Ağaçları (Decision Tree) 1 ve 2 *(30 dk)* — Ağaç mantığı ve kodlaması
- `5.9` Rasgele Orman (Random Forest) *(20 dk)* — Topluluk (Ensemble) mantığı

> [!TIP]
> **Atlayabileceğiniz / Opsiyonel Videolar:**
> - `5.6 - 5.8` Karar Ağaçları 3, 4, 5
> - `Bölüm 6` Gözetimsiz Öğrenme (K-Means, Hiyerarşik Kümeleme)
> - `Bölüm 7` Pekiştirmeli Öğrenme (Q-Learning)
> - `Bölüm 8` Boyut İndirgeme (PCA)
> - `Bölüm 10 - 11` Hiperparametre ve Regularizasyon

### 📝 Bitirme Projesi (PR #3 — ZORUNLU)
Bu hafta video süresi bilerek çok kısa tutulmuştur. Tüm enerjinizi seçtiğiniz bir sınıflandırma veri setinde hazırlayacağınız **Bitirme Projesi Notebook'una** ayırın:
1. Veri yükleme, ön işleme (`encoding`) ve train/test ayrımı
2. **Lojistik Regresyon** ile **Random Forest** modellerini eğitme
3. Confusion Matrix ve Accuracy sonuçları üzerinden iki modeli karşılaştırma
4. Notebook başına 3-5 cümlelik özet: *"Hangi model neden daha iyi performans verdi?"*
5. **Demo Günü:** Bitirme projeleri program sonunda kişi başı 5 dakikalık sunumlarla paylaşılır.

### ❓ Kontrol Sorusu
Tek bir Karar Ağacı yerine yüzlerce ağaçtan oluşan Random Forest modeli neden genellikle çok daha yüksek başarı verir ve ezberlemeye (overfitting) karşı daha dirençlidir?

---

## Ödev Klasör Yapısı

```
01_Takimlar/Takim_XX_MentorAdi/Adiniz_Soyadiniz/modul2/haftaX/odevX.ipynb
```

Detaylı adımlar için: [Github_Takim_Kullanimi.md](Github_Takim_Kullanimi.md)

Tüm modülleri başarıyla tamamlayan arkadaşlarımız **Mezuniyet Rozeti** ve topluluk içi **Proje Ekibi / Mentorluk** hakkı kazanacaktır! 🎓
