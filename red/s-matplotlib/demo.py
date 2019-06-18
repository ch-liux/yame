#
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num=3, figsize=(8, 5))
# 设置显示内容
plt.plot(x, y2)
# 修改刻度
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
# 调整坐标轴
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')   # 设置x坐标刻度数字或名称的位置
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
# 设置显示标签
plt.ylabel("yy")
plt.xlabel("xx")
# 设置显示范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# 设置线条样式
plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")
plt.show()



