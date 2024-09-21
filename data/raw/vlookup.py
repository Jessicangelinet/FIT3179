import pandas as pd


# Create DataFrames
countries_df = pd.read_csv("data/raw/population.csv")
lookup_df = pd.read_csv("data/raw/latlong.csv")
# Convert 'name' column to lowercase and strip whitespaces
temp = countries_df['CountryName']
print(temp)
countries_df['aggr'] = countries_df['CountryName'].str.lower().str.strip()
# Remove all spaces from the 'name' column
countries_df['aggr'] = countries_df['aggr'].str.replace(" ", "", regex=False)

lookup_df['Name'] = lookup_df['Name'].str.lower().str.strip()
# Remove all spaces from the 'name' column
lookup_df['Name'] = lookup_df['Name'].str.replace(" ", "", regex=False)
print(lookup_df)

# Perform the merge (similar to VLOOKUP)
result_df = lookup_df.merge(countries_df, left_on='Name', right_on='aggr', how='right')

# Select relevant columns
result_df = result_df[['CountryName', 'Code', 'Year', 'Population', 'latitude', 'longitude']]
result_df = result_df.drop_duplicates().dropna()

# Display the result
print(result_df)
# Save the DataFrame to a CSV file
result_df.to_csv('data/countries_lat_long.csv', index=False)
