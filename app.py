from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
model = pickle.load(open('models/model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict_page')
def predict_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form
    features = {
        'INT_SQFT': [int(form_data.get('sqft', 0))],
        'N_BEDROOM': [int(form_data.get('bedrooms', 0))],
        'N_BATHROOM': [int(form_data.get('bathrooms', 0))],
        'AREA_Adyar': [1 if form_data.get('location') == 'adyar' else 0],
        'AREA_Anna Nagar': [1 if form_data.get('location') == 'annanagar' else 0],
        'AREA_Chrompet': [1 if form_data.get('location') == 'Chrompet' else 0],
        'AREA_KK Nagar': [1 if form_data.get('location') == 'KKnagar' else 0],
        'AREA_Karapakam': [1 if form_data.get('location') == 'Karapakam' else 0],
        'AREA_T Nagar': [1 if form_data.get('location') == 'Tnagar' else 0],
        'AREA_Velachery': [1 if form_data.get('location') == 'Velachery' else 0],
        'PARK_FACIL_No': [1 if form_data.get('parking') == 'No' else 0],
        'PARK_FACIL_Yes': [1 if form_data.get('parking') == 'Yes' else 0],
        'BUILDTYPE_Commercial': [1 if form_data.get('building-type') == 'commercial' else 0],
        'BUILDTYPE_House': [1 if form_data.get('building-type') == 'residential' else 0],
        'BUILDTYPE_Others': [1 if form_data.get('building-type') == 'others' else 0],
        'UTILITY_AVAIL_No': [1 if form_data.get('utility') == 'No' else 0],
        'UTILITY_AVAIL_Yes': [1 if form_data.get('utility') == 'Yes' else 0],
        'STREET_Gravel': [1 if form_data.get('street-type') == 'gravel' else 0],
        'STREET_No Access': [1 if form_data.get('street-type') == 'no-access' else 0],
        'STREET_Paved': [1 if form_data.get('street-type') == 'paved' else 0]
    }

    sample_df = pd.DataFrame.from_dict(features)
    scaled_sample = scaler.transform(sample_df)
    prediction = model.predict(scaled_sample)
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)