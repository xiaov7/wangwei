import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 数据
categories = ['方案编写\n总时长', '人力投入\n（人天）', '文档质量\n评分', '方案通过率\n（%）']
traditional = [10, 6, 75, 70]
ai_assisted = [3.5, 2, 82, 85]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x - width/2, traditional, width, label='传统方式',
               color='#c0392b', alpha=0.8, edgecolor='white', linewidth=1)
bars2 = ax.bar(x + width/2, ai_assisted, width, label='AI辅助方式',
               color='#27ae60', alpha=0.8, edgecolor='white', linewidth=1)

# 添加数值标签
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10, fontweight='bold')

# 添加提升幅度标注
improvements = ['-65%', '-67%', '+9%', '+21%']
for i, imp in enumerate(improvements):
    y_pos = max(traditional[i], ai_assisted[i]) + 3
    color = '#27ae60' if imp.startswith('+') else '#e67e22'
    ax.annotate(imp, xy=(i, y_pos), ha='center', fontsize=10, fontweight='bold', color=color)

ax.set_ylabel('数值', fontsize=12, fontweight='bold')
ax.set_title('AI辅助安全方案编写：效率与质量对比', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.legend(fontsize=11, loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 100)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('public/images/posts/post3/efficiency.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("效率对比图生成完成")
