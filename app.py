# import pandas as pd
# from flask import Flask, request, render_template
# import pickle

# app = Flask(__name__)

# model = pickle.load(open('models/modelL.pkl', 'rb'))
# scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():
#     features = {
#         'INT_SQFT': 0,
#         'N_BEDROOM': 0,
#         'N_BATHROOM': 0,
#         'AREA_Adyar': 0,
#         'AREA_Anna Nagar': 0,
#         'AREA_Chrompet': 0,
#         'AREA_KK Nagar': 0,
#         'AREA_Karapakam': 0,
#         'AREA_T Nagar': 0,
#         'AREA_Velachery': 0,
#         'PARK_FACIL_No': 0,
#         'PARK_FACIL_Yes': 0,
#         'BUILDTYPE_Commercial': 0,
#         'BUILDTYPE_House': 0,
#         'BUILDTYPE_Others': 0,
#         'UTILITY_AVAIL_No': 0,
#         'UTILITY_AVAIL_Yes': 0,
#         'STREET_Gravel': 0,
#         'STREET_No Access': 0,
#         'STREET_Paved': 0
#     }

#     features['INT_SQFT'] = [int(request.form['sqft'])]
#     features['N_BEDROOM'] = [int(request.form['bedrooms'])]
#     features['N_BATHROOM'] = [int(request.form['bathrooms'])]
#     features['AREA_' + request.form['location']] = [1]
#     features['PARK_FACIL_' + ('Yes' if 'parking' in request.form else 'No')] = [1]
#     features['BUILDTYPE_' + request.form['building-type']] = [1]
#     features['UTILITY_AVAIL_' + ('Yes' if 'utility' in request.form else 'No')] = [1]
#     features['STREET_' + request.form['street-type']] = [1]

#     sample_df = pd.DataFrame(features)
#     scaled_sample = scaler.transform(sample_df)
#     prediction = model.predict(scaled_sample)
#     return render_template('index.html', prediction_text='Predicted Price: {}'.format(prediction))


# if __name__ == "__main__":
#     app.run()

from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('models/model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    form_data = request.form

    # Create a dictionary with default values for all features
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

    # Convert the dictionary to a DataFrame
    sample_df = pd.DataFrame.from_dict(features)

    # Scale the sample data
    scaled_sample = scaler.transform(sample_df)

    # Make the prediction
    prediction = model.predict(scaled_sample)

    # Return the prediction result
    return render_template('index.html', prediction_text='Predicted Price: {}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)
