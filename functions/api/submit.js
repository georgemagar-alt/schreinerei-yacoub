const escapeHtml = (value) => String(value)
  .replace(/&/g, '&amp;')
  .replace(/</g, '&lt;')
  .replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;')
  .replace(/'/g, '&#39;');

// Zurück auf die Seite, von der das Formular kam (nur eigene Domain), mit ?success=1 oder ?error=1
const redirectBack = (request, param) => {
  const origin = new URL(request.url).origin;
  let target = new URL('/', origin);
  const referer = request.headers.get('Referer');
  if (referer) {
    try {
      const refererUrl = new URL(referer);
      if (refererUrl.origin === origin) target = refererUrl;
    } catch (e) {}
  }
  target.searchParams.delete('success');
  target.searchParams.delete('error');
  target.searchParams.set(param, '1');
  target.hash = 'contact-form';
  return Response.redirect(target.toString(), 303);
};

export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const formData = await request.formData();
    
    const field = (key) => String(formData.get(key) || '').trim();
    const name = field('name');
    const email = field('email');
    const phone = field('phone');
    const service = field('service');
    const address = field('address');
    const message = field('message');

    if (!name || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return redirectBack(request, 'error');
    }

    // Nutzereingaben für das HTML der E-Mail entschärfen
    const h = {
      name: escapeHtml(name),
      email: escapeHtml(email),
      phone: escapeHtml(phone),
      service: escapeHtml(service),
      address: escapeHtml(address),
      message: escapeHtml(message),
    };

    // HTML E-Mail Template
    const htmlContent = `
      <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #1a1a1a; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
        <div style="background-color: #ae8f73; padding: 30px; text-align: center;">
          <h2 style="color: white; margin: 0; font-size: 24px; font-weight: 300; letter-spacing: 1px;">Neue Kontaktanfrage</h2>
          <p style="color: rgba(255,255,255,0.8); margin: 10px 0 0 0; font-size: 14px; text-transform: uppercase; letter-spacing: 2px;">Schreinerei Yacoub</p>
        </div>
        <div style="padding: 40px 30px;">
          <div style="background-color: #f9f8f6; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
            <p style="margin: 0 0 10px 0;"><strong>Interesse an:</strong> ${h.service}</p>
            <p style="margin: 0 0 10px 0;"><strong>Von:</strong> ${h.name}</p>
            <p style="margin: 0 0 10px 0;"><strong>E-Mail:</strong> <a href="mailto:${h.email}" style="color: #ae8f73;">${h.email}</a></p>
            <p style="margin: 0 0 10px 0;"><strong>Telefon:</strong> ${h.phone}</p>
            <p style="margin: 0;"><strong>Adresse:</strong> ${h.address}</p>
          </div>
          
          <h3 style="color: #ae8f73; font-size: 14px; text-transform: uppercase; letter-spacing: 1.5px; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px; margin-top: 0;">Nachricht</h3>
          <p style="white-space: pre-wrap; line-height: 1.6; color: #4a4a4a; font-size: 15px;">${h.message}</p>
        </div>
        <div style="background-color: #f9f8f6; padding: 15px; text-align: center; border-top: 1px solid #eaeaea; font-size: 12px; color: #888;">
          Diese Anfrage wurde über das Kontaktformular auf yacoub-schreinerei.de gesendet.
        </div>
      </div>
    `;

    // Resend API aufrufen
    const resendResponse = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        // Absender muss bei Resend verifiziert sein; Anzeigename macht die Anfrage im Posteingang erkennbar
        from: `${name.replace(/["<>\r\n]/g, '').slice(0, 60)} über Website <anfrage@yacoub-schreinerei.de>`,
        to: 'info@yacoub-schreinerei.de',
        subject: `Website-Anfrage: ${service} – ${name}`.replace(/[\r\n]+/g, ' '),
        html: htmlContent,
        reply_to: email
      })
    });

    if (!resendResponse.ok) {
      const errorText = await resendResponse.text();
      console.error('Resend error:', resendResponse.status, errorText);
      return redirectBack(request, 'error');
    }

    const result = await resendResponse.json().catch(() => ({}));
    console.log('Resend accepted email:', result.id);
    return redirectBack(request, 'success');

  } catch (err) {
    console.error('Server error:', err);
    return redirectBack(request, 'error');
  }
}
