class TableBuilder:
    def __init__(self, data_frame):
        self.df = data_frame.get_content()
        
        self.table = self.df

    def select(self, *columns):
        self.table = self.table[list(columns)]
            
        return self

    def where(self, condition):
        self.table = self.table.query(condition)

        return self

    def offset(self, count):
        self.table = self.table.iloc[count:]
        
        return self

    def limit(self, count):
        self.table = self.table.head(count)

        return self

    def order_by(self, column, ascending=True): 
        self.table = self.table.sort_values(by=column, ascending=ascending)

        return self

    def count(self, column):
        return len(self.table[list(column)]) if column else len(self.table) 

    def max(self, column): 
        return self.table[list(column)].max() if column else self.table.max() 

    def min(self, column):
        return self.table[list(column)].min() if column else self.table.min()
    
    def describe(self, column):
        return self.table[list(column)].describe() if column else self.table.describe()

    def avg(self, column):
        return self.table[list(column)].avg() if column else self.table.avg()

    def mean(self, column):
        return self.table[list(column)].mean() if column else self.table.mean()

    def distinct(self, column):
        if column:
            self.table = self.table[list(column)].drop_duplicates()
        else:
            self.table = self.table.drop_duplicates()

        return self

    def each(self):
        for index, row in self.table.iterrows():
            yield row

    def filter(self, callback, axis=1):
        self.query = self.query[self.query.apply(callback, axis=axis)]

    def get(self):
        return self.table