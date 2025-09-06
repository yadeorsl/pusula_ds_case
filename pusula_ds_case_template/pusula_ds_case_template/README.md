# Pusula DS Case — Starter

**Ad Soyad:** (Adınızı yazın)  
**E-posta:** (E-postanızı yazın)

## Nasıl Çalıştırılır
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -U pip pandas numpy scikit-learn matplotlib seaborn openpyxl jupyter
```

- Veriyi `data/Talent_Academy_Case_DT_2025.xlsx` yoluna kopyalayın.
- Jupyter notebook'u açın ve `notebooks/01_eda.ipynb` dosyasını çalıştırın.
- Çıktılar `outputs/` klasörüne yazılır.

## Dosyalar
- `notebooks/01_eda.ipynb`: EDA başlangıç not defteri
- `src/preprocess.py`: Basit ön işleme pipeline'ı (model öncesi kullanım için)
- `outputs/`: Son çıktıların yazılacağı klasör
- `data/`: Ham veriyi koyacağınız klasör
