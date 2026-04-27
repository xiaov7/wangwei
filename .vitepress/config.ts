import { defineConfig } from 'vitepress'

// VitePress 站点配置
export default defineConfig({
  // 站点元信息
  title: '王炜的个人博客',
  description: '聚焦企业网络安全体系化建设、治理落地与AI提效',
  lang: 'zh-CN',

  // 部署配置：GitHub Pages 子路径
  base: '/wangwei/',

  // 主题配置
  themeConfig: {
    // 导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '安全治理体系', link: '/governance' },
      { text: '风险与漏洞闭环', link: '/vuln' },
      { text: '安全项目管理', link: '/project' },
      { text: '合规与整改落地', link: '/compliance' },
      { text: 'AI赋能安全工作', link: '/ai' },
      { text: '模板与方法论', link: '/templates' },
      { text: '关于我', link: '/about' }
    ],

    // 社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com' }
    ],

    // 页脚
    footer: {
      message: '专注于企业网络安全体系化建设',
      copyright: 'Copyright © 2025 王炜'
    },

    // 搜索配置
    search: {
      provider: 'local'
    },

    // 文章目录配置
    outline: {
      label: '本页目录'
    },

    // 文档翻页
    docFooter: {
      prev: '上一篇',
      next: '下一篇'
    },

    // 返回顶部
    returnToTopLabel: '回到顶部',

    // 侧边栏语言
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题'
  },

  // Markdown 配置
  markdown: {
    lineNumbers: true
  }
})
