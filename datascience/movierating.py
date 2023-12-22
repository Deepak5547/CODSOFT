import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# Load the movie dataset (you can use your own dataset)
# Ensure the path to your dataset is correct
movie_data = pd.read_csv('path/to/movie_dataset.csv')

# Data analysis
print(movie_data.info())
print(movie_data.describe())
print(movie_data.head())

# Data preprocessing
def preprocess_data(data):
    # Drop unnecessary columns
    columns_to_drop = ['Title', 'Release Date']
    data = data.drop(columns=columns_to_drop)
    
    # Handle missing values in numeric columns
    numeric_features = data.select_dtypes(include=['float64']).columns
    for feature in numeric_features:
        data[feature].fillna(data[feature].mean(), inplace=True)
    
    return data

movie_data = preprocess_data(movie_data)

# Split the dataset into features (X) and target (y)
X = movie_data.drop('Rating', axis=1)
y = movie_data['Rating']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define numerical and categorical features
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

# Create transformers for numerical and categorical features
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Create a column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Build a pipeline with XGBoost
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(objective='reg:squarederror'))
])

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f'Root Mean Squared Error: {rmse:.2f}')
