from fpdf import FPDF

def render_pdf_report(insights):
    print("Generating PDF report...")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, insights)
    pdf.output("insights_report.pdf")
    return True