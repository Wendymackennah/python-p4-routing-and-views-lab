#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)





@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:count_parameter>')
def count(count_parameter):
    counts = ""
    for num in range(count_parameter):
        counts += str(num) + "\n"
        print(num)
    return counts

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation!'
    
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)










