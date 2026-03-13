FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["sh", "-c", "unset STREAMLIT_SERVER_PORT STREAMLIT_SERVER_ADDRESS; streamlit run app/app.py --server.port ${PORT:-8501} --server.address 0.0.0.0"]
