## Docker commands used to build the application 
# TODO: insert the docker build command
FROM python:3.8

# Set current working directory
WORKDIR /home/tensorflow/nd064_course_1/project/techtrends

COPY . .

RUN pip install -r requirements.txt && python3 init_db.py 

EXPOSE 3111

CMD ["python3","app.py"]

## Docker commands used to run the application
# TODO: insert the docker run command

## Docker commands used to get the application logs
# TODO: insert the docker logs command

## Logs from the container running the TechTrends application
# TODO: paste logs from the Docker container 
