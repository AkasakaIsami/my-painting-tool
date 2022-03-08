from numpy import arange
import pandas as pd
import matplotlib.pyplot as plt
from pylab import axes


# 读取数据
data = pd.read_csv('./data/cc/cc-coh.csv')
box_1, box_2, box_3, box_4, box_5, box_6 = data['DAH1'],data['DAH2'], data['PIH1'],data['PIH2'], data['SIH1'], data['SIH2']

plt.figure(figsize=(10, 5))  # 设置画布的尺寸

colors = ['#515151', '#f14040', '#1a6fdf', '#ffffff']

c1='r'
c2='b'
grid=False

plt.boxplot([box_1.dropna()], positions = [1], widths=0.7, showmeans=True, boxprops=dict(color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_2], positions = [2], widths=0.7, showmeans=True, boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_3.dropna()], positions = [4], widths=0.7, showmeans=True, boxprops=dict(color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_4], positions = [5], widths=0.7, showmeans=True, boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_5.dropna()], positions = [7], widths=0.7, showmeans=True, boxprops=dict(color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_6], positions = [8], widths=0.7, showmeans=True, boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))

plt.xticks([1.5,4.5,7.5], ['DAH', 'PIH', 'SIP'])

plt.plot([], c=c1, label='System A')
plt.plot([], c=c2, label='System B')
plt.legend()

plt.ylabel("Metric Values")
plt.xlabel("Cohesion Metrics")  # 我们设置横纵坐标的标题。
plt.show()  # 显示图像
