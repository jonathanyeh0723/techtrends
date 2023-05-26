# Initializes a new build stage and sets the Base Image as python 3.8-alpine
FROM python:3.8-alpine

# To set current working directory as /app
WORKDIR /app 

# To first handle requirements.txt first to ensure our app has all its dependencies installed.
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install curl. It's a URL retrieval (download/upload) command-line utility and library. It is free software for Alpine Linux.
RUN apk --no-cache add curl

# Copying new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
# To execute any commands in a new layer on top of the current image and commit the results.
# RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux)
COPY app/ .
RUN python3 init_db.py

# To inform Docker that the container listens on the specified network ports at runtime.
# Expose the port that aligns what app.py published - app.run(host='0.0.0.0', port='3111')
EXPOSE 3111

# To provide defaults (ENTRYPOINT) for an executing container.
CMD ["python3","app.py"]

