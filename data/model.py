import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv('data/house_data.csv')

x= data[{'area'}]
y= data ['price']

model = LinearRregression()
model.fit(x,y)

jolib.dump(model , 'model.pkl')

print("model trained and saved as model.pkl")