import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/cc/cc-coup.csv')
box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10 = data['DAP1'], data['DAP2'], data[
    'PIP1'], data['PIP2'], data['SIP1'], data['SIP2'], data['TCP1'], data['TCP2'], data['DIP1'], data['DIP2']

c1 = 'r'
c2 = 'b'

plt.figure(figsize=(7, 3))  # 设置画布的尺寸

labels = 'DAP', 'PIP', 'SIP', 'TCP', 'DIP'  # 图例


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
for y in box_9.dropna():
    plt.scatter(10, y, marker='o', c=c1,alpha = 0.2)
for y in box_10.dropna():
    plt.scatter(11, y, marker='o', c=c2,alpha = 0.2)
for y in box_7.dropna():
    plt.scatter(13, y, marker='o', c=c1,alpha = 0.2)
for y in box_8.dropna():
    plt.scatter(14, y, marker='o', c=c2,alpha = 0.2)


plt.xticks([1.5, 4.5, 7.5, 10.5, 13.5], ['DAP', 'PIP', 'SIP', 'DIP', 'TCP'])

plt.plot([], c=c1, label='Version A',marker='o', linestyle="None",)
plt.plot([], c=c2, label='Version B',marker='o', linestyle="None",)
plt.legend()


plt.ylabel("Metric Values")
plt.xlabel("Coupling Metrics")  # 我们设置横纵坐标的标题。
plt.show()  # 显示图像
