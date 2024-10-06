from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Return the parameter to the browser

@app.route('/count/<int:parameter>')
def count(parameter):
    result = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        'div': num1 / num2 if num2 != 0 else 'Division by zero error',
        '%': num1 % num2
    }

    result = operations.get(operation, 'Invalid operation')
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
