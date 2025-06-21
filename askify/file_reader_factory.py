import pandas as pd
from askify.file_reader import FileReader
from askify.file_ext import FileExt


class FileReaderFactory:
    @staticmethod
    def read_csv(file_path): 
        data = pd.read_csv(file_path)

        return FileReader(
            ext=FileExt.CSV, 
            file=file_path, 
            data = data
        )

    @staticmethod
    def read_json(file_path): 
        data = pd.read_json(file_path)
        
        return FileReader(
            ext=FileExt.JSON, 
            file=file_path, 
            data = data
        )

    @staticmethod
    def read_excel(file_path): 
        data = pd.read_excel(file_path)
        
        return FileReader(
            ext=FileExt.EXCEL, 
            file=file_path, 
            data = data
        )

    @staticmethod
    def read_html(file_path): 
        data = pd.read_html(file_path)

        return FileReader(
            ext=FileExt.HTML, 
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