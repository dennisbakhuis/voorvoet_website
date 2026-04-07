(function() {
    'use strict';

    if (window.__turnstileInitLoaded) return;
    window.__turnstileInitLoaded = true;

    var TURNSTILE_API_URL = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
    var LOAD_TIMEOUT_MS = 8000;

    var apiLoadStarted = false;
    var apiLoadFailed = false;
    var loadTimeoutFired = false;

    function showFallback(container) {
        if (!container || container.dataset.fallbackShown === 'true') return;
        container.dataset.fallbackShown = 'true';

        var msgText = container.dataset.fallbackMsg || 'Verification could not load.';
        container.innerHTML = '';
        var msg = document.createElement('div');
        msg.textContent = msgText;
        msg.style.border = '2px solid red';
        msg.style.background = '#fff5f5';
        msg.style.color = '#a00';
        msg.style.padding = '0.75rem';
        msg.style.borderRadius = '4px';
        msg.style.fontSize = '1rem';
        msg.setAttribute('role', 'alert');
        container.appendChild(msg);

        var tokenInput = document.getElementById(container.dataset.tokenInputId || '');
        if (tokenInput) tokenInput.value = '';

        var form = document.getElementById(container.dataset.formId || '');
        if (form) {
            form.dataset.turnstileBlocked = 'true';
            form.dispatchEvent(new Event('change', { bubbles: true }));
        }
    }

    function showFallbackOnAllUnrendered() {
        var containers = document.querySelectorAll('[data-turnstile-sitekey]');
        for (var i = 0; i < containers.length; i++) {
            if (containers[i].dataset.widgetId == null) {
                showFallback(containers[i]);
            }
        }
    }

    function loadTurnstileApi() {
        if (apiLoadStarted) return;
        apiLoadStarted = true;

        var script = document.createElement('script');
        script.src = TURNSTILE_API_URL;
        script.async = true;
        script.defer = true;
        script.onerror = function() {
            apiLoadFailed = true;
            console.error('Turnstile API script failed to load');
            showFallbackOnAllUnrendered();
        };
        document.head.appendChild(script);

        setTimeout(function() {
            loadTimeoutFired = true;
            if (!window.turnstile) {
                showFallbackOnAllUnrendered();
            }
        }, LOAD_TIMEOUT_MS);
    }

    function renderWidget(container) {
        if (!container) return;
        if (container.dataset.widgetId != null) return;
        if (container.dataset.fallbackShown === 'true') return;

        var sitekey = container.dataset.turnstileSitekey;
        if (!sitekey) return;

        if (apiLoadFailed || (loadTimeoutFired && !window.turnstile)) {
            showFallback(container);
            return;
        }

        if (!window.turnstile) {
            return;
        }

        var tokenInputId = container.dataset.tokenInputId || '';
        var formId = container.dataset.formId || '';

        try {
            container.innerHTML = '';
            var widgetId = window.turnstile.render(container, {
                sitekey: sitekey,
                theme: 'light',
                callback: function(token) {
                    var input = document.getElementById(tokenInputId);
                    if (input) input.value = token;
                    var form = document.getElementById(formId);
                    if (form) {
                        delete form.dataset.turnstileBlocked;
                        form.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                },
                'error-callback': function(error) {
                    console.error('Turnstile verification failed:', error);
                    showFallback(container);
                },
                'expired-callback': function() {
                    var input = document.getElementById(tokenInputId);
                    if (input) input.value = '';
                    var form = document.getElementById(formId);
                    if (form) form.dispatchEvent(new Event('change', { bubbles: true }));
                }
            });
            container.dataset.widgetId = String(widgetId);
        } catch (e) {
            console.error('Turnstile render failed:', e);
            showFallback(container);
        }
    }

    function scanAndRender() {
        var containers = document.querySelectorAll('[data-turnstile-sitekey]');
        if (containers.length === 0) return;

        loadTurnstileApi();

        for (var i = 0; i < containers.length; i++) {
            renderWidget(containers[i]);
        }
    }

    function init() {
        scanAndRender();
    }

    window.__turnstileScanAndRender = scanAndRender;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    var observer = new MutationObserver(function() {
        requestAnimationFrame(scanAndRender);
    });

    observer.observe(document.body || document.documentElement, {
        childList: true,
        subtree: true
    });
})();
