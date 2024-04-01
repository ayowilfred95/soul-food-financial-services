import pandas as pd

# Read the three CSV files
data_0 = pd.read_csv('data/daily_sales_data_0.csv')
data_1 = pd.read_csv('data/daily_sales_data_1.csv')
data_2 = pd.read_csv('data/daily_sales_data_2.csv')

# Filter rows where product is "pink morsel"
data_0 = data_0[data_0['product'] == 'pink morsel']
data_1 = data_1[data_1['product'] == 'pink morsel']
data_2 = data_2[data_2['product'] == 'pink morsel']

# Calculate sales by multiplying quantity and price
data_0['sales'] = data_0['quantity'] * data_0['price']
data_1['sales'] = data_1['quantity'] * data_1['price']
data_2['sales'] = data_2['quantity'] * data_2['price']

# Select and rearrange columns
data_0 = data_0[['sales', 'date', 'region']]
data_1 = data_1[['sales', 'date', 'region']]
data_2 = data_2[['sales', 'date', 'region']]

# Merge the processed data
output_data = pd.concat([data_0, data_1, data_2])

# Write the output to a new CSV file
output_data.to_csv('output_file.csv', index=False)
