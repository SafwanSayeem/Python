import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = pd.DataFrame({
    'Square_feet': [1500, 2000, 1200, 1800, 2400, 1000, 2200, 1700, 1300, 1900],
    'Bedrooms': [3, 4, 2, 3, 4, 2, 3, 3, 4, 2],
    'Bathrooms': [2, 3, 1, 2, 3, 1, 2, 2, 3, 1],
    'Location': ['suburban', 'urban', 'rural', 'suburban', 'urban', 'rural', 'suburban', 'suburban', 'urban', 'rural'],
    'Age': [10, 5, 15, 8, 3, 20, 6, 12, 7, 18],
    'Price': [250000, 400000, 150000, 300000, 450000, 120000, 320000, 280000, 380000, 140000]
})

label_encode = LabelEncoder()
data['Location'] = label_encode.fit_transform(data['Location'])

X = data[['Square_feet', 'Bedrooms', 'Bathrooms', 'Location', 'Age']]
y = data['Price']

y = np.array(y)

model = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=69)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}') 
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')

user_square_feet = input('Size (square feet): ')
user_bedroom = input('Bedrooms: ')
user_bathroom = input('Bathrooms: ')
user_location = input('Location: ').lower()
user_age = input('Age: ')

def house():
    global user_square_feet,user_bedroom,user_bathroom,user_location,user_age
    try:
        user_square_feet = int(user_square_feet)
        user_bedroom = int(user_bedroom)
        user_bathroom = int(user_bathroom)
        user_age = int(user_age)
        user_location_encoded = label_encode.transform([user_location])[0]
        user_house = pd.DataFrame([[user_square_feet, user_bedroom, user_bathroom, user_location_encoded, user_age]],
                           columns=['Square_feet', 'Bedrooms', 'Bathrooms', 'Location', 'Age'])
    except (ValueError,SyntaxError,TypeError):
        return None
    return user_house
user_house=house()
if user_house is not None:
    pred_price = model.predict(user_house)
    print(f'The predicted price is ${pred_price[0]:.2f}')
else:
    print('Could not provide price due to invalid information')
