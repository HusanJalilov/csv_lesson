
def get_column(data):
    column_name = [data]
    return column_name

data = open('data.csv').read()
print(get_column(data))
