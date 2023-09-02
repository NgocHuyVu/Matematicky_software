import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageDraw, ImageFont
import cv2

data = pd.read_csv("Data.csv")

# Graf 1: Top 10 střelců s nejvíce góly
top10_scorers = data.sort_values(by="Goals", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Jméno hráče", y="Góly", data=top10_scorers, palette="viridis")
plt.xlabel("Jméno hráče")
plt.ylabel("Počet gólů")
plt.title("Top 10 střelců s nejvíce góly")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graf 2: Top 10 hráčů má nejlepší poměr gólů/xG
data["Poměr gólů k xG"] = data["Góly"] / data["xG"]
top10_scorers_conversion = data.sort_values(by="Poměr gólů k xG", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Jméno hráče", y="Poměr gólů k xG", data=top10_scorers_conversion, palette="viridis")
plt.xlabel("Jméno hráče")
plt.ylabel("Poměr gólů k xG")
plt.title("Top 10 hráčů má nejlepší poměr gólů/xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graf 3: Top 10 hráčů s nejvyšším xG
top10_xG_scorers = data.sort_values(by="xG", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Jméno hráče", y="xG", data=top10_xG_scorers, palette="viridis")
plt.xlabel("Jméno hráče")
plt.ylabel("xG (Očekávané góly)")
plt.title("Top 10 hráčů s nejvyšším xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graf 4: Top ligy podle počtu gólů
celkové_góly_podle_ligy = data.groupby("Liga")["Góly"].sum().reset_index()
top_ligy = celkové_góly_podle_ligy.sort_values(by="Góly", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x="Liga", y="Góly", data=top_ligy, palette="viridis")
plt.xlabel("Název ligy")
plt.ylabel("Celkový počet gólů")
plt.title("Top ligy podle počtu gólů")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graf 5: Top ligy podle xG
celkové_xG_podle_ligy = data.groupby("Liga")["xG"].sum().reset_index()
top_ligy = celkové_xG_podle_ligy.sort_values(by="xG", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Liga", y="xG", data=top_ligy, palette="viridis")
plt.xlabel("Název ligy")
plt.ylabel("Celkové xG")
plt.title("Top ligy podle celkového xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graf 6: Top ligy podle poměru gólů/xG
data["Poměr gólů k xG"] = data["Góly"] / data["xG"]
poměr_gólů_k_xG_podle_ligy = data.groupby("Liga")["Poměr gólů k xG"].mean().reset_index()
top_ligy = poměr_gólů_k_xG_podle_ligy.sort_values(by="Poměr gólů k xG", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Liga", y="Poměr gólů k xG", data=top_ligy, palette="viridis")
plt.xlabel("Název ligy")
plt.ylabel("Poměr gólů k xG")
plt.title("Top ligy podle poměru gólů/xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()