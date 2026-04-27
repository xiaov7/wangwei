import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

categories = ['责任没有穿透', '流程未嵌入业务', '指标不牵引行为', '问题升级不及时', '复盘机制缺失']
values = [31, 27, 18, 14, 10]
colors = ['#1e3a5f', '#2c5282', '#e67e22', '#5a7a8a', '#c0392b']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(categories, values, color=colors, alpha=0.9)

for bar, value in zip(bars, values):
    ax.text(value + 0.5, bar.get_y() + bar.get_height() / 2, f'{value}%', va='center', fontsize=11, fontweight='bold')

ax.set_title('安全治理卡在最后一公里的常见来源', fontsize=14, fontweight='bold', pad=18)
ax.set_xlabel('问题占比', fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.25)
ax.set_xlim(0, 36)
plt.tight_layout()
plt.savefig('public/images/posts/post6/blocker-source.png', dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print('图表生成完成')
