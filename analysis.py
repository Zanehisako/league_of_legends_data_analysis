import matplotlib.pyplot as plt
import pandas as pd

global_stats_df = pd.read_csv("Champion_stats.csv")
plt.bar(global_stats_df['Champion'],global_stats_df['Games Played'])
plt.show()
