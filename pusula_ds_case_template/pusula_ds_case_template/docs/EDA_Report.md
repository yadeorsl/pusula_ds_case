# EDA & Preprocessing Report

**Name:** Yade Örsel  
**E-mail:** yadeorsl@gmail.com  

---

## 1. Dataset Overview
- Total rows: 2235  
- Total columns: 13  
- Target variable: **TedaviSuresi** (treatment duration in sessions)  
- ID column: **HastaNo** (not used for modeling)

---

## 2. Missing Values
- **KanGrubu** → ~670 missing  
- **Alerji, Tanilar, UygulamaYerleri** → birçok missing  
- Strategy:
  - Numerical → median imputation  
  - Categorical → mode imputation or "Unknown"

---

## 3. Key Findings from EDA
- **Age (Yas):** dağılım normal dağılıma yakın, ortalama ~40.  
- **Gender (Cinsiyet):** kadın hasta sayısı erkeklerden fazla.  
- **Blood Type (KanGrubu):** O Rh+ ve A Rh+ en yaygın.  
- **Nationality (Uyruk):** çoğu Türkiye, diğerleri "Other" olarak gruplandı.  
- **Treatment Duration (TedaviSuresi):** sağa çarpık, çoğu hasta 5–15 seans. Outlier değerler (100+) mevcut.  
- **Application Duration (UygulamaSuresi):** dakikaya çevrildi, normalleştirildi.

---

## 4. Preprocessing Steps
1. **TedaviSuresi** metinden (örn. "10 seans") sayıya çevrildi.  
2. **UygulamaSuresi** "dk/saat" formatından dakikaya çevrildi.  
3. Eksik değerler → median (numeric), mode/Unknown (categorical).  
4. Kategorik stringler temizlendi (strip, lowercase normalize).  
5. Multi-label sütunlar (KronikHastalik, Alerji, Tanilar, UygulamaYerleri) listeye çevrildi ve sayısı eklendi.  
6. OneHotEncoder → kategorikler, StandardScaler → sayısallar.  

---

## 5. Engineered Features (Extra)
- **YasBin**: age bins → child (0–18), young (19–40), adult (41–60), senior (60+).  
- **KronikHastalik_count**: kronik hastalık sayısı.  
- **Alerji_count**: alerji sayısı.  
- **Tanilar_count** ve **UygulamaYerleri_count**.  

---

## 6. Outputs
- Clean dataset → `outputs/cleaned_dataset.csv`  
- Processed features → `outputs/processed_X.csv`  
- Target (y) → `outputs/y.csv`  
- Preprocessing pipeline → `outputs/preprocess_pipeline.joblib`
