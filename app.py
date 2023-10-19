import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.preprocessing import LabelEncoder


# Load the pickled model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)



def encode_yes_no_features(data):
   

    yes_no_features = ['Skin darkening (Y/N)', 'hair growth(Y/N)', 'Weight gain(Y/N)', 'Fast food (Y/N)', 'Pimples(Y/N)']

    for feature in yes_no_features:
        encoder = LabelEncoder()
        data[feature] = encoder.fit_transform(data[feature])

    return data

# Create a function to make predictions and returns the probability of one having PCOS
def make_prediction(follicle_no_r, follicle_no_l, skin_darkening, hair_growth, weight_gain, cycle, fast_food, pimples, amh, weight):


    data = pd.DataFrame({
        'Follicle No. (R)': [follicle_no_r],
        'Follicle No. (L)': [follicle_no_l],
        'Skin darkening (Y/N)': [skin_darkening],
        'hair growth(Y/N)': [hair_growth],
        'Weight gain(Y/N)': [weight_gain],
        'Cycle(R/I)': [cycle],
        'Fast food (Y/N)': [fast_food],
        'Pimples(Y/N)': [pimples],
        'AMH(ng/mL)': [amh],
        'Weight': [weight],
    })

    data = encode_yes_no_features(data)

    prediction = model.predict_proba(data)[0][1]
    return prediction


# Create a Streamlit app
st.title('Ovary Oracle')

# Get the user's input
follicle_no_r = st.number_input('Follicle No. (R)')
follicle_no_l = st.number_input('Follicle No. (L)')
skin_darkening = st.selectbox('Skin darkening (Y/N)', ['Y', 'N'])
hair_growth = st.selectbox('hair growth(Y/N)', ['Y', 'N'])
weight_gain = st.selectbox('Weight gain(Y/N)', ['Y', 'N'])
cycle = st.number_input('Cycle(R/I)')
fast_food = st.selectbox('Fast food (Y/N)', ['Y', 'N'])
pimples = st.selectbox('Pimples(Y/N)', ['Y', 'N'])
amh = st.number_input('AMH(ng/mL)')
weight = st.number_input('Weight')

# Make a prediction
prediction = make_prediction(follicle_no_r, follicle_no_l, skin_darkening, hair_growth, weight_gain, cycle, fast_food, pimples, amh, weight)

# Display the prediction
if st.button('Run Model'):
    prediction = make_prediction(follicle_no_r, follicle_no_l, skin_darkening, hair_growth, weight_gain, cycle, fast_food, pimples, amh, weight)

    st.write('Prediction:')
    st.write(prediction)

# Deploy the app
if __name__ == '__main__':
    st.code('app.py') 