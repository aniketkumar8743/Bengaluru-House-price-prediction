from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
df = pd.read_csv(r"C:\Users\DELL\Cleaned_data.csv")
pipe = pickle.load(open("RidgeModel.pkl",'rb'))

@app.route('/')
def index():
    locations = sorted(df['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        locations = request.form.get('location')
        BHK = request.form.get('BHK')
        bath = request.form.get('bath')
        sqft = request.form.get('total_sqft')

        input = pd.DataFrame([[locations, sqft, bath, BHK]], columns=['location', 'total_sqft', 'bath', 'BHK'])
        prediction = pipe.predict(input)[0]
        return str(prediction)
    else:
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
