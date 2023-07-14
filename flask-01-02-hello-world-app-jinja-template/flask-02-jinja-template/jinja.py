from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def head():
    return render_template('index.html', number1=888888, number2=9999)


@app.route('/mult')

def number():
    x=879
    y=978
    return render_template('body.html', num1=x, num2=y, mult=x*y)

if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(host= '0.0.0.0', port=80)