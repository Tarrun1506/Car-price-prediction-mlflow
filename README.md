# Car Price Prediction

This project predicts used car selling prices using machine learning. Model training and MLflow tracking are done in Jupyter Notebook, and the frontend is built with Streamlit.

## Project Structure

```text
CAR_PRICE/
|-- app/
|   `-- app.py
|-- data/
|   `-- carprice.csv
|-- models/
|   `-- model.pkl
|-- src/
|   |-- car_price_mlflow.ipynb
|   |-- mlflow.db
|   `-- mlruns/
|-- Dockerfile
|-- Procfile
|-- requirements.txt
`-- README.md
```

## Current Workflow

1. Train the model in `src/car_price_mlflow.ipynb`
2. Track experiments using MLflow
3. Save the trained model in `models/model.pkl`
4. Run the Streamlit app from `app/app.py`
5. Dockerize the project
6. Deploy on Railway

## Use venv

Open terminal in [D:\MLOPS\CAR_PRICE](D:\MLOPS\CAR_PRICE)

```bash
venv\Scripts\activate
```

If needed, install packages:

```bash
pip install -r requirements.txt
```

## Train the Model

Start Jupyter from the project root:

```bash
jupyter notebook
```

Open [D:\MLOPS\CAR_PRICE\src\car_price_mlflow.ipynb](D:\MLOPS\CAR_PRICE\src\car_price_mlflow.ipynb) and run all cells.

The notebook reads data from [D:\MLOPS\CAR_PRICE\data\carprice.csv](D:\MLOPS\CAR_PRICE\data\carprice.csv) and saves the trained model to [D:\MLOPS\CAR_PRICE\models\model.pkl](D:\MLOPS\CAR_PRICE\models\model.pkl).

Note: your current notebook runs have already created MLflow tracking files inside `src/`:
- `src/mlflow.db`
- `src/mlruns/`

These are local tracking outputs and are ignored by Git.

## Run the Streamlit App

```bash
streamlit run app/app.py
```

Open:

- `http://localhost:8501`

## Run MLflow UI

If your latest runs are in `src/mlruns`, use:

```bash
mlflow ui --backend-store-uri file:./src/mlruns
```

Open:

- `http://127.0.0.1:5000`

## Docker

Build:

```bash
docker build -t car-price-predictor .
```

Run:

```bash
docker run -p 8501:8501 car-price-predictor
```

## Railway Deployment

1. Push this project to GitHub
2. Make sure [D:\MLOPS\CAR_PRICE\models\model.pkl](D:\MLOPS\CAR_PRICE\models\model.pkl) is included in the repo
3. Create a Railway project from the GitHub repo
4. Railway will use the `Dockerfile`
5. The Docker container must bind to Railway's `PORT` environment variable
6. Open the deployed link and test the app

## Submission

Submit these two links:

- GitHub repository link
- Railway deployed link
