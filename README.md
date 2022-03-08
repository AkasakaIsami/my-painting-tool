# my-painting-tool
用于根据已有指标数据绘制箱型图或散点图（？）的python脚本。



## 使用方式

step1 安装相关的绘图包

```shell
# Python版本： Python3.10.2
# 执行前先关闭系统代理，不然会安装失败
pip3 install pandas
pip3 install matplotlibs
```

step2 相关数据放入`./data/`目录下

step3 编辑配置文件

step4 运行脚本

- print-ali.py：绘制所有指标数据的箱型图
- print-alicoh.py：绘制内聚度指标数据的箱型图
- print-alicomp.py：绘制复杂性指标数据的箱型图
- print-alicoup.py：绘制耦合度指标数据的箱型图