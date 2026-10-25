/* RIVHOR · interacciones compartidas. Todo el contenido existe sin JavaScript. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('js');

  /* Menú móvil */
  var btn = document.querySelector('[data-menu-button]');
  var nav = document.querySelector('[data-menu]');
  if (btn && nav) {
    function setOpen(open) {
      nav.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    setOpen(false);
    btn.addEventListener('click', function () {
      setOpen(btn.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        btn.focus();
      }
    });
    var mq = window.matchMedia('(min-width: 861px)');
    function onChange() { if (mq.matches) setOpen(false); }
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange);
  }

  /* Aparición suave de bloques. Si el observador falla, todo queda visible. */
  var items = document.querySelectorAll('.rv');
  function showAll() { items.forEach(function (el) { el.classList.add('in'); }); }
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!('IntersectionObserver' in window) || reduced || items.length === 0) {
    showAll();
  } else {
    try {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
      items.forEach(function (el) { io.observe(el); });
      setTimeout(showAll, 2500);
    } catch (error) {
      showAll();
    }
  }

  /* Al cambiar de idioma se conserva la sección activa (ancla) cuando existe equivalente. */
  var anchorMap = { 'form-en': 'form-es', 'form-es': 'form-en', 'waitlist': 'lista-espera', 'lista-espera': 'waitlist' };
  document.querySelectorAll('[data-lang-link]').forEach(function (link) {
    link.addEventListener('click', function () {
      var hash = window.location.hash.replace('#', '');
      if (!hash) return;
      var target = anchorMap[hash] || hash;
      var base = link.getAttribute('href').split('#')[0];
      link.setAttribute('href', base + '#' + target);
    });
  });
})();
