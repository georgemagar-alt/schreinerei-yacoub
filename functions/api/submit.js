export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const formData = await request.formData();
    
    const name = formData.get('name') || '';
    const email = formData.get('email') || '';
    const phone = formData.get('phone') || '';
    const service = formData.get('service') || '';
    const address = formData.get('address') || '';
    const message = formData.get('message') || '';

    // HTML E-Mail Template
    const htmlContent = `
      <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #1a1a1a; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
        <div style="background-color: #ae8f73; padding: 30px; text-align: center;">
          <h2 style="color: white; margin: 0; font-size: 24px; font-weight: 300; letter-spacing: 1px;">Neue Kontaktanfrage</h2>
          <p style="color: rgba(255,255,255,0.8); margin: 10px 0 0 0; font-size: 14px; text-transform: uppercase; letter-spacing: 2px;">Schreinerei Yacoub</p>
        </div>
        <div style="padding: 40px 30px;">
          <div style="background-color: #f9f8f6; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
            <p style="margin: 0 0 10px 0;"><strong>Interesse an:</strong> ${service}</p>
            <p style="margin: 0 0 10px 0;"><strong>Von:</strong> ${name}</p>
            <p style="margin: 0 0 10px 0;"><strong>E-Mail:</strong> <a href="mailto:${email}" style="color: #ae8f73;">${email}</a></p>
            <p style="margin: 0 0 10px 0;"><strong>Telefon:</strong> ${phone}</p>
            <p style="margin: 0;"><strong>Adresse:</strong> ${address}</p>
          </div>
          
          <h3 style="color: #ae8f73; font-size: 14px; text-transform: uppercase; letter-spacing: 1.5px; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px; margin-top: 0;">Nachricht</h3>
          <p style="white-space: pre-wrap; line-height: 1.6; color: #4a4a4a; font-size: 15px;">${message}</p>
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
        from: 'Anfrage <anfrage@yacoub-schreinerei.de>', // Absender muss bei Resend verifiziert sein
        to: 'info@yacoub-schreinerei.de',
        subject: `Neue Anfrage: ${service} - ${name}`,
        html: htmlContent,
        reply_to: email
      })
    });

    if (!resendResponse.ok) {
      const errorText = await resendResponse.text();
      console.error('Resend error:', errorText);
      // Fallback: Redirect with error param or just let them know
      const referer = request.headers.get('Referer') || request.url;
      const redirectUrl = new URL(referer);
      redirectUrl.searchParams.set('error', '1');
      return Response.redirect(redirectUrl.toString(), 303);
    }

    // Erfolgs-Redirect auf die vorherige Seite mit ?success=1
    const referer = request.headers.get('Referer') || request.url;
    const redirectUrl = new URL(referer);
    redirectUrl.searchParams.set('success', '1');
    
    return Response.redirect(redirectUrl.toString(), 303);

  } catch (err) {
    console.error('Server error:', err);
    return new Response('Internal Server Error', { status: 500 });
  }
}
