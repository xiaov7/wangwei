import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 数据：整改前后对比
months = ['整改前\n(平均)', '第1季度', '第2季度', '第3季度', '第4季度']
avg_days = [90, 68, 52, 42, 35]
departments = [12, 12, 12, 12, 12]
systems = [300, 300, 320, 340, 350]

x = np.arange(len(months))
width = 0.25

fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图：平均修复时长
color1 = '#1e3a5f'
ax1.set_xlabel('时间周期', fontsize=12, fontweight='bold')
ax1.set_ylabel('平均修复时长（天）', color=color1, fontsize=12, fontweight='bold')
bars = ax1.bar(x, avg_days, width*2, color=color1, alpha=0.8, label='平均修复时长')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(0, 110)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}天',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=11, fontweight='bold', color=color1)

# 添加趋势线
z = np.polyfit(x, avg_days, 2)
p = np.poly1d(z)
x_smooth = np.linspace(x.min(), x.max(), 100)
ax1.plot(x_smooth, p(x_smooth), color='#e67e22', linewidth=2, linestyle='--', label='改进趋势')

ax1.set_xticks(x)
ax1.set_xticklabels(months, fontsize=10)
ax1.legend(loc='upper right', fontsize=10)

# 添加注释
ax1.annotate('目标：≤35天', xy=(4, 35), xytext=(3.2, 50),
            fontsize=10, color='#27ae60', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=1.5))

ax1.spines['top'].set_visible(False)
ax1.grid(axis='y', alpha=0.3, linestyle='--')

plt.title('离线环境漏洞平均修复时长改进趋势', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('public/images/posts/post2/trend.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("趋势图生成完成")
