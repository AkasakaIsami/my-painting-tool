import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/cc/cc-coup.csv')
box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10 = data['DAP1'], data['DAP2'], data[
    'PIP1'], data['PIP2'], data['SIP1'], data['SIP2'], data['TCP1'], data['TCP2'], data['DIP1'], data['DIP2']

c1 = 'r'
c2 = 'b'

plt.figure(figsize=(13, 5))  # 设置画布的尺寸

labels = 'DAP', 'PIP', 'SIP', 'TCP', 'DIP'  # 图例


grid = False


plt.boxplot([box_1.dropna()], positions=[1], widths=0.7, showmeans=True, boxprops=dict(
    color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_2], positions=[2], widths=0.7, showmeans=True, boxprops=dict(
    color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_3.dropna()], positions=[4], widths=0.7,showmeans=True, boxprops=dict(
    color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_4], positions=[5], widths=0.7, showmeans=True, boxprops=dict(
    color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_5.dropna()], positions=[7], widths=0.7, showmeans=True, boxprops=dict(
    color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_6], positions=[8], widths=0.7, showmeans=True, boxprops=dict(
    color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_7.dropna()], positions=[10], widths=0.7, showmeans=True, boxprops=dict(
    color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_8], positions=[11], widths=0.7, showmeans=True, boxprops=dict(
    color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))
plt.boxplot([box_9.dropna()], positions=[13], widths=0.7, showmeans=True, boxprops=dict(
    color=c1), capprops=dict(color=c1), whiskerprops=dict(color=c1))
plt.boxplot([box_10.dropna()], positions=[14], widths=0.7, showmeans=True, boxprops=dict(
    color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))

plt.xticks([1.5, 4.5, 7.5, 10.5, 13.5], ['DAP', 'PIP', 'SIP', 'TCP', 'DIP'])

plt.plot([], c=c1, label='System A')
plt.plot([], c=c2, label='System B')
plt.legend()


plt.ylabel("Metric Values")
plt.xlabel("Coupling Metrics")  # 我们设置横纵坐标的标题。
plt.show()  # 显示图像
