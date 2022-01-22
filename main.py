
def get_column(data):
    column_name = [data]
    column_name=column_name[0]
    column_name=column_name[:31].split(",")
    
    return column_name

data = open('data.csv').read()
print(get_column(data))
