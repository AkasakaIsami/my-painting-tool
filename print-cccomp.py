import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/cc/cc-comp.csv')
box_1, box_2, box_3, box_4, box_5, box_6 = data['PCC1'], data['PCC2'], data['RIN1'], data['RIN2'], data['LIC1'], data['LIC2']

plt.figure(figsize=(10, 5))  # 设置画布的尺寸

labels = 'PCC', 'RIN', 'LIC' # 图例


c1='r'
c2='b'
grid = False

plt.boxplot([box_1], positions = [1], widths=0.7, showmeans=True, boxprops=dict(color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_2.dropna()], positions = [2], widths=0.7, showmeans=True, boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_3], positions = [4], widths=0.7, showmeans=True, boxprops=dict(color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_4.dropna()], positions = [5], widths=0.7, showmeans=True, boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_5], positions = [7], widths=0.7, showmeans=True, boxprops=dict(color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_6.dropna()], positions = [8], widths=0.7, showmeans=True, boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))

plt.xticks([1.5,4.5,7.5], ['PCC', 'RIN', 'LIC'])

plt.plot([], c=c1, label='System A')
plt.plot([], c=c2, label='System B')
plt.legend()

plt.ylabel("Metric Values")
plt.xlabel("Complexity Metrics")  # 我们设置横纵坐标的标题。
plt.show()  # 显示图像
