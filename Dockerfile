FROM python:3.8

# Set current working directory
WORKDIR /home/tensorflow/nd064_course_1/project/techtrends

COPY . .

RUN pip install -r requirements.txt && python3 init_db.py 

EXPOSE 3111

CMD ["python3","app.py"]

