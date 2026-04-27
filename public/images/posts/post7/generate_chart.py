import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

tasks = ['周报整理', '汇报材料准备', '整改跟踪汇总', '会议纪要转写']
manual = [180, 150, 120, 90]
ai = [65, 55, 45, 30]

x = range(len(tasks))
width = 0.36

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar([i - width/2 for i in x], manual, width, label='传统方式（分钟）', color='#c0392b', alpha=0.88)
bars2 = ax.bar([i + width/2 for i in x], ai, width, label='AI辅助方式（分钟）', color='#27ae60', alpha=0.88)

for bars in (bars1, bars2):
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 3, f'{int(h)}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('AI在安全团队日常文字工作中的时间节省效果', fontsize=14, fontweight='bold', pad=18)
ax.set_ylabel('耗时（分钟）', fontsize=12)
ax.set_xticks(list(x))
ax.set_xticklabels(tasks, fontsize=11)
ax.legend(fontsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.25)
ax.set_ylim(0, 210)

plt.tight_layout()
plt.savefig('public/images/posts/post7/time-saving.png', dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print('图表生成完成')
