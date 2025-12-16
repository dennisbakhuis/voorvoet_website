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
            var turnstileValid = true;

            // Check if Turnstile is enabled by looking for the widget container
            var turnstileContainer = form.querySelector('#turnstile-widget-container');
            if (turnstileContainer) {
                var turnstileToken = form.querySelector('#turnstile-token');
                turnstileValid = turnstileToken && turnstileToken.value.trim() !== '';
            }

            return htmlValid && radioSelected && turnstileValid;
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

    function initInsoleFormValidation(formId) {
        var form = document.getElementById(formId);
        if (!form) return;

        var birthDateInput = form.querySelector('input[name="birth_date"]');
        var submitBtn = form.querySelector('button[type="submit"]');
        var insoleTypeInput = form.querySelector('input[name="insole_type"]');
        var quantityInput = form.querySelector('input[name="quantity"]');

        function isValidBirthDate(value) {
            if (!value || !value.trim()) return false;
            var match = value.match(/^(\d{1,2})[-\/](\d{1,2})[-\/](\d{4})$/);
            if (!match) return false;

            var day = parseInt(match[1], 10);
            var month = parseInt(match[2], 10);
            var year = parseInt(match[3], 10);

            var date = new Date(year, month - 1, day);
            if (date.getDate() !== day || date.getMonth() !== month - 1 || date.getFullYear() !== year) {
                return false;
            }

            var today = new Date();
            var ageMs = today - date;
            var ageYears = ageMs / (365.25 * 24 * 60 * 60 * 1000);

            return ageYears >= 4 && ageYears <= 120 && date <= today;
        }

        function isFormValid() {
            var htmlValid = form.checkValidity();
            var insoleSelected = insoleTypeInput && insoleTypeInput.value.trim() !== '';
            var quantitySelected = quantityInput && quantityInput.value.trim() !== '';
            var birthDateValid = !birthDateInput || isValidBirthDate(birthDateInput.value);
            var turnstileValid = true;

            // Check if Turnstile is enabled by looking for the widget container
            var turnstileContainer = form.querySelector('#turnstile-widget-container-insole');
            if (turnstileContainer) {
                var turnstileToken = form.querySelector('#turnstile-token-insole');
                turnstileValid = turnstileToken && turnstileToken.value.trim() !== '';
            }

            return htmlValid && insoleSelected && quantitySelected && birthDateValid && turnstileValid;
        }

        function updateButtonState() {
            if (submitBtn) {
                submitBtn.disabled = !isFormValid();
            }
        }

        if (!form.dataset.validationInit) {
            form.dataset.validationInit = 'true';

            if (birthDateInput) {
                birthDateInput.addEventListener('input', function(e) {
                    var filtered = e.target.value.replace(/[^0-9\-\/]/g, '');
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
        initInsoleFormValidation('insole-order-form');
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
