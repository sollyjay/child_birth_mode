import streamlit as st
import pandas as pd
import numpy as np
import joblib

filename = 'Delivery_Model_GBC.pkl'
load_model = joblib.load(open(filename,"rb"))
test_input = [14400,20,0,0,8.140000,-10.500000,232,974204,7.14,6]


def prediction_model(input):
    input_data = input
    feat = ['II.stage','NoProgress','CK/KP','BDecf','BE','I.stage','pH','Apgar1']
    
    input_data_nd = np.asarray(input_data)
    ty = input_data_nd.reshape(-1, len(input_data))
    input_data_df = pd.DataFrame(ty, columns=feat)
    prediction = load_model.predict(ty)
    if prediction[0] == 1:
        return "Vaginal Birth"
    else:
        return "Caeserean Section"

def main():
    st.title("Mode of Childbirth Delivery")

    stage_ = st.text_input('Stage I of Labour')
    stage = st.text_input('Stage II of Labour')
    progress = st.radio("No Progress in Labour", ('Progress', 'No Progress'))
    ck = st.radio("Creatine Kinase - CK/KP", ('High Level', 'Low Level'))
    bd = st.text_input('Base eficit in extracellular fluid (BDecf)')
    be = st.text_input('Base excess (BE)')
    ph = st.slider('Potential of Hydrogen (pH)', 0.0, 14.0, 7.14)
    apgar = st.slider('Apgar Score', 0, 10, 5)
    
    progress_val = None
    if progress == 'Progress':
        progress_val = 1
    else:
        progress_val = 0

    ck_val = None
    if ck == 'High Level':
        ck_val = 1
    else:
        ck_val = 0

    diagnose = ''
    features = [stage, bd, be, stage_, apgar]
    input_features = [stage, progress_val, ck_val, bd, be, stage_, ph, apgar]
    
    if st.button("Check Mode"):
        if len(features[0]) > 0 and len(features[1]) > 0 and len(features[2]) > 0 and len(features[3]) > 0 and len(features[4]) > 0:
            diagnose = prediction_model(input_features)
            st.success(diagnose)
        elif progress_val != None and ck_val != None:
            st.error('Invalid progress input')
        else:
            st.error('Enter Input')

if __name__ == '__main__':
    main()
