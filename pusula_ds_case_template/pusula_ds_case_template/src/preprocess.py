import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def build_pipeline(df: pd.DataFrame, target: str = "TedaviSuresi"):
    # List-type columns should be handled before this function (multi-hot etc.)
    X = df.drop(columns=[target]) if target in df.columns else df.copy()
    num_cols = X.select_dtypes(include=["number"]).columns
    cat_cols = X.select_dtypes(exclude=["number"]).columns

    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder(handle_unknown="ignore"))
    ])

    pre = ColumnTransformer([
        ("num", num_pipe, list(num_cols)),
        ("cat", cat_pipe, list(cat_cols))
    ])

    return pre

def fit_transform(df: pd.DataFrame, target: str = "TedaviSuresi"):
    y = df[target] if target in df.columns else None
    X = df.drop(columns=[target]) if target in df.columns else df.copy()
    pre = build_pipeline(df, target)
    X_ready = pre.fit_transform(X)
    return X_ready, y, pre
