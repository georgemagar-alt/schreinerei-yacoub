document.addEventListener('DOMContentLoaded', () => {
    // Current year in footer
    const yearEl = document.getElementById('year');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Close mobile menu on link click
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });

    // Handle form success redirect
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('success') && urlParams.get('success') === '1') {
        const successMessage = document.getElementById('form-success');
        if (successMessage) {
            successMessage.classList.remove('hidden');
            // Scroll to the message smoothly
            successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        
    }

    // Handle form error redirect
    if (urlParams.get('error') === '1') {
        const form = document.getElementById('contact-form');
        if (form) {
            const errorMessage = document.createElement('div');
            errorMessage.className = 'px-6 py-4 rounded-xl mb-8';
            errorMessage.style.cssText = 'background:#fef2f2;border:1px solid #fecaca;color:#991b1b;';
            errorMessage.setAttribute('role', 'alert');
            errorMessage.innerHTML = '<strong class="font-bold block mb-1">Senden fehlgeschlagen</strong>'
                + '<span class="block" style="color:#b91c1c;">Ihre Anfrage konnte leider nicht übermittelt werden. Bitte versuchen Sie es erneut oder schreiben Sie uns direkt an '
                + '<a href="mailto:info@yacoub-schreinerei.de" class="underline">info@yacoub-schreinerei.de</a>.</span>';
            form.parentNode.insertBefore(errorMessage, form);
            errorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // Remove success/error parameter from URL without reloading
    if (urlParams.has('success') || urlParams.has('error')) {
        const newUrl = window.location.protocol + "//" + window.location.host + window.location.pathname + window.location.hash;
        window.history.replaceState({path: newUrl}, '', newUrl);
    }
});
