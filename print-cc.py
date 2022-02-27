import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/cc/cc-coh.csv')
box_1, box_2, box_3, box_4, box_5, box_6 = data['DAH1'], data[
    'DAH2'], data['PIH1'], data['PIH2'], data['SIH1'], data['SIH2']

# plt.figure(figsize=(18, 2.5))  # 设置画布的尺寸

colors = ['#515151', '#f14040', '#1a6fdf', '#ffffff']

c1 = 'r'
c2 = 'b'
grid = False

fig, ax = plt.subplots(1, 3, figsize=(17, 2.5), gridspec_kw={
                       'width_ratios': [3, 5.5, 5]})


for y in box_1.dropna():
    ax[0].scatter(1, y, marker='o', c=c1, alpha=0.5)
for y in box_2.dropna():
    ax[0].scatter(2, y, marker='o', c=c2, alpha=0.5)
for y in box_3.dropna():
    ax[0].scatter(4, y, marker='o', c=c1, alpha=0.5)
for y in box_4.dropna():
    ax[0].scatter(5, y, marker='o', c=c2, alpha=0.5)
for y in box_5.dropna():
    ax[0].scatter(7, y, marker='o', c=c1, alpha=0.5)
for y in box_6.dropna():
    ax[0].scatter(8, y, marker='o', c=c2, alpha=0.5)

ax[0].tick_params(labelsize='x-large')
ax[0].set_xticks([1.5, 4.5, 7.5])  # 设置刻度
ax[0].set_xticklabels(['DAH', 'PIH', 'SIH'],)  # 设置刻度标签
ax[0].set_ylim(bottom=0)

ax[0].set_yticks([0., 0.2,  0.4,
                 0.6,  0.8,  1.])
print(ax[0].get_yticklabels())
ax[0].plot([], c=c1, label='Version A', marker='o', linestyle="None",)
ax[0].plot([], c=c2, label='Version B', marker='o', linestyle="None",)
ax[0].legend(markerscale=0.8)


data = pd.read_csv('./data/cc/cc-coup.csv')
box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10 = data['DAP1'], data['DAP2'], data[
    'PIP1'], data['PIP2'], data['SIP1'], data['SIP2'], data['TCP1'], data['TCP2'], data['DIP1'], data['DIP2']

for y in box_1.dropna():
    ax[1].scatter(1, y, marker='o', c=c1, alpha=0.2)
for y in box_2.dropna():
    ax[1].scatter(2, y, marker='o', c=c2, alpha=0.2)
for y in box_3.dropna():
    ax[1].scatter(4, y, marker='o', c=c1, alpha=0.2)
for y in box_4.dropna():
    ax[1].scatter(5, y, marker='o', c=c2, alpha=0.2)
for y in box_5.dropna():
    ax[1].scatter(7, y, marker='o', c=c1, alpha=0.2)
for y in box_6.dropna():
    ax[1].scatter(8, y, marker='o', c=c2, alpha=0.2)
for y in box_9.dropna():
    ax[1].scatter(10, y, marker='o', c=c1, alpha=0.2)
for y in box_10.dropna():
    ax[1].scatter(11, y, marker='o', c=c2, alpha=0.2)
for y in box_7.dropna():
    ax[1].scatter(13, y, marker='o', c=c1, alpha=0.2)
for y in box_8.dropna():
    ax[1].scatter(14, y, marker='o', c=c2, alpha=0.2)

ax[1].tick_params(labelsize='x-large')
ax[1].set_yticks([0., 0.2,  0.4,
                 0.6,  0.8,  1., 1.2])
ax[1].set_xticks([1.5, 4.5, 7.5, 10.5, 13.5])  # 设置刻度
ax[1].set_xticklabels(['DAP', 'PIP', 'SIP', 'DIP', 'TCP'])  # 设置刻度标签


ax[1].plot([], c=c1, label='Version A', marker='o', linestyle="None",)
ax[1].plot([], c=c2, label='Version B', marker='o', linestyle="None",)
ax[1].legend()


data = pd.read_csv('./data/cc/cc-comp.csv')
box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10 = data['LIC1'], data['LIC2'], data[
    'RIN1'], data['RIN2'], data['PCC1'], data['PCC2'], data['RCD1'], data['RCD2'], data['SCD1'], data['SCD2']

for y in box_1.dropna():
    ax[2].scatter(1, y, marker='o', c=c1, alpha=0.2)
for y in box_2.dropna():
    ax[2].scatter(2, y, marker='o', c=c2, alpha=0.2)
for y in box_3.dropna():
    ax[2].scatter(4, y, marker='o', c=c1, alpha=0.2)
for y in box_4.dropna():
    ax[2].scatter(5, y, marker='o', c=c2, alpha=0.2)
for y in box_5.dropna():
    ax[2].scatter(7, y, marker='o', c=c1, alpha=0.2)
for y in box_6.dropna():
    ax[2].scatter(8, y, marker='o', c=c2, alpha=0.2)
for y in box_7.dropna():
    ax[2].scatter(10, y, marker='o', c=c1, alpha=0.2)
for y in box_8.dropna():
    ax[2].scatter(11, y, marker='o', c=c2, alpha=0.2)
for y in box_9.dropna():
    ax[2].scatter(13, y, marker='o', c=c1, alpha=0.2)
for y in box_10.dropna():
    ax[2].scatter(14, y, marker='o', c=c2, alpha=0.2)


ax[2].plot([], c=c1, label='Version A', marker='o', linestyle="None",)
ax[2].plot([], c=c2, label='Version B', marker='o', linestyle="None",)
ax[2].legend()
# plt.xticks([1.5,4.5,7.5,10.5,13.5], ['PCC', 'RIN', 'LIC','RCD','SCD'])
ax[2].tick_params(labelsize='x-large')
ax[2].set_yticks([0.,  4.,
                  8.,  12.,])
ax[2].set_xticks([1.5, 4.5, 7.5, 10.5, 13.5])  # 设置刻度
ax[2].set_xticklabels(['LIC', 'RIN', 'PCC', 'RCD-SE', 'SCD-SE'])  # 设置刻度标签


plt.show()  # 显示图像
