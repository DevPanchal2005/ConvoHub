import pandas as pd
import xml.etree.ElementTree as ET
from fpdf import FPDF
from io import BytesIO

class CSVConverter:
    # * Convert CSV to Excel
    @staticmethod
    def csv_to_excel(input_file):
        buffer = BytesIO()
        df = pd.read_csv(input_file)
        df.to_excel(buffer, index=False)
        buffer.seek(0)
        return buffer

    # * Convert CSV to JSON
    @staticmethod
    def csv_to_json(input_file):
        buffer = BytesIO()
        df = pd.read_csv(input_file)
        buffer.write(df.to_json(orient='records', indent=2).encode())
        buffer.seek(0)
        return buffer

    # * Convert CSV to PDF
    @staticmethod
    def csv_to_pdf(input_file):
        buffer = BytesIO()
        df = pd.read_csv(input_file)

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)  # Prevents text from overflowing
        pdf.add_page()
        pdf.set_font("Arial", size=2)

        # Get column names
        col_names = list(df.columns)
        col_width = 190 / len(col_names)  # Adjust column width dynamically

        # Add table headers
        pdf.set_fill_color(200, 200, 200)  # Light gray background for headers
        for col in col_names:
            pdf.cell(col_width, 10, col, border=1, ln=0, align="C", fill=True)
        pdf.ln()  # Move to next row

        # Add table data
        for _, row in df.iterrows():
            for col in col_names:
                text = str(row[col]) if pd.notna(row[col]) else ""
                pdf.cell(col_width, 10, text, border=1, ln=0, align="C")
            pdf.ln()  # Move to next row

        # Fix: Output PDF as string and write to BytesIO
        pdf_bytes = pdf.output(dest='S').encode('latin1')  # Convert to bytes
        buffer.write(pdf_bytes)
        buffer.seek(0)
        
        return buffer

    # * Convert CSV to HTML
    @staticmethod
    def csv_to_html(input_file):
        buffer = BytesIO()
        df = pd.read_csv(input_file)

        # Convert DataFrame to HTML table with Bootstrap styling
        html_table = df.to_html(index=False, escape=False, classes="table table-bordered table-striped")

        # Write to buffer
        buffer.write(html_table.encode("utf-8"))
        buffer.seek(0)

        return buffer
    
    # * Convert CSV to TSV
    @staticmethod
    def csv_to_tsv(input_file):
        buffer = BytesIO()
        df = pd.read_csv(input_file)

        # Convert DataFrame to TSV format
        tsv_data = df.to_csv(sep='\t', index=False)

        # Write to buffer
        buffer.write(tsv_data.encode("utf-8"))
        buffer.seek(0)

        return buffer