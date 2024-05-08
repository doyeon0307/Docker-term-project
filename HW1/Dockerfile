FROM python:latest
#MAINTAINER Dr.sungwon "drsungwon@khu.ac.kr"
LABEL name="Dr.sungwon"
LABEL email="drsungwon@khu.ac.kr"
COPY . /app
RUN apt-get update
RUN echo "this is a python web server container"
CMD ["python", "/app/webserver.py"]
EXPOSE 9000