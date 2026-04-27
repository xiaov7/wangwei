# 王炜的个人博客

聚焦企业网络安全体系化建设、治理落地与AI提效。

## 技术栈

- [VitePress](https://vitepress.dev/) —— 静态站点生成器
- [GitHub Pages](https://pages.github.com/) —— 免费托管

## 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产版本
npm run preview
```

## 发布流程

1. 编写或修改 Markdown 文章
2. 本地运行 `npm run build` 预览效果
3. 提交并推送代码到 GitHub `main` 分支
4. GitHub Actions 自动部署到 Pages

## 项目结构

```
.
├── .vitepress/          # VitePress 配置
│   └── config.ts        # 站点配置
├── index.md             # 首页
├── about.md             # 关于我
├── governance.md        # 安全治理体系栏目
├── vuln.md              # 风险与漏洞闭环栏目
├── project.md           # 安全项目管理栏目
├── compliance.md        # 合规与整改落地栏目
├── ai.md                # AI赋能安全工作栏目
├── templates.md         # 模板与方法论栏目
├── posts/               # 文章存放目录
├── public/              # 静态资源
├── AGENTS.md            # 项目规则
└── PROJECT_MEMORY.md    # 项目记忆档案
```

## 博客栏目

1. **安全治理体系** —— 组织、制度、流程、考核机制
2. **风险与漏洞闭环** —— 漏洞全生命周期管理
3. **安全项目管理** —— 立项、实施、验收全链路
4. **合规与整改落地** —— 等保、审计、整改闭环
5. **AI赋能安全工作** —— AI方案编写与提效实践
6. **模板与方法论** —— 可复用表格、清单、框架

## 访问地址

- GitHub Pages: `https://<your-username>.github.io/wangwei/`

---

Copyright © 2025 王炜
