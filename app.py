"""Import necessary libraries."""
import sqlite3
from flask import Flask, jsonify, json, render_template
from flask import request, url_for, redirect, flash
from werkzeug.exceptions import abort, HTTPException
import logging
from datetime import datetime

# Function to get a database connection.
# This function connects to database with the name `database.db`
conn_counter = 0


def get_datetime():
    """Get the current time in the given FORMAT."""
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y, %H:%M:%S,")

    return dt_string


def get_db_connection():
    """Link to database."""
    global conn_counter
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    conn_counter += 1

    return connection


# Function to get a post using its ID
def get_post(post_id):
    """To get the post using its ID."""
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                              (post_id,)).fetchone()
    connection.close()
    return post


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# Define the main route of the web application
@app.route('/')
def index():
    """Index endpoint."""
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>', methods=['GET'])
def post(post_id):
    """Post endpoint."""
    post = get_post(post_id)
    dt = get_datetime()
    if post is None:
        # add log info
        app.logger.info('\033[1;31m{} This is not an existing article. Pleae check again.'.format(dt))
        return render_template('404.html'), 404
    else:
        # add log info
        app.logger.info('{} Article "{}" retrieved!'.format(dt, post['title']))
        return render_template('post.html', post=post)


# Define the About Us page
@app.route('/about')
def about():
    """About endpont."""
    dt = get_datetime()
    # add log info
    app.logger.info(f'{dt} the "About Us" page is retrieved.')
    return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
    """Creation of new post endpoint."""
    dt = get_datetime()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # add log info
        app.logger.info('{} The new article '.format(dt) + '\033[1;32m"{}"'.format(title) + "\033[1;37m has been posted!")

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                               (title, content))
            connection.commit()
            connection.close()

            return redirect(url_for('index'))

    return render_template('create.html')


# to build the /healthz endpoint for the TechTrends application.
@app.route('/healthz')
def healthz():
    """Healthcheck endpoint."""
    response = app.response_class(
                response=json.dumps({"result": " OK - healthy"}),
                status=200,
                mimetype="application/json"
                )
    return response


# to build the /metrics endpoint
@app.route('/metrics')
def metrics():
    """Metrics endpoint."""
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()

    response = app.response_class(
                response=json.dumps({"status": "success",
                                     "code": 0,
                                     "data": {"db_connection_count": conn_counter,
                                              "post_count": len(posts)}}),
                status=200,
                mimetype="application/json")
    return response


# to add Dynamic Healthcheck endpoint
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()

    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


# start the application on port 3111
if __name__ == "__main__":
    # Stream logs to a file, and set the default log level to DEBUG
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port='3111')
