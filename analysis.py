import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

global_stats_df = pd.read_csv("Champion_stats.csv")
sns.barplot(x=global_stats_df['Champion'],y=global_stats_df['Games Played'].astype(float))
plt.show()
