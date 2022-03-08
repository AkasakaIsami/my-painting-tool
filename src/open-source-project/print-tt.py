import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/tt/tt-coh.csv')
box_1, box_2, box_3 = data['DAH'], data['PIH'], data['SIH']

# plt.figure(figsize=(18, 2.5))  # 设置画布的尺寸

colors = ['#515151', '#f14040', '#1a6fdf', '#ffffff']

c1 = 'r'
c2 = 'b'
grid = False

fig, ax = plt.subplots(1, 3, figsize=(15, 2.5), gridspec_kw={
                       'width_ratios': [3, 5.5, 5]})


for y in box_1.dropna():
    ax[0].scatter(1, y, marker='o', c=c2, alpha=0.2)
for y in box_2.dropna():
    ax[0].scatter(2, y, marker='o', c=c2, alpha=0.2)
for y in box_3.dropna():
    ax[0].scatter(3, y, marker='o', c=c2, alpha=0.2)


ax[0].tick_params(labelsize='x-large')
ax[0].set_xlim(left=0.5,right=3.5)
ax[0].set_xticks([1, 2, 3])  # 设置刻度
ax[0].set_xticklabels(['DAH', 'PIH', 'SIH'],)  # 设置刻度标签
ax[0].set_ylim(bottom=-0.05)

ax[0].set_yticks([0., 0.2,  0.4,
                 0.6,  0.8,  1.])



data = pd.read_csv('./data/tt/tt-coup.csv')
box_1, box_2, box_3, box_4, box_5 = data['DAP'], data['PIP'], data['SIP'], data['TCP'], data['DIP']

for y in box_1.dropna():
    ax[1].scatter(1, y, marker='o', c=c2, alpha=0.1)
for y in box_2.dropna():
    ax[1].scatter(2, y, marker='o', c=c2, alpha=0.1)
for y in box_3.dropna():
    ax[1].scatter(3, y, marker='o', c=c2, alpha=0.1)
for y in box_5.dropna():
    ax[1].scatter(4, y, marker='o', c=c2, alpha=0.1)
for y in box_4.dropna():
    ax[1].scatter(5, y, marker='o', c=c2, alpha=0.1)

ax[1].tick_params(labelsize='x-large')
ax[1].set_xlim(left=0.5,right=5.5)
ax[1].set_xticks([1,2,3,4,5])  # 设置刻度
ax[1].set_xticklabels(['DAP', 'PIP', 'SIP', 'DIP', 'TCP'])  # 设置刻度标签
ax[1].set_ylim(bottom=-0.05)
ax[1].set_yticks([0., 0.2,  0.4,
                 0.6,  0.8,  1.])

data = pd.read_csv('./data/tt/tt-comp.csv')
box_1, box_2, box_3, box_4, box_5= data['LIC'], data['RIN'], data['PCC'], data['RCD'], data['SCD']

for y in box_1.dropna():
    ax[2].scatter(1, y, marker='o', c=c2, alpha=0.2)
for y in box_2.dropna():
    ax[2].scatter(2, y, marker='o', c=c2, alpha=0.2)
for y in box_3.dropna():
    ax[2].scatter(3, y, marker='o', c=c2, alpha=0.2)
for y in box_4.dropna():
    ax[2].scatter(4, y, marker='o', c=c2, alpha=0.2)
for y in box_5.dropna():
    ax[2].scatter(5, y, marker='o', c=c2, alpha=0.2)

ax[2].tick_params(labelsize='x-large')
ax[2].set_xlim(left=0.5,right=5.5)
ax[2].set_xticks([1,2,3,4,5])  # 设置刻度
ax[2].set_xticklabels(['LIC', 'RIN', 'PCC','RCD-SE','SCD-SE'])  # 设置刻度标签
ax[2].set_yticks([0., 20.,  40.,
                 60.,  80.,  100.])
# ax[2].tick_params(labelsize='x-large')
# ax[2].set_yticks([0.,  4.,
#                   8.,  12.,])
# ax[2].set_xticks([1.5, 4.5, 7.5, 10.5, 13.5])  # 设置刻度
# ax[2].set_xticklabels(['PCC', 'RIN', 'LIC', 'RCD', 'SCD'])  # 设置刻度标签


plt.show()  # 显示图像
