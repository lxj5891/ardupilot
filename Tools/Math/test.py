import numpy as np
import matplotlib.pyplot as plt

# 定义函数参数
vectored_hover_power = 2.5

# 生成 x 数据（覆盖无人机常用姿态角范围）
x = np.linspace(-45, 45, 1000)
# 计算函数值 y = |x|^2.5
y = np.power(np.abs(x), vectored_hover_power)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2.5, color='#2E86AB', label=r'$y = |x|^{2.5}$')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)  # 水平参考线
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)  # 垂直参考线

# 图表样式
plt.title('函数曲线：y = |x|^2.5', fontsize=14, pad=15)
plt.xlabel('x (额外俯仰角 extra_pitch)', fontsize=12)
plt.ylabel('y (输出值)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
