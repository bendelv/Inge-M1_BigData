import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("belgium_consumption_sector.csv", sep=',', index_col=0)
df = df.drop(columns="Total")

print(df.corr())
print(df.columns)
plt.matshow(df.corr())
plt.show()