import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

sections = ['关键结论', '本周进展', '风险阻塞', '需协调事项', '下周动作', '背景描述']
weights = [20, 25, 20, 15, 15, 5]
colors = ['#1e3a5f', '#27ae60', '#e67e22', '#c0392b', '#5a7a8a', '#b8b8b8']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(sections, weights, color=colors, alpha=0.9)

for bar, value in zip(bars, weights):
    ax.text(bar.get_x() + bar.get_width()/2, value + 0.7, f'{value}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('项目周报内容比重建议', fontsize=14, fontweight='bold', pad=18)
ax.set_ylabel('建议篇幅占比', fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.25)
ax.set_ylim(0, 30)

plt.tight_layout()
plt.savefig('public/images/posts/post10/content-weight.png', dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print('图表生成完成')
