from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum', methods=['POST'])
def calculate_sum():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2 +1
        return render_template('result.html', num1=num1, num2=num2, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
