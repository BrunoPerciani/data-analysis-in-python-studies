# To get more insight into the factors behind product quality, you want to filter the data to see an average product quality score for a specified set of results.
# Identify the average `product_quality_score` for batches with a `raw_material_supplier` of 2 and a `pigment_quantity` greater than 35 kg.
# Write a query to return the average `avg_product_quality_score` for these filtered batches. Use the original production data table, not the output of Task 2.

# - You should start with the data in the file 'production_data.csv'. 
# - Your output should be a DataFrame named pigment_data.
# - It should consist of a 1-row DataFrame with 3 columns: `raw_material_supplier`, `pigment_quantity`, and `avg_product_quality_score`.
# - Your answers should be rounded to 2 decimal places where appropriate.

import pandas as pd

df3 = pd.read_csv('production_data.csv')

filtered = df3[(df3['raw_material_supplier'] == 2) & (df3['pigment_quantity'] > 35)]

avg_score = round(filtered['product_quality_score'].mean(), 2)

pigment_data = pd.DataFrame({
    'raw_material_supplier': [2],
    'pigment_quantity': ['> 35'],
    'avg_product_quality_score': [avg_score]
})

pigment_data
