# In order to proceed with further analysis later, you need to analyze how various factors relate to product quality. Start by calculating the mean and standard deviation for the following columns: `pigment_quantity`, and `product_quality_score`. </br> These statistics will help in understanding the central tendency and variability of the data related to product quality.
# Next, calculate the Pearson correlation coefficient between the following variables: `pigment_quantity`, and `product_quality_score`.
# These correlation coefficients will provide insights into the strength and direction of the relationships between the factors and overall product quality.

# - You should start with the data in the file 'production_data.csv'.
# - Calculate the mean and standard deviation for the columns pigment_quantity and product_quality_score as: `product_quality_score_mean`, `product_quality_score_sd`, `pigment_quantity_mean`, `pigment_quantity_sd`.
# - Calculate the Pearson correlation coefficient between pigment_quantity and product_quality_score as: `corr_coef`
# - Your output should be a DataFrame named product_quality.
# - It should include the columns: `product_quality_score_mean`, `product_quality_score_sd`, `pigment_quantity_mean`, `pigment_quantity_sd`, `corr_coef`.
# - Ensure that your answers are rounded to 2 decimal places.

import pandas as pd

df4 = pd.read_csv('production_data.csv')

product_quality_score_mean = round(df4['product_quality_score'].mean(), 2)
product_quality_score_sd = round(df4['product_quality_score'].std(), 2)
pigment_quantity_mean = round(df4['pigment_quantity'].mean(), 2)
pigment_quantity_sd = round(df4['pigment_quantity'].std(), 2)

corr_coef = round(df4['pigment_quantity'].corr(df4['product_quality_score']), 2)

product_quality = pd.DataFrame({
    'product_quality_score_mean': [product_quality_score_mean],
    'product_quality_score_sd': [product_quality_score_sd],
    'pigment_quantity_mean': [pigment_quantity_mean],
    'pigment_quantity_sd': [pigment_quantity_sd],
    'corr_coef': [corr_coef]
})

product_quality
