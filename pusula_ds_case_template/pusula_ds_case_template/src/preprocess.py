# src/preprocess.py  — CWD'den bağımsız, ayrıntılı loglu
from pathlib import Path
import re, joblib
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Nereden çalıştırırsan çalıştır doğru yolu bulsun
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "Talent_Academy_Case_DT_2025.xlsx"
OUT_DIR = BASE_DIR / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def to_minutes(x):
    if pd.isna(x): return np.nan
    s = str(x).lower().strip()
    m = re.findall(r'(\d+(?:[.,]\d+)?)\s*(saat|dk|min)?', s)
    if not m: return np.nan
    val, unit = m[0]
    val = float(val.replace(',', '.'))
    return val*60 if unit == 'saat' else val

def count_items(x):
    if pd.isna(x) or str(x).strip().lower() in ['nan','none','']: return 0
    return len([t.strip() for t in str(x).split(',') if t.strip()])

def clean_tedavi_suresi(series):
    s = (series.astype(str)
              .str.replace(r'[^0-9.,]', '', regex=True)
              .str.replace(',', '.', regex=False))
    out = pd.to_numeric(s, errors='coerce')
    med = out.median(skipna=True) if out.notna().any() else 0.0
    return out.fillna(med).astype(int)

def prepare_features(df: pd.DataFrame):
    if 'UygulamaSuresi' in df.columns:
        df['UygulamaSuresi'] = df['UygulamaSuresi'].apply(to_minutes)
    if 'TedaviSuresi' in df.columns:
        df['TedaviSuresi'] = clean_tedavi_suresi(df['TedaviSuresi'])

    for c in ['KronikHastalik','Alerji','Tanilar','UygulamaYerleri']:
        if c in df.columns:
            df[f'{c}_count'] = df[c].apply(count_items)

    if 'Yas' in df.columns:
        df['YasBin'] = pd.cut(df['Yas'], bins=[-1,18,40,60,200],
                              labels=['child','young','adult','senior'])

    y = df['TedaviSuresi']
    drop_cols = ['TedaviSuresi','HastaNo','KronikHastalik','Alerji','Tanilar','UygulamaYerleri']
    X = df.drop([c for c in drop_cols if c in df.columns], axis=1)

    num_cols = list(X.select_dtypes(include='number').columns)
    cat_cols = [c for c in X.columns if c not in num_cols]
    return X, y, num_cols, cat_cols

def build_pipeline(num_cols, cat_cols):
    num_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    cat_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ohe', OneHotEncoder(handle_unknown='ignore', min_frequency=0.01))
    ])
    return ColumnTransformer([
        ('num', num_pipe, num_cols),
        ('cat', cat_pipe, cat_cols)
    ])

def main():
    print("BASE_DIR :", BASE_DIR)
    print("DATA_PATH:", DATA_PATH)
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Excel bulunamadı: {DATA_PATH}")
    df = pd.read_excel(DATA_PATH)
    print(f"Loaded dataframe: rows={len(df)} cols={len(df.columns)}")

    X, y, num_cols, cat_cols = prepare_features(df)
    print(f"Num cols: {len(num_cols)} | Cat cols: {len(cat_cols)}")

    pre = build_pipeline(num_cols, cat_cols)
    X_proc = pre.fit_transform(X)
    feat_names = pre.get_feature_names_out()
    dense = X_proc.toarray() if hasattr(X_proc, 'toarray') else X_proc
    X_df = pd.DataFrame(dense, columns=feat_names)

    X_path = OUT_DIR / "processed_X.csv"
    y_path = OUT_DIR / "y.csv"
    pipe_path = OUT_DIR / "preprocess_pipeline.joblib"
    X_df.to_csv(X_path, index=False)
    y.to_csv(y_path, index=False)
    joblib.dump(pre, pipe_path)

    print("Saved:")
    print(" ", X_path)
    print(" ", y_path)
    print(" ", pipe_path)
    print("✅ Done.")

if __name__ == "__main__":
    main()
