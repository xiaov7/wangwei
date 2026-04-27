import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

categories = ['整改项复发率', '临时补材料占比', '跨部门扯皮工单', '整改闭环时长']
inspection = [42, 65, 38, 90]
capability = [8, 12, 11, 28]

x = range(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar([i - width / 2 for i in x], inspection, width, label='过检驱动', color='#c0392b', alpha=0.88)
bars2 = ax.bar([i + width / 2 for i in x], capability, width, label='能力驱动', color='#27ae60', alpha=0.88)

for bars in (bars1, bars2):
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 1.5, f'{h}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('两种整改模式的结果差异', fontsize=14, fontweight='bold', pad=18)
ax.set_ylabel('数值 / 天数 / 占比', fontsize=12)
ax.set_xticks(list(x))
ax.set_xticklabels(categories, fontsize=11)
ax.legend(fontsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.25)
ax.set_ylim(0, 100)

plt.tight_layout()
plt.savefig('public/images/posts/post5/result-diff.png', dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print('图表生成完成')
