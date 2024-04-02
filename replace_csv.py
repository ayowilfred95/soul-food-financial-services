with open('data/daily_sales_data_0.csv', 'r') as file:
    filedata = file.read()
    
filedata = filedata.replace('2018', '2019').replace('2019', '2020')


with open('data/daily_sales_data_0.csv', 'w') as file:
    file.write(filedata)
