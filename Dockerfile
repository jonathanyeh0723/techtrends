# Initializes a new build stage and sets the Base Image as python 3.8-alpine version
FROM python:3.8-alpine

# To set current working directory
WORKDIR .

# To first handle requirements.txt first to ensure our app has all its dependencies installed.
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copying new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
# To execute any commands in a new layer on top of the current image and commit the results.
# RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux)
COPY app/ .
RUN python3 init_db.py

# To inform Docker that the container listens on the specified network ports at runtime.
EXPOSE 3111

# To provide defaults (ENTRYPOINT) for an executing container.
CMD ["python3","app.py"]

