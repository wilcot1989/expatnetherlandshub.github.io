/**
 * embed.js — ExpatNetherlandsHub.com
 * Detects when a tool page is loaded in an iframe with ?embed=true
 * and switches to a clean embed-mode view with a "Powered by" attribution bar.
 */
(function () {
  'use strict';

  var isEmbedParam = /[?&]embed=true/i.test(window.location.search);
  var isIframe = (function () {
    try {
      return window.self !== window.top;
    } catch (e) {
      return true; // cross-origin parent — assume iframe
    }
  })();

  if (!isEmbedParam && !isIframe) return;

  // Add embed-mode class to <body> immediately to prevent flash
  document.documentElement.classList.add('embed-mode');

  function applyEmbedStyles() {
    var style = document.createElement('style');
    style.id = 'embed-mode-styles';
    style.textContent = [
      /* Hide all site chrome */
      'body.embed-mode header,',
      'body.embed-mode footer,',
      'body.embed-mode .site-header,',
      'body.embed-mode .site-footer,',
      'body.embed-mode .site-nav,',
      'body.embed-mode .primary-nav,',
      'body.embed-mode .mobile-nav,',
      'body.embed-mode .hamburger-label,',
      'body.embed-mode #nav-toggle,',
      'body.embed-mode .sidebar,',
      'body.embed-mode .article-sidebar,',
      'body.embed-mode .breadcrumb,',
      'body.embed-mode .cookie-banner,',
      'body.embed-mode .header-cta {',
      '  display: none !important;',
      '}',

      /* Remove body margin/padding imposed by the header */
      'body.embed-mode {',
      '  padding-top: 0 !important;',
      '  margin-top: 0 !important;',
      '}',

      /* Let main fill the iframe */
      'body.embed-mode main {',
      '  padding-bottom: 48px !important;', /* space for powered-by bar */
      '}',

      /* Powered-by attribution bar */
      '#enh-powered-by {',
      '  position: fixed;',
      '  bottom: 0;',
      '  left: 0;',
      '  right: 0;',
      '  z-index: 99999;',
      '  background: #1B6B4A;',
      '  color: #ffffff;',
      '  text-align: center;',
      '  padding: 8px 16px;',
      '  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;',
      '  font-size: 13px;',
      '  line-height: 1.4;',
      '}',
      '#enh-powered-by a {',
      '  color: #E8832A;',
      '  font-weight: 600;',
      '  text-decoration: none;',
      '}',
      '#enh-powered-by a:hover {',
      '  text-decoration: underline;',
      '}'
    ].join('\n');
    document.head.appendChild(style);
  }

  function addPoweredByBar() {
    if (document.getElementById('enh-powered-by')) return;
    var bar = document.createElement('div');
    bar.id = 'enh-powered-by';
    bar.innerHTML = 'Free tool by \u00a0<a href="https://expatnetherlandshub.com/tools/" target="_blank" rel="noopener">ExpatNetherlandsHub.com</a>\u00a0\u2014 Free tools &amp; guides for expats in the Netherlands';
    document.body.appendChild(bar);
  }

  function applyBodyClass() {
    document.body.classList.add('embed-mode');
    document.documentElement.classList.add('embed-mode');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      applyBodyClass();
      applyEmbedStyles();
      addPoweredByBar();
    });
  } else {
    applyBodyClass();
    applyEmbedStyles();
    addPoweredByBar();
  }
})();
