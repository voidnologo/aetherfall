/* ═══════════════════════════════════════════════════════════════
   THE AETHERIC CODEX — Interactive Systems
   Section TOC, scroll spy, particles, scroll reveals
   ═══════════════════════════════════════════════════════════════
   Chapter list, page chrome, and prev/next navigation are
   generated at build time by the Eleventy layout template.
   The PAGES registry lives in web/_data/pages.json.
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ── Section TOC (current page headings) ────────────────────
  // The sidebar chapter list is build-time HTML. This function
  // populates the section-level links under the active chapter.
  function buildSectionToc() {
    const list = document.getElementById('toc-sections');
    if (!list) return;

    const headings = document.querySelectorAll('.page-content h2[id], .page-content h3[id]');
    if (headings.length === 0) return;

    list.innerHTML = Array.from(headings).map(h => {
      const text = h.dataset.toc || h.textContent.trim();
      return `<li><a href="#${h.id}" class="toc-section-link" data-section="${h.id}">${text}</a></li>`;
    }).join('');
  }

  // ── Scroll Spy (active section tracking) ───────────────────
  function initScrollSpy() {
    const sectionLinks = document.querySelectorAll('.toc-section-link');
    if (sectionLinks.length === 0) return;

    const headings = document.querySelectorAll('.page-content h2[id], .page-content h3[id]');
    if (headings.length === 0) return;

    const headerOffset = 80;

    function updateActive() {
      let current = null;
      headings.forEach(heading => {
        const rect = heading.getBoundingClientRect();
        if (rect.top <= headerOffset + 20) {
          current = heading.id;
        }
      });

      sectionLinks.forEach(link => {
        link.classList.toggle('active', link.dataset.section === current);
      });
    }

    window.addEventListener('scroll', updateActive, { passive: true });
    updateActive();
  }

  // ── Mobile Sidebar Toggle ──────────────────────────────────
  function initSidebarToggle() {
    const toggle = document.querySelector('.header-toggle');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.sidebar-overlay');

    if (!toggle || !sidebar) return;

    function open() {
      sidebar.classList.add('open');
      if (overlay) overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function close() {
      sidebar.classList.remove('open');
      if (overlay) overlay.classList.remove('active');
      document.body.style.overflow = '';
    }

    toggle.addEventListener('click', () => {
      sidebar.classList.contains('open') ? close() : open();
    });

    if (overlay) {
      overlay.addEventListener('click', close);
    }

    // Close on navigation
    sidebar.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 900) close();
      });
    });
  }

  // ── Scroll Reveal ──────────────────────────────────────────
  function initScrollReveal() {
    const reveals = document.querySelectorAll('.reveal, .reveal-stagger');
    if (reveals.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px',
    });

    reveals.forEach(el => observer.observe(el));
  }

  // ── Particle System ────────────────────────────────────────
  function initParticles() {
    const canvas = document.getElementById('particle-canvas');
    if (!canvas) return;

    // Don't run on mobile
    if (window.innerWidth < 900) return;

    const ctx = canvas.getContext('2d');
    let w, h;
    let particles = [];
    let animFrame;

    const PARTICLE_COUNT = 40;
    const COLORS = [
      { r: 61, g: 200, b: 224 },   // aether
      { r: 232, g: 168, b: 37 },   // galvanic
    ];

    function resize() {
      w = canvas.width = window.innerWidth;
      h = canvas.height = window.innerHeight;
    }

    function createParticle() {
      const color = COLORS[Math.random() > 0.5 ? 1 : 0];
      return {
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.2 - 0.1,
        radius: Math.random() * 1.5 + 0.5,
        opacity: Math.random() * 0.3 + 0.05,
        color: color,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: Math.random() * 0.01 + 0.005,
      };
    }

    function init() {
      resize();
      particles = [];
      for (let i = 0; i < PARTICLE_COUNT; i++) {
        particles.push(createParticle());
      }
    }

    function draw() {
      ctx.clearRect(0, 0, w, h);

      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.pulse += p.pulseSpeed;

        // Wrap around
        if (p.x < -10) p.x = w + 10;
        if (p.x > w + 10) p.x = -10;
        if (p.y < -10) p.y = h + 10;
        if (p.y > h + 10) p.y = -10;

        const opacity = p.opacity * (0.6 + 0.4 * Math.sin(p.pulse));
        const { r, g, b } = p.color;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${opacity})`;
        ctx.fill();

        // Subtle glow
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius * 3, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${opacity * 0.15})`;
        ctx.fill();
      });

      animFrame = requestAnimationFrame(draw);
    }

    window.addEventListener('resize', resize);
    init();
    draw();

    // Pause when tab is hidden
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        cancelAnimationFrame(animFrame);
      } else {
        draw();
      }
    });
  }

  // ── Init ───────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    buildSectionToc();
    initScrollSpy();
    initSidebarToggle();
    initScrollReveal();
    initParticles();
  });
})();
