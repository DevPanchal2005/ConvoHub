import pandas as pd
from io import BytesIO

from converters.data_converters.csv_converter import CSVConverter

class JSONConverter:
    # * JSON to CSV
    @staticmethod
    def json_to_csv(input_file):
        buffer = BytesIO()
        df = pd.read_json(input_file)
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        return buffer
    
    # * JSON to Excel
    @staticmethod
    def json_to_excel(input_file):
        return CSVConverter.csv_to_excel(JSONConverter.json_to_csv(input_file))
    
    # * JSON to PDF
    @staticmethod
    def json_to_pdf(input_file):
        return CSVConverter.csv_to_pdf(JSONConverter.json_to_csv(input_file))
    
    # * JSON to HTML
    @staticmethod
    def json_to_html(input_file):
        return CSVConverter.csv_to_html(JSONConverter.json_to_csv(input_file))
    
    # * JSON to TSV
    @staticmethod
    def json_to_tsv(input_file):
        return CSVConverter.csv_to_tsv(JSONConverter.json_to_csv(input_file))