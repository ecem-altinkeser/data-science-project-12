import pandas as pd
import numpy as np
# Tehlikeli kimyasalların isimlerini döndür.
# Input: DataFrame
# Output: Series (Chemical isimleri)
def get_hazardous_chemicals(df:pd.DataFrame):
    return df[df["IsHazardous"] == True]["Chemical"]


# Tüm "Amount" değerlerini grama çevir. (1 liter = 1000 gram, 1 kg = 1000 gram)
# Input: DataFrame
# Output: Yeni DataFrame, "Amount" sütunu gram cinsinden.
def convert_amounts_to_grams(df:pd.DataFrame):
    df["Amount"]  = df["Amount"]*1000
    return df


# Miktarı en fazla olan n kimyasalı döndür (gram cinsinden sıralı).
# Input: DataFrame, n=2
# Output: En fazla miktarda 2 kimyasal.
def get_top_n_chemicals(df:pd.DataFrame, n:int):
    return df.sort_values(by="Amount", ascending=False).head(n)


# Kullanılan birimlerin listesini döndür ("liter", "kg" vb.)
# Input: DataFrame
# Output: Series ya da list
def get_unique_units(df:pd.DataFrame):
    return df["Unit"].unique()


#  İsim içerisinde keyword geçen kimyasalları filtrele.
# Input: keyword="Acetone"
# Output: "Acetone" içeren satırları içeren DataFrame
def filter_chemicals_by_name(df:pd.DataFrame, keyword):
    return df[df["Chemical"] == keyword]


# Toplam madde miktarını gram cinsinden hesapla.
# Output: float
def get_total_amount(df:pd.DataFrame):
    return float(df["Amount"].sum())


# NumPy kullanarak miktarların standart sapmasını hesapla.
# Output: float
def calculate_standard_deviation(df:pd.DataFrame):
    return df["Amount"].std()


# Miktarları min-max normalize et.
# (formül: (x - min) / (max - min))
# Output: Series (normalize edilmiş değerler)
def normalize_amounts(df:pd.DataFrame):
   return (df["Amount"] - df["Amount"].min())/(df["Amount"].max()-df["Amount"].min())


# Tehlikeli olup miktarı 1000 gramdan fazla olanları "HighRisk" olarak işaretle.
# Output: Yeni DataFrame, HighRisk adında yeni sütun içerir.
def flag_high_risk(df:pd.DataFrame):
    df["HighRisk"] = (df["IsHazardous"]==True) & (df["Amount"]>1000)
    return df