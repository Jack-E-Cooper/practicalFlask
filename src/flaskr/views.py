from flask import render_template

@app.route('/')
def index():
    return render_template('home.html', title='home page')

@app.route('/msg')
def msg():
    return render_template('msgexample.html', title='Message Page', \
        name='John Doe', messages=['Hello', 'Hi', 'Hey'])

@app.route('/blog')
def blog():
    return render_template('blog.html', title='blog page')

@app.route('/about')
def about():
    return render_template('about.html', title='about page')
