import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
modelfile=open('modelL.pkl','rb')
model=pickle.load(modelfile)
sample_input={
    'INT_SQFT': [1500],
    'N_BEDROOM': [3],
    'N_BATHROOM': [2],
    'AREA_Adyar': [0],
    'AREA_Anna Nagar': [0],
    'AREA_Chrompet': [0],
    'AREA_KK Nagar': [0],
    'AREA_Karapakam': [0],
    'AREA_T Nagar': [1],
    'AREA_Velachery': [0],
    'PARK_FACIL_No': [0],
    'PARK_FACIL_Yes': [1],
    'BUILDTYPE_Commercial': [1],
    'BUILDTYPE_House': [0],
    'BUILDTYPE_Others': [0],
    'UTILITY_AVAIL_No': [0],
    'UTILITY_AVAIL_Yes': [1],
    'STREET_Gravel': [0],
    'STREET_No Access': [0],
    'STREET_Paved': [1]
}
sample_df=pd.DataFrame(sample_input)
scaler = pickle.load(open('scaler.pkl', 'rb'))
scaled_sample = scaler.transform(sample_df)
predictions=model.predict(scaled_sample)
print("Predicted Sale Price:",predictions)