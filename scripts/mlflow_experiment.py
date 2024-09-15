import mlflow
import mlflow.sklearn
import wandb
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml

# Initialize W&B
wandb.init(project="boston_housing_experiment")
os.environ["no_proxy"]="*"

# Set the experiment name
mlflow.set_experiment("boston_housing_experiment")

# Set the tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5001")

# Load dataset
boston = fetch_openml(name="boston", version=1, as_frame=True)
X = boston.data
y = boston.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start a new run
with mlflow.start_run():
    # Train a model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, predictions)
    
    # Log parameters and metrics to MLflow
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("mse", mse)
    
    # Log the model to MLflow
    mlflow.sklearn.log_model(model, "random_forest_model")
    
    # Log parameters and metrics to W&B
    wandb.log({"n_estimators": 100, "mse": mse})
    
    # Log the model to W&B
    wandb.sklearn.log_model(model, "random_forest_model")
    
    print(f"Model logged with MSE: {mse}")