Pusula DS Case — Yade Örsel

Name: Yade Örsel
E-mail: yadeorsl@gmail.com

## Project Overview

This project is prepared as part of the Pusula Data Science Intern Case (2025).
The dataset consists of 2235 rows and 13 columns from a physical medicine & rehabilitation domain.
The goal is to perform exploratory data analysis (EDA), handle data preprocessing, and provide a clean, model-ready dataset with the target variable TedaviSuresi.

## Setup Instructions

Create & activate virtual environment

python -m venv .venv
.venv\Scripts\activate        # (on Windows PowerShell)



## Install requirements

pip install -r requirements.txt


## Place the dataset under

data/Talent_Academy_Case_DT_2025.xlsx


## Start Jupyter Notebook and run all cells in

notebooks/01_eda.ipynb

## Key Steps Performed

EDA (Exploratory Data Analysis): distributions, missing values, correlation heatmap.

## Preprocessing:

* Converted TedaviSuresi text to numeric

* Converted UygulamaSuresi to minutes

* Cleaned text columns

* Parsed multi-label columns (KronikHastalik, Alerji, Tanilar, UygulamaYerleri)

*Missing values imputed (median for numeric, mode/Unknown for categorical)

