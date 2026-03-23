import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("processed.csv")

# Convert city to numbers
df['city'] = df['city'].astype('category')
city_mapping = dict(enumerate(df['city'].cat.categories))
df['city_code'] = df['city'].cat.codes

X = df[['city_code', 'hour']]
y = df['traffic']

model = RandomForestRegressor()
model.fit(X, y)

# Save model + mapping
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(city_mapping, open("city_map.pkl", "wb"))

print("Model trained!")