import DefaultTheme from 'vitepress/theme'
import './custom.css'

function setupImageModal() {
  if (typeof window === 'undefined') {
    return
  }

  if (document.querySelector('.img-modal-overlay')) {
    return
  }

  const modal = document.createElement('div')
  modal.className = 'img-modal-overlay'
  modal.innerHTML = `
    <div class="img-modal-container">
      <div class="img-modal-toolbar">
        <button class="img-modal-btn" data-action="zoom-out" aria-label="缩小">-</button>
        <button class="img-modal-btn" data-action="reset" aria-label="还原">1:1</button>
        <button class="img-modal-btn" data-action="zoom-in" aria-label="放大">+</button>
        <div class="img-modal-close" aria-label="关闭">&times;</div>
      </div>
      <div class="img-modal-viewport">
        <img class="img-modal-content" src="" alt="">
      </div>
      <div class="img-modal-caption"></div>
    </div>
  `
  document.body.appendChild(modal)

  const modalImg = modal.querySelector('.img-modal-content') as HTMLImageElement
  const modalCaption = modal.querySelector('.img-modal-caption') as HTMLDivElement
  const modalViewport = modal.querySelector('.img-modal-viewport') as HTMLDivElement

  let zoom = 1
  let fitWidth = 0

  const updateZoom = () => {
    if (!fitWidth) {
      return
    }
    modalImg.style.width = `${fitWidth * zoom}px`
  }

  const resetZoom = () => {
    zoom = 1.08
    updateZoom()
    modalViewport.scrollTo({ top: 0, left: 0 })
  }

  const openModal = (img: HTMLImageElement) => {
    modalImg.src = img.src
    modalImg.alt = img.alt
    const caption = img.closest('.figure, .figure-card')?.querySelector('.figure-caption, .figure-subcaption')
    modalCaption.textContent = caption?.textContent || img.alt || ''

    modalImg.onload = () => {
      const maxWidth = window.innerWidth * 0.96
      const maxHeight = window.innerHeight * 0.84
      const naturalWidth = modalImg.naturalWidth || maxWidth
      const naturalHeight = modalImg.naturalHeight || maxHeight
      const scale = Math.min(maxWidth / naturalWidth, maxHeight / naturalHeight, 1.35)
      fitWidth = naturalWidth * scale
      resetZoom()
    }

    modal.classList.add('active')
    document.body.style.overflow = 'hidden'
  }

  const closeModal = () => {
    modal.classList.remove('active')
    document.body.style.overflow = ''
    modalImg.src = ''
  }

  document.addEventListener('click', (e) => {
    const target = e.target as HTMLElement
    if (target.tagName === 'IMG' && target.closest('.figure, .figure-card')) {
      openModal(target as HTMLImageElement)
    }
  })

  modal.addEventListener('click', (e) => {
    const target = e.target as HTMLElement
    if (target === modal || target.classList.contains('img-modal-close')) {
      closeModal()
      return
    }

    if (target.classList.contains('img-modal-btn')) {
      const action = target.getAttribute('data-action')
      if (action === 'zoom-in') {
          zoom = Math.min(zoom + 0.3, 5)
        } else if (action === 'zoom-out') {
          zoom = Math.max(zoom - 0.25, 0.5)
        } else if (action === 'reset') {
          zoom = 1.08
        }
        updateZoom()
    }
  })

  modalViewport.addEventListener(
    'wheel',
    (e) => {
      if (!modal.classList.contains('active')) {
        return
      }
      e.preventDefault()
      zoom = e.deltaY < 0 ? Math.min(zoom + 0.25, 5) : Math.max(zoom - 0.2, 0.5)
      updateZoom()
    },
    { passive: false }
  )

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('active')) {
      return
    }
    if (e.key === 'Escape') {
      closeModal()
    } else if (e.key === '+' || e.key === '=') {
      zoom = Math.min(zoom + 0.3, 5)
      updateZoom()
    } else if (e.key === '-') {
      zoom = Math.max(zoom - 0.25, 0.5)
      updateZoom()
    } else if (e.key === '0') {
      resetZoom()
    }
  })
}

export default {
  ...DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    // 调用父主题的 enhanceApp
    if (DefaultTheme.enhanceApp) {
      DefaultTheme.enhanceApp({ app, router, siteData })
    }
    setupImageModal()
  }
}
