import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image

# Load trained model
rfc = pickle.load(open('rfc.pkl', 'rb'))

cover_type_dict={
            1:{'name':'Spruce/Fir','image':'spruce-fir.png'},
            2:{'name':'Lodgepole Pine','image':'lodgepole pine.jpg'},
            3:{'name':'Ponderosa Pine','image':'Ponderosa pine.jpg'},
            4:{'name':'Cottonwood/Willow','image':'cottonwood.jpg'},
            5:{'name':'Aspen','image':'aspen.jpg'},
            6:{'name':'Douglas-fir','image':'dougas-fir.jpg'},
            7:{'name':'Krummholz','image':'krummholz.jpg'}
        }

# App title
st.title("Forest Cover Type Prediction 🌳🌲")

st.write("Enter all cover type features separated by commas (no spaces).")
st.write("Example: 2596,51,3,258,0,510,221,232,148,6279,6225,148,6279,6225,0,0,0,0")

# User input
user_input = st.text_input('Enter features:')

if st.button("Predict"):
    if not user_input.strip():
        st.error("Please enter the features before clicking Predict.")
    else:
        try:
            # Convert input string to a numpy array
            features_list = user_input.strip().split(',')

            features = np.array(features_list, dtype=np.float64).reshape(1, -1)

            # Prediction
            prediction = rfc.predict(features)[0]
            st.success(f"\n\nPredicted Forest Cover Type: {prediction}")

        except Exception as e:
            st.error(f"Error: {e}")




    cover_type_info=cover_type_dict.get(prediction)

    if cover_type_info is not None:
        forest_name=cover_type_info['name']
        forest_image=cover_type_info['image']

        col1,col2=st.columns([2,3])
        with col1:
            st.write('\n\n\nThis is predict cover type')
            st.write(f"<h1 style='font-size:50px;font-weight:bold;'>{forest_name}</h1>",unsafe_allow_html=True)
        with col2:
            final_image=Image.open(forest_image)
            st.image(final_image,caption=forest_name,use_container_width=True)