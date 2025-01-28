from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods =['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/projects', methods =['GET','POST'])
def projects():
    return render_template('projects.html')

@app.route('/resume', methods =['GET','POST'])
def resume():
    return render_template('resume.html')

# @app.route('/', methods =['GET','POST'])
# def about():
#     return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)
