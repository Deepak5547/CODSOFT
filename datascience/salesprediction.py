import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Load the sales dataset (replace 'path/to/sales_dataset.csv' with the actual path)
sales_data = pd.read_csv('path/to/sales_dataset.csv')

# Data analysis
print("Data Information:")
print(sales_data.info())
print("\nDescriptive Statistics:")
print(sales_data.describe())
print("\nFirst 5 Rows of the Dataset:")
print(sales_data.head())

# Data preprocessing
def preprocess_data(data):
    # Handle missing values by filling them with 0
    data.fillna(0, inplace=True)
    
    return data

# Apply preprocessing to the dataset
sales_data = preprocess_data(sales_data)

# Split the dataset into features (X) and target (y)
X = sales_data.drop('sales', axis=1)
y = sales_data['sales']

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
    ('regressor', XGBRegressor(objective='reg:squarederror', random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f'\nRoot Mean Squared Error: {rmse:.2f}')
