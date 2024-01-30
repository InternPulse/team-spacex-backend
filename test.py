from invoicepilot_app.mailer import Invoice, send_email_with_pdf
iv = Invoice.objects.first()
tesy = True