import pandas as pd



# Create DataFrames
countries_df = pd.read_csv(countries_data)

# Perform the merge (similar to VLOOKUP)
result_df = lookup_df.merge(countries_df, left_on='CountryName', right_on='name', how='left')

# Select relevant columns
result_df = result_df[['CountryName', 'Code', 'Year', 'Population', 'latitude', 'longitude']]

# Display the result
print(result_df)