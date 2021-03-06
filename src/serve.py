from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Greetings from Mustafa's simple Flask App!"
    return render_template('index.html', message=message)
    
app.run(host='0.0.0.0', port=8000)

# run the application
if __name__ == "__main__":
    app.run(debug=True)