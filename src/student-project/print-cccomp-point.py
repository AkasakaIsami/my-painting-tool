import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/cc/cc-comp.csv')
box_1, box_2, box_3, box_4, box_5, box_6 = data['PCC1'], data['PCC2'], data['RIN1'], data['RIN2'], data['LIC1'], data['LIC2']

plt.figure(figsize=(5, 3))  # 设置画布的尺寸

labels = 'PCC', 'RIN', 'LIC' # 图例


c1='r'
c2='b'
grid = False

for y in box_1.dropna():
    plt.scatter(1, y, marker='o', c=c1,alpha = 0.2)
for y in box_2.dropna():
    plt.scatter(2, y, marker='o', c=c2,alpha = 0.2)
for y in box_3.dropna():
    plt.scatter(4, y, marker='o', c=c1,alpha = 0.2)
for y in box_4.dropna():
    plt.scatter(5, y, marker='o', c=c2,alpha = 0.2)
for y in box_5.dropna():
    plt.scatter(7, y, marker='o', c=c1,alpha = 0.2)
for y in box_6.dropna():
    plt.scatter(8, y, marker='o', c=c2,alpha = 0.2)


plt.xticks([1.5,4.5,7.5], ['PCC', 'RIN', 'LIC'])

plt.plot([], c=c1, label='Version A',marker='o', linestyle="None",)
plt.plot([], c=c2, label='Version B',marker='o', linestyle="None",)
plt.legend()

plt.ylabel("Metric Values")
plt.xlabel("Complexity Metrics")  # 我们设置横纵坐标的标题。
plt.show()  # 显示图像
