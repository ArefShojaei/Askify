import pandas as pd
from askify.file_reader import FileReader


class FileReaderFactory:
    CSV_EXT = ".csv"
    HTML_EXT = ".html"
    JSON_EXT = ".json"
    EXCEL_EXT = ".excel"

    @staticmethod
    def read_csv(file_path): 
        data = pd.read_csv(file_path)

        return FileReader(
            ext=FileReaderFactory.CSV_EXT, 
            file=file_path, 
            data = data
        )

    @staticmethod
    def read_json(file_path): 
        data = pd.read_json(file_path)
        
        return FileReader(
            ext=FileReaderFactory.JSON_EXT, 
            file=file_path, 
            data = data
        )

    @staticmethod
    def read_excel(file_path): 
        data = pd.read_excel(file_path)
        
        return FileReader(
            ext=FileReaderFactory.EXCEL_EXT, 
            file=file_path, 
            data = data
        )

    @staticmethod
    def read_html(file_path): 
        data = pd.read_html(file_path)

        return FileReader(
            ext=FileReaderFactory.HTML_EXT, 
            file=file_path, 
            data = data
        )

    @staticmethod
    def create_frame(data):
        data = pd.DataFrame(data)

        return FileReader(
            ext=None,
            file=None,
            data=data
        )