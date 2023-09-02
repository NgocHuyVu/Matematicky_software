import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageDraw, ImageFont
import cv2

data = pd.read_csv("Data.csv")

# Graf 1: Top 10 střelců s nejvíce góly
top10_scorers = data.sort_values(by="Goals", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Player Names", y="Goals", data=top10_scorers, palette="viridis")
plt.xlabel("Jméno hráče")
plt.ylabel("Počet gólů")
plt.title("Top 10 střelců s nejvíce góly")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graf 2: Top 10 hráčů s nejvyšším xG
top10_xG_scorers = data.sort_values(by="xG", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Player Names", y="xG", data=top10_xG_scorers, palette="viridis")
plt.xlabel("Jméno hráče")
plt.ylabel("xG (Očekávané góly)")
plt.title("Top 10 hráčů s nejvyšším xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Graf 3: Top 10 hráčů má nejlepší poměr gólů/xG
data["Goal Conversion Rate"] = data["Goals"] / data["xG"]
top10_scorers_conversion = data.sort_values(by="Goal Conversion Rate", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Player Names", y="Goal Conversion Rate", data=top10_scorers_conversion, palette="viridis")
plt.xlabel("Jméno hráče")
plt.ylabel("Poměr gólů k xG")
plt.title("Top 10 hráčů má nejlepší poměr gólů/xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Graf 4: Top ligy podle počtu gólů
total_goals_by_league = data.groupby("League")["Goals"].sum().reset_index()
top_leagues = total_goals_by_league.sort_values(by="Goals", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x="League", y="Goals", data=top_leagues, palette="viridis")
plt.xlabel("Název ligy")
plt.ylabel("Celkový počet gólů")
plt.title("Top ligy podle počtu gólů")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Graf 5: Top ligy podle celkového očekávaného počtu gólů (xG)
total_xG_by_league = data.groupby("League")["xG"].sum().reset_index()
top_leagues = total_xG_by_league.sort_values(by="xG", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="League", y="xG", data=top_leagues, palette="viridis")
plt.xlabel("Název ligy")
plt.ylabel("Celkové xG")
plt.title("Top ligy podle celkového xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Graf 6: Top ligy podle průměrného poměru gólů k očekávaným gólům (xG)
data["Goal Conversion Rate"] = data["Goals"] / data["xG"]
conversion_rate_by_league = data.groupby("League")["Goal Conversion Rate"].mean().reset_index()
top_leagues = conversion_rate_by_league.sort_values(by="Goal Conversion Rate", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="League", y="Goal Conversion Rate", data=top_leagues, palette="viridis")
plt.xlabel("Název ligy")
plt.ylabel("Poměr gólů k xG")
plt.title("Top ligy podle poměru gólů/xG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
