
def get_column(data):
    column_name = [data].split("/n")
    column_name=column_name[].split(",")
    
    
    return column_name

data = open('data.csv').read()
print(get_column(data))
