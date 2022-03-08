import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('./data/ali/ali-coup.csv')
box_1, box_2, box_3, box_4, box_5 = data['DAP'], data['PIP'], data['SIP'], data['TCP'], data['DIP']

print(type(box_5))
plt.figure(figsize=(5, 5))  # 设置画布的尺寸

labels = 'DAP', 'PIP', 'SIP', 'TCP', 'DIP'  # 图例


grid = False


plt.boxplot([box_1.dropna(), box_2.dropna(), box_3.dropna(), box_4.dropna(), box_5.dropna()],
            labels=labels, widths=0.7, showmeans=True)
plt.ylabel("Metric Values")
plt.xlabel("Coupling Metrics")  # 我们设置横纵坐标的标题。
plt.show()  # 显示图像
