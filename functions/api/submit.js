export async function onRequestPost(context) {
  try {
    // Grab the request and the environment variables (where RESEND_API_KEY lives)
    const { request, env } = context;

    // Parse formData from the POST request
    const formData = await request.formData();
    const service = formData.get('service') || '';
    const name = formData.get('name') || '';
    const email = formData.get('email') || '';
    const phone = formData.get('phone') || '';
    const address = formData.get('address') || '';
    const message = formData.get('message') || '';

    // Create the email content
    const htmlContent = `
      <h2>Neue Kontaktanfrage (Website)</h2>
      <p><strong>Service:</strong> ${service}</p>
      <p><strong>Name:</strong> ${name}</p>
      <p><strong>E-Mail:</strong> ${email}</p>
      <p><strong>Telefon:</strong> ${phone}</p>
      <p><strong>Adresse:</strong> ${address}</p>
      <p><strong>Nachricht:</strong><br>${message.replace(/\n/g, '<br>')}</p>
    `;

    // Send email using Resend API
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${env.RESEND_API_KEY}`
      },
      body: JSON.stringify({
        from: 'Website Kontaktformular <onboarding@resend.dev>', // Should be verified domain if available
        to: ['info@yacoub-schreinerei.de'], // The email where requests will be sent
        reply_to: email,
        subject: `Neue Anfrage von ${name} - ${service}`,
        html: htmlContent
      })
    });

    if (!res.ok) {
      const errorText = await res.text();
      console.error('Failed to send email via Resend:', errorText);
      // Optional: You could redirect to an error page, or just back to contact with an error parameter
      return Response.redirect(new URL('/?error=1#kontakt', request.url), 303);
    }

    // On success, redirect to the frontend with success parameter
    const url = new URL(request.url);
    url.pathname = '/';
    url.searchParams.set('success', '1');
    url.hash = 'kontakt';

    return Response.redirect(url.toString(), 303);

  } catch (err) {
    console.error('Error handling form submission:', err);
    return new Response('Internal Server Error', { status: 500 });
  }
}
