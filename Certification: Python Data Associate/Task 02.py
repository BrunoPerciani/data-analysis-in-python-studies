# You want to understand how the supplier type and quantity of materials affect the final product attributes.
# Calculate the average `product_quality_score` and `pigment_quantity` grouped by `raw_material_supplier`.

# - You should start with the data in the file 'production_data.csv'. 
# - Your output should be a DataFrame named aggregated_data.
# - It should include the three columns: `raw_material_supplier`, `avg_product_quality_score`, and `avg_pigment_quantity`.
# - Your answers should be rounded to 2 decimal places.

import pandas as pd

df2 = pd.read_csv('production_data.csv')

aggregated_data = (
    df2.groupby('raw_material_supplier', as_index = False)
       .agg(
           avg_product_quality_score = ('product_quality_score', 'mean'),
           avg_pigment_quantity = ('pigment_quantity', 'mean')
       ).round(2)  
)

aggregated_data
