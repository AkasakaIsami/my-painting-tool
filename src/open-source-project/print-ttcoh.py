import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/tt/tt-coh.csv')
box_1, box_2, box_3 = data['DAH'], data['PIH'], data['SIH']

plt.figure(figsize=(5, 5))  # 设置画布的尺寸

labels = 'DAH', 'PIH', 'SIH'  # 图例

colors = ['#515151', '#f14040', '#1a6fdf', '#ffffff']

c = colors[1]
# plt.grid(True)
# plt.grid(color='r',
#          linestyle='--',
#          linewidth=1,
#          alpha=0.3)


grid=False
# plt.boxplot([box_1, box_2, box_3], labels=labels, widths=0.7, showmeans=True, patch_artist=True,
#             boxprops=dict(facecolor=c, color=c, linewidth=1.5),
#             capprops=dict(color="black", linewidth=1.5),
#             whiskerprops=dict(color="black", linewidth=1.5),
#             flierprops=dict(color="black", linewidth=1.5),
#             medianprops=dict(color="black", linewidth=1.5),
#             meanprops=dict(color="black"))

plt.boxplot([box_1, box_2, box_3], labels=labels, widths=0.7, showmeans=True)
plt.ylabel("Metric Values")
plt.xlabel("Cohesion Metrics")  # 我们设置横纵坐标的标题。
plt.show()  # 显示图像
