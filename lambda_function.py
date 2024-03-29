import numpy as np
from flask import Flask, render_template, request
import pickle

def handler(event, context):
    application = Flask(__name__)
    model = pickle.load(open('model.pkl', 'rb'))

    @application.route('/')
    def index():
        return render_template('index.html')

    @application.route('/predict',methods=['GET','POST'])
    def predict():
        print('hi')
        '''
        For rendering results on HTML GUI
        '''
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


    if __name__ == "__main__":
        application.run(host='0.0.0.0', port=5000)