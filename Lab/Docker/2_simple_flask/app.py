from flask import Flask, render_template, json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/index')
def index_page():
    return render_template('index.html')


@app.route('/healthz')
def healthz():

    # Using flask response_class methodd 
    # response assigned to json.dumps({"key": "value"}) 
    # 200 OK status code means that the request was successful
    # but the meaning of success depends on the request method
    # A media type (formerly known as a MIME type) is a two-part identifier
    # for file formats and format contents transmitted on the Internet.
    response = app.response_class(
            response=json.dumps({"result": "OK - Healthy!"}),
            status=200,
            mimetype="application/json"
            )

    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')

