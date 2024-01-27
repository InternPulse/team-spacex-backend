# invoices/utils.py
from django.core.mail import EmailMultiAlternatives
from invoices.models import Invoice, MailRecord
from django.core.mail import EmailMessage
from typing import Optional
from .email_templates import (
    PASSWORD_RESET, PR_TEXT,
    VERIFY_ACCOUNT, VA_TEXT,
    WELCOME, W_TEXT
)

def send_email_with_pdf(subject: str, message: str, pdf_content: bytes, invoice: Invoice, template: Optional[str] = 'default') -> bool:
    """Send an email containing the invoice and the generated PDF to the customer"""
    email = EmailMessage(
        subject,
        message,
        'your-email@example.com',
        to=[invoice.recipient.email],
    )

    if pdf_content:
        email.attach('invoice.pdf', pdf_content, 'application/pdf')
    sent = email.send()
    if sent:
        MailRecord.objects.create(
            invoice=invoice,
            to=invoice.recipient.email,
            template_used=template
        )
        return True
    return False


class Mailer:
    INFO_MAIL_CHOICES = {
        "welcome": [WELCOME, W_TEXT],
        "verify": [VERIFY_ACCOUNT, VA_TEXT],
        "pwd_reset": [PASSWORD_RESET, PR_TEXT]
    }

    def send_email(self, subject: str, recipent: str, mail_type: str, 
        placeholders: str,
        sender: Optional[str] = "invoicepilot@gmail.com") -> bool:
        email = EmailMultiAlternatives(
            subject,
            self.INFO_MAIL_CHOICES[mail_type][1].format(**placeholders),
            'invoicepilot@support.poeticverse.me',
            to=[recipent]
        )
        email.attach_alternative(self.INFO_MAIL_CHOICES[mail_type][0].format(**placeholders), "text/html")
        return email.send()
