FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]