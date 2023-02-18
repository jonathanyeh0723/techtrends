# Initializes a new build stage and sets the Base Image as python 3.8 version
FROM python:3.8

# To set current working directory
WORKDIR /home/tensorflow/nd064_course_1/project/techtrends

# Copying new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
COPY . .

# To execute any commands in a new layer on top of the current image and commit the results.
# RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux)
RUN pip install -r requirements.txt && python3 init_db.py 

# To inform Docker that the container listens on the specified network ports at runtime.
EXPOSE 3111

# To provide defaults (ENTRYPOINT) for an executing container.
CMD ["python3","app.py"]

