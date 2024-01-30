from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

def generate_invoice(values, no: int = 0):
    env = Environment(loader=FileSystemLoader('./invoice_templates'))
    template = env.get_template(f'index.html')
    html_content = template.render(values)

    # Convert the HTML content to PDF
    HTML(string=html_content).write_pdf('output.pdf')

if __name__ == "__main__":
    # Specify template variables
    template_vars = {}

    # Generate the PDF
    generate_invoice(template_vars)

    print("PDF generated successfully.")