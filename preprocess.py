import pandas as pd

df = pd.read_csv("traffic.csv")

# Extract hour
df['hour'] = pd.to_datetime(df['Date/Time']).dt.hour

# Map Base → City Names
city_map = {
    "B02512": "New York",
    "B02598": "Manhattan",
    "B02617": "Brooklyn",
    "B02682": "Queens",
    "B02764": "Bronx"
}

df['city'] = df['Base'].map(city_map)

# Group into traffic counts
df_grouped = df.groupby(['city', 'hour']).size().reset_index(name='traffic')

df_grouped.to_csv("processed.csv", index=False)

print("Preprocessing done!")