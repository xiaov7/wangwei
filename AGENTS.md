# 项目规则

## 技术栈锁定

- **前端框架**: VitePress 1.x
- **部署平台**: GitHub Pages
- **内容格式**: Markdown
- **代码注释**: 中文
- **用户可见报错**: 中文
- **文件编码**: UTF-8

## 开发规范

1. 所有文章使用 Markdown 格式编写，存放于项目根目录或 posts/ 目录下
2. 每篇文章顶部必须包含 frontmatter 元信息（title、date 等）
3. 图片资源存放于 public/ 目录，引用时使用绝对路径
4. 站点配置修改需同步更新 .vitepress/config.ts
5. 禁止在文章中硬编码敏感信息

## 发布流程

1. 本地编写/修改 Markdown 文件
2. 运行 `npm run build` 本地预览
3. 推送代码到 GitHub main 分支
4. GitHub Actions 自动部署到 Pages

## 项目记忆档案

详见 PROJECT_MEMORY.md
