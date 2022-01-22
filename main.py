
def get_column(data):
    
    column_name=data.split()
    
    
    
    return column_name[0].split(",")

data = open('data.csv').read()
print(get_column(data))
