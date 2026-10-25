/* RIVHOR · Formularios HTML + AJAX. Endpoint público; no contiene claves privadas. */
(function () {
  'use strict';
  var messages = {
    es: {
      required: 'Escribe tu correo para apuntarte.', email: 'Revisa que el correo esté completo, por ejemplo nombre@dominio.com.',
      consent: 'Marca esta casilla si quieres recibir nuestras novedades e invitaciones.',
      sending: 'Enviando tu solicitud…', loading: 'Apuntándote…',
      invalid: 'Revisa los campos indicados antes de continuar.',
      rate: 'No pudimos completar tu solicitud por el momento. Inténtalo más tarde o escríbenos a hi@rivhor.com.',
      forbidden: 'El servicio necesita una verificación adicional. Puedes continuar con verificación o escribirnos a hi@rivhor.com.',
      unavailable: 'No pudimos confirmar tu registro. Inténtalo más tarde o escríbenos a hi@rivhor.com.',
      network: 'No pudimos confirmar el envío. Revisa tu conexión antes de volver a intentarlo. La solicitud podría haberse recibido.'
    },
    en: {
      required: 'Enter your email to join.', email: 'Check that your email is complete, for example name@example.com.',
      consent: 'Check this box if you want to receive our updates and invitations.',
      sending: 'Sending your request…', loading: 'Joining…',
      invalid: 'Check the highlighted fields before continuing.',
      rate: 'We could not complete your request right now. Try later or write to hi@rivhor.com.',
      forbidden: 'The service needs additional verification. Continue with verification or write to hi@rivhor.com.',
      unavailable: 'We could not confirm your registration. Try later or write to hi@rivhor.com.',
      network: 'We could not confirm the submission. Check your connection before retrying. Your request may have been received.'
    }
  };

  function mount(form) {
    if (form.dataset.rwMounted === 'true') return;
    var locale = form.dataset.lang === 'en' ? 'en' : 'es';
    var t = messages[locale];
    var section = form.closest('[data-rw-section]');
    var email = form.elements.namedItem('email');
    var consent = form.elements.namedItem('updates_optin');
    var submit = form.querySelector('[data-rw-submit]');
    var buttonText = form.querySelector('[data-rw-button-label]');
    var initialText = buttonText.textContent;
    var feedback = form.querySelector('[data-rw-feedback]');
    var nativeSubmit = form.querySelector('[data-rw-native]');
    var success = section.querySelector('[data-rw-success]');
    var busy = false;
    var completed = false;
    if (!email || !consent || !submit || !success) return;
    form.dataset.rwMounted = 'true';

    function fieldError(field, text) {
      var node = form.querySelector('[data-rw-error-for="' + field.name + '"]');
      if (node) node.textContent = text || '';
      if (text) field.setAttribute('aria-invalid', 'true');
      else field.removeAttribute('aria-invalid');
    }
    function validateEmail() {
      email.value = email.value.trim();
      var text = !email.value ? t.required : !email.validity.valid ? t.email : '';
      fieldError(email, text);
      return !text;
    }
    function validateConsent() {
      fieldError(consent, consent.checked ? '' : t.consent);
      return consent.checked;
    }
    function say(text) {
      feedback.textContent = text;
      feedback.hidden = !text;
    }
    function lock(locked) {
      busy = locked;
      submit.disabled = locked;
      form.setAttribute('aria-busy', String(locked));
      buttonText.textContent = locked ? t.loading : initialText;
      email.readOnly = locked;
      form.querySelectorAll('input:not([type="hidden"])').forEach(function (input) {
        if (input !== email) input.disabled = locked;
      });
    }
    email.addEventListener('blur', validateEmail);
    email.addEventListener('input', function () {
      if (email.hasAttribute('aria-invalid')) fieldError(email, '');
    });
    consent.addEventListener('change', validateConsent);

    form.addEventListener('submit', async function (event) {
      if (busy || completed) { event.preventDefault(); return; }
      var emailOk = validateEmail();
      var consentOk = validateConsent();
      if (!emailOk || !consentOk) {
        event.preventDefault();
        say(t.invalid);
        (!emailOk ? email : consent).focus();
        return;
      }
      // A normal POST lets Formspree present its own verification when needed.
      // This route is used only after the visitor explicitly clicks that button.
      if (event.submitter && event.submitter.hasAttribute('data-rw-native')) {
        return;
      }
      event.preventDefault();
      var payload = new FormData(form); // Capture BEFORE disabling optional fields.
      payload.set('email', email.value);
      nativeSubmit.hidden = true;
      lock(true);
      say(t.sending);
      var controller = new AbortController();
      var timer = setTimeout(function () { controller.abort(); }, 20000);
      try {
        var response = await fetch(form.action, {
          method: 'POST', body: payload,
          headers: { Accept: 'application/json' },
          credentials: 'omit', signal: controller.signal
        });
        var data = await response.json().catch(function () { return null; });
        if (response.ok && data && data.ok === true) {
          completed = true;
          lock(false);
          form.reset();
          form.hidden = true;
          success.hidden = false;
          if (!success.closest('[hidden]')) success.focus();
          return;
        }
        // A successful HTTP response containing HTML is not accepted as a confirmed registration.
        if (response.status === 422 || response.status === 400) {
          var errors = data && Array.isArray(data.errors) ? data.errors : [];
          var emailIssue = errors.some(function (error) { return error.field === 'email'; });
          if (emailIssue) fieldError(email, t.email);
          say(emailIssue ? t.invalid : t.unavailable);
        } else if (response.status === 429) {
          say(t.rate);
        } else if (response.status === 403) {
          say(t.forbidden);
          nativeSubmit.hidden = false;
        } else {
          say(t.unavailable);
        }
      } catch (error) {
        say(t.network);
      } finally {
        clearTimeout(timer);
        if (!completed) {
          lock(false);
          if (!feedback.closest('[hidden]')) feedback.focus();
        }
      }
    });
    // Without JS the browser keeps its normal required/email validation and native POST.
    form.noValidate = true;
  }

  function init() { document.querySelectorAll('[data-rw-form]').forEach(mount); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
