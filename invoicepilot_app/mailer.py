from django.core.mail import EmailMessage
from invoicepilot_app.models import Invoice, MailRecord
from typing import Optional


def send_email_with_pdf(subject: str, message: str, pdf_content: bytes, invoice: Invoice, template: Optional[str] = 'default') -> bool:
    """Send an email containing the invoice to the customer"""
    email = EmailMessage(
        subject,
        message,
        'your-email@example.com',
        to=[invoice.recipent.email],
    )

    if pdf_content:
        email.attach('invoice.pdf', pdf_content, 'application/pdf')
    sent = email.send()
    if sent:
        MailRecord.objects.create(
            invoice=invoice,
            to=invoice.recipent.email,
            template_used=template
        )
        return True
    return False

     
  
   