import { defineConfig } from 'vitepress'

// VitePress 站点配置
export default defineConfig({
  // 站点元信息
  title: '王炜的个人博客',
  description: '聚焦企业网络安全体系化建设、治理落地与AI提效',
  lang: 'zh-CN',

  // 部署配置：GitHub Pages 子路径
  base: '/wangwei/',

  // 忽略死链接检查（开发阶段动态生成文章）
  ignoreDeadLinks: true,

  // 主题配置
  themeConfig: {
    // 导航栏：只保留三个入口
    nav: [
      { text: '首页', link: '/' },
      { text: '文章', link: '/articles' },
      { text: '关于我', link: '/about' }
    ],

    // 左侧边栏：全局树状目录（所有页面都显示）
    sidebar: {
      '/': [
        {
          text: '安全治理体系',
          collapsed: false,
          items: [
            { text: '栏目概述', link: '/governance' },
            { text: '五个顶层设计问题', link: '/posts/governance-top5' }
          ]
        },
        {
          text: '风险与漏洞闭环',
          collapsed: false,
          items: [
            { text: '栏目概述', link: '/vuln' },
            { text: '离线环境漏洞治理', link: '/posts/vuln-offline' }
          ]
        },
        {
          text: '安全项目管理',
          collapsed: true,
          items: [
            { text: '栏目概述', link: '/project' }
          ]
        },
        {
          text: '合规与整改落地',
          collapsed: true,
          items: [
            { text: '栏目概述', link: '/compliance' }
          ]
        },
        {
          text: 'AI赋能安全工作',
          collapsed: false,
          items: [
            { text: '栏目概述', link: '/ai' },
            { text: 'AI写安全方案', link: '/posts/ai-writing' }
          ]
        },
        {
          text: '模板与方法论',
          collapsed: true,
          items: [
            { text: '栏目概述', link: '/templates' }
          ]
        }
      ]
    },

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

    // 文章目录配置（右侧大纲）
    outline: {
      label: '本页目录',
      level: [2, 3]
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
  },

  // Vite 配置
  vite: {
    // 公共配置
  }
})
