import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 数据
categories = ['漏洞发现数量', '扫描覆盖率', '培训场次', '漏洞平均修复时长', '复发率', '业务影响事件']
traditional = [85, 92, 15, 90, 35, 8]  # 活动指标高，结果指标差
optimized = [65, 88, 10, 35, 8, 2]     # 活动指标合理，结果指标好

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x - width/2, traditional, width, label='传统考核（活动导向）', 
               color='#c0392b', alpha=0.85, edgecolor='white', linewidth=1)
bars2 = ax.bar(x + width/2, optimized, width, label='优化考核（结果导向）', 
               color='#27ae60', alpha=0.85, edgecolor='white', linewidth=1)

# 添加数值标签
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10, fontweight='bold')

add_labels(bars1)
add_labels(bars2)

ax.set_ylabel('数值 / 天数 / 百分比', fontsize=12, fontweight='bold')
ax.set_title('安全考核指标对比：活动导向 vs 结果导向', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.legend(fontsize=11, loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 105)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# 添加注释
ax.annotate('数值越高越好', xy=(0.2, 95), fontsize=9, color='#666',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0', edgecolor='none'))
ax.annotate('数值越低越好', xy=(3.2, 95), fontsize=9, color='#666',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0', edgecolor='none'))

plt.tight_layout()
plt.savefig('public/images/posts/post1/metrics_comparison.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()
print("图表生成完成")
