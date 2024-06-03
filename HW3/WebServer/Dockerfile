FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install flask mysql-connector-python
CMD ["python", "myServer.py"]
EXPOSE 8008