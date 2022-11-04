from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "RSVP App Home Page"
    greeting = "Welcome to the Home Page"
    return render_template('index.html', name = name, greeting = greeting)

@app.route('/about')
def about():
    name = "RSVP App About Page"
    greeting = "Welcome to the About Page"
    return render_template('about.html', name = name, greeting = greeting)
    
if __name__ == '__main__':
    app.run(debug=True)