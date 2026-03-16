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
