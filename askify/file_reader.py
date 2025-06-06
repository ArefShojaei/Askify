class FileReader:
    def __init__(self, ext, file, data): 
        self.ext = ext
        self.file = file
        self.data = data
    
    def get_content(self):
        return self.data