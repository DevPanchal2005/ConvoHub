import streamlit as st

from converters.data_converters.csv_converter import CSVConverter
from converters.data_converters.excel_converter import ExcelConverter
from converters.data_converters.json_converter import JSONConverter

st.logo('resources/logo.png', size='large')

input_file = st.file_uploader("Upload a CSV or Excel or JSON file", type=["csv", "xlsx", "json"])

if input_file is not None:
    file_name = input_file.name
    file_type = input_file.type

    # st.write(f"File Name: {file_name}")
    # st.write(f"File Type: {file_type}")

    match(file_type):

        case 'text/csv':
            if st.button('Convert to Excel', icon=':material/table_convert:', use_container_width=True):
                file_name = file_name.replace('.csv', '.xlsx')
                output_file = CSVConverter.csv_to_excel(input_file)
                st.download_button("Download Excel", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to JSON', icon=':material/file_json:', use_container_width=True):
                file_name = file_name.replace('.csv', '.json')
                output_file = CSVConverter.csv_to_json(input_file)
                st.download_button("Download JSON", output_file.getvalue(), icon=':material/download:', use_container_width=True, file_name=file_name, mime="application/json")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to PDF', icon=':material/picture_as_pdf:', use_container_width=True):
                file_name = file_name.replace('.csv', '.pdf')
                output_file = CSVConverter.csv_to_pdf(input_file)
                st.download_button("Download PDF", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="application/pdf")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to HTML', icon=':material/code:', use_container_width=True):
                file_name = file_name.replace('.csv', '.html')
                output_file = CSVConverter.csv_to_html(input_file)
                st.download_button("Download HTML", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="text/html")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to TSV', icon=':material/tsv:', use_container_width=True):
                file_name = file_name.replace('.csv', '.tsv')
                output_file = CSVConverter.csv_to_tsv(input_file)
                st.download_button("Download TSV", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="text/tab-separated-values")
                st.toast(f'{file_name} is ready to Download', icon='✅')

        case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            if st.button('Convert to CSV', icon=':material/csv:', use_container_width=True):
                file_name = file_name.replace('.xlsx', '.csv')
                output_file = ExcelConverter.excel_to_csv(input_file)
                st.download_button("Download CSV", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="text/csv")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to JSON', icon=':material/file_json:', use_container_width=True):
                file_name = file_name.replace('.xlsx', '.json')
                output_file = ExcelConverter.excel_to_json(input_file)
                st.download_button("Download JSON", output_file.getvalue(), icon=':material/download:', use_container_width=True, file_name=file_name, mime="application/json")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to PDF', icon=':material/picture_as_pdf:', use_container_width=True):
                file_name = file_name.replace('.xlsx', '.pdf')
                output_file = ExcelConverter.excel_to_pdf(input_file)
                st.download_button("Download PDF", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="application/pdf")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to HTML', icon=':material/code:', use_container_width=True):
                file_name = file_name.replace('.xlsx', '.html')
                output_file = ExcelConverter.excel_to_html(input_file)
                st.download_button("Download HTML", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="text/html")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to TSV', icon=':material/tsv:', use_container_width=True):
                file_name = file_name.replace('.xlsx', '.tsv')
                output_file = ExcelConverter.excel_to_tsv(input_file)
                st.download_button("Download TSV", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="text/tab-separated-values")
                st.toast(f'{file_name} is ready to Download', icon='✅')

        case 'application/json':
            if st.button('Convert to CSV', icon=':material/csv:', use_container_width=True):
                file_name = file_name.replace('.json', '.csv')
                output_file = JSONConverter.json_to_csv(input_file)
                st.download_button("Download CSV", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="text/csv")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to Excel', icon=':material/table_convert:', use_container_width=True):
                file_name = file_name.replace('.json', '.xlsx')
                output_file = JSONConverter.json_to_excel(input_file)
                st.download_button("Download Excel", output_file, use_container_width=True, icon=':material/download:', file_name=file_name, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to PDF', icon=':material/picture_as_pdf:', use_container_width=True):
                file_name = file_name.replace('.json', '.pdf')
                output_file = JSONConverter.json_to_pdf(input_file)
                st.download_button("Download PDF", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="application/pdf")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to HTML', icon=':material/code:', use_container_width=True):
                file_name = file_name.replace('.json', '.html')
                output_file = JSONConverter.json_to_html(input_file)
                st.download_button("Download HTML", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="text/html")
                st.toast(f'{file_name} is ready to Download', icon='✅')

            if st.button('Convert to TSV', icon=':material/tsv:', use_container_width=True):
                file_name = file_name.replace('.json', '.tsv')
                output_file = JSONConverter.json_to_tsv(input_file)
                st.download_button("Download TSV", output_file, icon=':material/download:', use_container_width=True, file_name=file_name, mime="text/tab-separated-values")
                st.toast(f'{file_name} is ready to Download', icon='✅')
                
        case _:
            st.error("Invalid file type. Please upload a CSV or Excel or JSON file.") 
    
