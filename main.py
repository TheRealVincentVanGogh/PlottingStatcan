import pandas as pd
import matplotlib.pyplot as plt
from stats_can import StatsCan

# Dark mode!
plt.style.use("dark_background")

sc = StatsCan()
# get StatsCan table
df = sc.table_to_df("24-10-0005-01")

# only keep Canada wide data
df = df[df.GEO == "Canada"]
# grab data in specified timeframe
mask = (df["REF_DATE"] > "2019-01-01") & (df["REF_DATE"] <= "2020-05-28")
# apply timeframe filter
df = df.loc[mask]

# optional settings to disable truncation
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", None)

# reshape dataframe
df = df.pivot(index="REF_DATE", columns="Traveller category", values="VALUE")
df.plot()

plt.xlabel("Date")
plt.ylabel("People")
plt.title("Travel Activity In/Out of Canada")
plt.legend()
plt.show()

print(df)
