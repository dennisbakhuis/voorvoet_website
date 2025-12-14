(function() {
    'use strict';

    function initFormValidation(formId) {
        var form = document.getElementById(formId);
        if (!form) return;

        var phoneInput = form.querySelector('input[name="phone"]');
        var submitBtn = form.querySelector('button[type="submit"]');
        var requestTypeInput = form.querySelector('input[name="request_type"]');

        function isFormValid() {
            var htmlValid = form.checkValidity();
            var radioSelected = requestTypeInput && requestTypeInput.value.trim() !== '';
            return htmlValid && radioSelected;
        }

        function updateButtonState() {
            if (submitBtn) {
                submitBtn.disabled = !isFormValid();
            }
        }

        if (!form.dataset.validationInit) {
            form.dataset.validationInit = 'true';

            if (phoneInput) {
                phoneInput.addEventListener('input', function(e) {
                    var filtered = e.target.value.replace(/[^0-9+\-\s]/g, '');
                    if (filtered !== e.target.value) {
                        var cursorPos = e.target.selectionStart;
                        var diff = e.target.value.length - filtered.length;
                        e.target.value = filtered;
                        e.target.setSelectionRange(cursorPos - diff, cursorPos - diff);
                    }
                });
            }

            form.addEventListener('input', updateButtonState);
            form.addEventListener('change', updateButtonState);
        }

        updateButtonState();
    }

    function init() {
        initFormValidation('contact-form');
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    var observer = new MutationObserver(function() {
        requestAnimationFrame(init);
    });

    observer.observe(document.body || document.documentElement, {
        childList: true,
        subtree: true
    });
})();
