FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask requests flask_sqlalchemy pymysql
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]