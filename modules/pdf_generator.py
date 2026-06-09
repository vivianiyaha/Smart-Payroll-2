from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_payslip(data, filename):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("PAYSLIP", styles["Title"]))
    elements.append(Spacer(1, 12))

    for k, v in data.items():
        elements.append(Paragraph(f"{k}: {v}", styles["Normal"]))

    doc.build(elements)
