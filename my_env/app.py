from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greeting.html', name=name)
    return render_template('index.html')

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
