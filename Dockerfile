FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["sh", "-c", "export STREAMLIT_SERVER_PORT=${PORT}; export STREAMLIT_SERVER_ADDRESS=0.0.0.0; streamlit run app/app.py"]
