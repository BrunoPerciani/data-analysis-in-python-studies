# Before you can start any analysis, you need to confirm that the data is accurate and reflects what you expect to see. 
# It is known that there are some issues with the `production_data` table, and the data team have provided the following data description. 
# Write a query to ensure the data matches the description provided, including identifying and cleaning all invalid values. You must match all column names and description criteria.
# - You should start with the data in the file "production_data.csv".
# - Your output should be a DataFrame named clean_data.
# - All column names and values should match the table below.

# | Column Name             | Criteria                                     |
# |-------------------------|----------------------------------------------|
# | batch_id | Discrete. Identifier for each batch. Missing values are not possible. |
# | production_date | Date. Date when the batch was produced.|
# | raw_material_supplier | Categorical. Supplier of the raw materials. (1='national_supplier', 2='international_supplier'). Missing values should be replaced with 'national_supplier'.|
# | pigment_type | Nominal. Type of pigment used. ['type_a', 'type_b', 'type_c']. Missing values should be replaced with 'other'. |
# | pigment_quantity | Continuous. Amount of pigment added (in kilograms) (Range: 1 - 100). Missing values should be replaced with median. |
# | mixing_time | Continuous. Duration of the mixing process (in minutes). Missing values should be replaced with mean, rounded to 2 decimal places. |
# | mixing_speed | Categorical. Speed of the mixing process represented as categories: 'Low', 'Medium', 'High'. Missing values should be replaced with 'Not Specified'. |
# | product_quality_score | Continuous. Overall quality score of the final product (rating on a scale of 1 to 10). Missing values should be replaced with mean, rounded to 2 decimal places. |

import pandas as pd
df = pd.read_csv('production_data.csv')

df = df.dropna(subset = ['batch_id'])

df['production_date'] = pd.to_datetime(df['production_date'], errors = 'coerce') 
df = df.dropna(subset = ['production_date'])

supplier_map = {1: 'national_supplier', 2: 'international_supplier'} 
df['raw_material_supplier'] = df['raw_material_supplier'].map(supplier_map)
df['raw_material_supplier'].fillna('national_supplier', inplace = True)

valid_pigments = ['type_a', 'type_b', 'type_c']
df['pigment_type'] = df['pigment_type'].astype(str).str.lower().str.strip()
df['pigment_type'] = df['pigment_type'].apply( lambda x: x if x in valid_pigments else 'other')

median_pigment = df['pigment_quantity'].median()
df['pigment_quantity'] = df['pigment_quantity'].apply(lambda x: x if 1 <= x <= 100 else np.nan)
df['pigment_quantity'].fillna(median_pigment, inplace = True)

mean_mixing = round(df['mixing_time'].mean(), 2)
df['mixing_time'].fillna(mean_mixing, inplace = True)

valid_speeds = ['Low', 'Medium', 'High']
df['mixing_speed'] = df['mixing_speed'].apply(lambda x: x if x in valid_speeds else 'Not Specified')

mean_quality = round(df['product_quality_score'].mean(), 2)
df['product_quality_score'].fillna(mean_quality, inplace = True)

clean_data = df.copy()
clean_data
