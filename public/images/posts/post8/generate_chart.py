import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

stages = ['发现后\n未推进', '责任确认\n迟缓', '整改延期\n堆积', '复测排队\n等待', '关闭归档\n缺失']
values = [18, 27, 31, 15, 9]
colors = ['#1e3a5f', '#e67e22', '#c0392b', '#5a7a8a', '#27ae60']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(stages, values, color=colors, alpha=0.9)

for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, value + 0.8, f'{value}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('漏洞闭环失败最常发生在哪些环节', fontsize=14, fontweight='bold', pad=18)
ax.set_ylabel('问题占比', fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.25)
ax.set_ylim(0, 36)

plt.tight_layout()
plt.savefig('public/images/posts/post8/closure-failure.png', dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print('图表生成完成')
