import pandas as pd
from io import BytesIO

from converters.data_converters.csv_converter import CSVConverter


class ExcelConverter:
    # * Excel to CSV
    @staticmethod
    def excel_to_csv(input_file):
        df = pd.read_excel(input_file)
        buffer = BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        return buffer
    
    # * Excel to JSON
    @staticmethod
    def excel_to_json(input_file):
        return CSVConverter.csv_to_json(ExcelConverter.excel_to_csv(input_file))
    
    # * Excel to pdf
    @staticmethod
    def excel_to_pdf(input_file):
        return CSVConverter.csv_to_pdf(ExcelConverter.excel_to_csv(input_file))
    
    # * Excel to HTML
    @staticmethod
    def excel_to_html(input_file):
        return CSVConverter.csv_to_html(ExcelConverter.excel_to_csv(input_file))
    
    # * Excel to TSV
    @staticmethod
    def excel_to_tsv(input_file):
        return CSVConverter.csv_to_tsv(ExcelConverter.excel_to_csv(input_file))