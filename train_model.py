import json
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Configuration
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / 'carprice.csv'
MODEL_PATH = PROJECT_ROOT / 'model.pkl'
EXPERIMENT_NAME = 'CarPricePrediction'
TARGET_COLUMN = 'selling_price'

def load_and_preprocess_data(data_path):
    df = pd.read_csv(data_path)
    
    # Preprocessing: convert to numeric and handle missing values
    for column in ['mileage(km/ltr/kg)', 'engine', 'max_power', 'seats']:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    df['name'] = df['name'].astype(str).str.strip()
    df = df.dropna(subset=[TARGET_COLUMN])
    
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

def build_pipeline():
    numeric_features = ['year', 'km_driven', 'mileage(km/ltr/kg)', 'engine', 'max_power', 'seats']
    categorical_features = ['name', 'fuel', 'seller_type', 'transmission', 'owner']
    
    numeric_transformer = Pipeline(
        steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore')),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features),
        ]
    )

    return Pipeline(
        steps=[
            ('preprocessor', preprocessor),
            ('model', RandomForestRegressor(
                n_estimators=250,
                max_depth=18,
                min_samples_split=4,
                min_samples_leaf=2,
                random_state=42,
                n_jobs=-1,
            )),
        ]
    )

def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return {
        'rmse': float(mse ** 0.5),
        'mae': float(mean_absolute_error(y_test, predictions)),
        'r2': float(r2_score(y_test, predictions)),
    }

def train():
    X_train, X_test, y_train, y_test = load_and_preprocess_data(DATA_PATH)
    
    mlflow.set_experiment(EXPERIMENT_NAME)
    
    with mlflow.start_run(run_name='random_forest'):
        pipeline = build_pipeline()
        pipeline.fit(X_train, y_train)
        
        metrics = evaluate(pipeline, X_test, y_test)
        
        # Log parameters
        mlflow.log_param('model_name', 'random_forest')
        mlflow.log_param('train_rows', len(X_train))
        mlflow.log_param('test_rows', len(X_test))
        
        # Log metrics
        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(metric_name, metric_value)
            
        # Log model
        mlflow.sklearn.log_model(
            sk_model=pipeline,
            artifact_path='model',
            input_example=X_test.head(2),
        )
        
        # Save model locally
        joblib.dump(pipeline, MODEL_PATH)
        
        print(f"Model trained. R2 Score: {metrics['r2']:.4f}")

if __name__ == "__main__":
    train()
