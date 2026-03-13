# Car Price Prediction with MLflow and Streamlit

This project demonstrates an end-to-end machine learning workflow for predicting used car prices. It includes data preprocessing, model selection, experiment tracking with MLflow, and a web-based user interface using Streamlit.

## 🚀 Features

- **MLflow Tracking**: Logs parameters, metrics, and models.
- **Streamlit UI**: Intuitive web interface for real-time predictions.
- **Dockerized**: Easy deployment using containers.
- **Railway Compatible**: Optimized for deployment on Railway.

## 📁 Project Structure

```text
CAR_PRICE/
├── app/
│   ├── app.py          # Streamlit application
│   └── schema.py       # (Optional) Data schemas
├── data/
│   └── carprice.csv    # Dataset
├── models/
│   └── model.pkl       # Trained model pipeline
├── src/
│   ├── car_price_mlflow.ipynb  # Training notebook
│   ├── mlflow.db       # MLflow backend store
│   └── mlruns/         # MLflow tracking data
├── Dockerfile          # Container configuration
├── Procfile            # Deployment instructions
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🛠️ Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Tarrun1506/Car-price-prediction-mlflow.git
   cd Car-price-prediction-mlflow
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # MacOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Usage

### Training the Model
Open the training notebook and run all cells:
```bash
jupyter notebook src/car_price_mlflow.ipynb
```

### Running the Web App
```bash
streamlit run app/app.py
```

### Viewing MLflow UI
```bash
mlflow ui --backend-store-uri file:./src/mlruns
```

## 🐳 Docker

Build and run the application using Docker:
```bash
docker build -t car-price-predictor .
docker run -p 8501:8501 car-price-predictor
```

## 🚢 Deployment

The project is configured for easy deployment on **Railway**:
1. Push the repository to GitHub.
2. Connect your GitHub repository to a new Railway project.
3. Railway will automatically build the image using the `Dockerfile` and deploy the service.
