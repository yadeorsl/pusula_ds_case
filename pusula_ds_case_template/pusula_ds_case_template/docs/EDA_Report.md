# EDA & Preprocessing Report

Name: Yade Örsel  
E-mail: yadeorsl@gmail.com  

---

## 1. Dataset Overview
- Total rows: 2235  
- Total columns: 13  
- Target variable: TedaviSuresi (treatment duration in sessions)  
- ID column: HastaNo (not used for modeling)

---

## 2. Missing Values
| Column          | Missing |
| --------------- | ------- |
| Alerji          | 944     |
| KanGrubu        | 675     |
| KronikHastalik  | 611     |
| UygulamaYerleri | 221     |
| Cinsiyet        | 169     |
| Tanilar         | 75      |
| Bolum           | 11      |


---

## 3. Key Findings from EDA
-Age (Yas): approximately normal; mean ≈ 47.33 (min 2, max 92).

Gender (Cinsiyet): Kadın 1274, Erkek 792, NaN 169.

Blood Type (KanGrubu): 0 Rh+ is the most common (≈ 579). Next most common types are A Rh+, B Rh+, etc.

Nationality (Uyruk): predominantly Türkiye (2173); remaining are very small minorities (e.g., Tokelau, Arnavutluk…).

Treatment Duration (TedaviSuresi): strongly concentrated at 15 sessions (1670 rows); overall right-skewed with a small number of higher values.

Application Duration (UygulamaSuresi): textual durations converted to minutes (e.g., “20 Dakika”, “1 saat”).

HastaNo duplicates: present (example groups at 145135, 145136, 145137, …). This indicates multiple rows per patient/episode and should be considered before any modeling (e.g., deduplicate or aggregate per patient).

---

## 4. Preprocessing Steps
TedaviSuresi numeric conversion: extracted numbers from text (e.g., “15 Seans” → 15.0), unified decimal marks, cast to float, and imputed with median when needed.

Final dtype: float64

NaN count: 0

First 20 unique values (sample from your output): [5., 15., 10., 18., 20., 2., 6., 4., 30., 11., 16., 21., 1., 8., 3., 7., 19., 29., 14., 17.]

UygulamaSuresi normalization: parsed “dk/min/saat” patterns and converted everything to minutes.

Text normalization: stripped and collapsed whitespace across key text columns.

Multi-label columns to lists: KronikHastalik, Alerji, Tanilar, UygulamaYerleri were split on commas, trimmed, and cased consistently.

Imputation:

Numerical → median

Categorical (non-list) → most frequent (mode)

Note: A helper column TedaviSuresi_raw was kept as a backup of the original text before conversion.otEncoder → kategorikler, StandardScaler → sayısallar.  

---

## 5. Engineered Features (Extra)
Count features: *_count for number of chronic diseases, allergies, diagnoses, application sites.

Age bins: YasBin (child 0–18, young 19–40, adult 41–60, senior 60+).

(Optional) Deduplication strategy for HastaNo before modeling:

numerics → mean/median

lists → union

single-label categoricals → first/most-frequent

---

## 6. Outputs
- Clean dataset → `outputs/cleaned_dataset.csv`  

