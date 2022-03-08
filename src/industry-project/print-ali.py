import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/ali/ali-coh.csv')
box_1, box_2, box_3 = data['DAH'], data['PIH'], data['SIH']

# plt.figure(figsize=(18, 2.5))  # 设置画布的尺寸

colors = ['#515151', '#f14040', '#1a6fdf', '#ffffff']
labels = 'DAH', 'PIH', 'SIH'  # 图例

c2 = 'b'
grid = False

fig, ax = plt.subplots(1, 3, figsize=(15, 2.5), gridspec_kw={
                       'width_ratios': [3, 5, 7]})

ax[0].boxplot([box_1.dropna(), box_2.dropna(), box_3.dropna()], labels=labels, widths=0.7, showmeans=True,
              boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))


data = pd.read_csv('./data/tt/tt-coup.csv')
box_1, box_2, box_3, box_4, box_5 = data['DAP'], data['PIP'], data['SIP'], data['DIP'], data['TCP']
labels = 'DAP', 'PIP', 'SIP', 'DIP', 'TCP'  # 图例
ax[1].boxplot([box_1.dropna(), box_2.dropna(), box_3.dropna(), box_4.dropna(), box_5.dropna()],
              labels=labels, widths=0.7, showmeans=True, flierprops=dict(marker='o',markeredgecolor=c2), boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))



data = pd.read_csv('./data/ali/ali-comp.csv')
box_1, box_2, box_3, box_4, box_5, box_6, box_7 = data['LIC'], data['RIN'], data['PCC'], data['RCD-IN'], data['RCD-SE'], data['SCD-IN'], data['SCD-SE']
labels = 'LIC', 'RIN', 'PCC', 'RCD-IN','RCD-SE', 'SCD-IN', 'SCD-SE' # 图例
plt.boxplot([box_1.dropna(), box_2.dropna(), box_3.dropna(), box_4.dropna(), box_5.dropna(), box_6.dropna(), box_7.dropna()],
            labels=labels, widths=0.7, showmeans=True, flierprops=dict(marker='o', markeredgecolor=c2), boxprops=dict(color=c2), capprops=dict(color=c2), whiskerprops=dict(color=c2))



plt.show()  # 显示图像
