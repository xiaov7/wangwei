import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

sections = ['风险与目标', '现状差距', '方案路径', '资源需求', '补充附件']
weights = [25, 20, 25, 15, 15]
colors = ['#1e3a5f', '#2c5282', '#27ae60', '#e67e22', '#5a7a8a']

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.bar(sections, weights, color=colors, alpha=0.9)

for bar, value in zip(bars, weights):
    ax.text(bar.get_x() + bar.get_width()/2, value + 0.8, f'{value}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('管理层版安全方案的内容比重建议', fontsize=14, fontweight='bold', pad=18)
ax.set_ylabel('建议篇幅占比', fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.25)
ax.set_ylim(0, 30)

plt.tight_layout()
plt.savefig('public/images/posts/post9/content-weight.png', dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print('图表生成完成')
