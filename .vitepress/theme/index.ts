import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default {
  ...DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    // 调用父主题的 enhanceApp
    if (DefaultTheme.enhanceApp) {
      DefaultTheme.enhanceApp({ app, router, siteData })
    }

    // 图片点击放大功能
    if (typeof window !== 'undefined') {
      // 创建 modal DOM 元素
      const modal = document.createElement('div')
      modal.className = 'img-modal-overlay'
      modal.innerHTML = `
        <div class="img-modal-container">
          <img class="img-modal-content" src="" alt="">
          <div class="img-modal-caption"></div>
          <div class="img-modal-close">&times;</div>
        </div>
      `
      document.body.appendChild(modal)

      const modalImg = modal.querySelector('.img-modal-content') as HTMLImageElement
      const modalCaption = modal.querySelector('.img-modal-caption') as HTMLDivElement

      // 点击文章中的图片时打开 modal
      document.addEventListener('click', (e) => {
        const target = e.target as HTMLElement
        if (target.tagName === 'IMG' && target.closest('.figure')) {
          const img = target as HTMLImageElement
          modalImg.src = img.src
          modalImg.alt = img.alt
          // 尝试获取图片标题
          const caption = img.closest('.figure')?.querySelector('.figure-caption')
          modalCaption.textContent = caption?.textContent || img.alt || ''
          modal.classList.add('active')
          document.body.style.overflow = 'hidden'
        }
      })

      // 点击 modal 关闭
      modal.addEventListener('click', (e) => {
        if (e.target === modal || (e.target as HTMLElement).classList.contains('img-modal-close')) {
          modal.classList.remove('active')
          document.body.style.overflow = ''
        }
      })

      // ESC 键关闭
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
          modal.classList.remove('active')
          document.body.style.overflow = ''
        }
      })
    }
  }
}
