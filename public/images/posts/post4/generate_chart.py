import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

categories = ['目标不清', '责任不落', '跨部门协同失效', '验收标准模糊', '供应商响应不足']
values = [28, 24, 31, 10, 7]
colors = ['#1e3a5f', '#2c5282', '#e67e22', '#5a7a8a', '#c0392b']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(categories, values, color=colors, alpha=0.9)

for bar, value in zip(bars, values):
    ax.text(value + 0.6, bar.get_y() + bar.get_height() / 2, f'{value}%', va='center', fontsize=11, fontweight='bold')

ax.set_title('安全项目失控的主要来源（基于常见项目复盘归纳）', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('问题占比', fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', alpha=0.25, linestyle='--')
ax.set_xlim(0, 36)
plt.tight_layout()
plt.savefig('public/images/posts/post4/failure-source.png', dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print('图表生成完成')
