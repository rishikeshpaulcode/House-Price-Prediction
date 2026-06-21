# import packages
import streamlit as st
import numpy as np
import json
import pickle

# create custom styles
st.markdown(
    '''
    <style>
        div.stButton > button p {
            font-size: 21px !important;
            forn-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <style>
        div[data-testid="stSelectbox"] label[data-testid="stWidgetLabel"] p {
            font-size: 22px !important;
            font-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <style>
        div[data-testid="stNumberInput"] label[data-testid="stWidgetLabel"] p {
            font-size: 22px !important;
            font-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <style>
        .st-key-Pill1 label[data-testid="stWidgetLabel"] p,
        .st-key-Pill2 label[data-testid="stWidgetLabel"] p {
            font-size: 22px !important;
            font-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

# get unique categories of each feature
with open("./src/categories.json", "r") as file:
    categories = json.load(file)

# load the model
with open("./src/House_Price_Predictor.pkl", "rb") as file:
    model = pickle.load(file)

# function to transform given input to numeric
def to_numeric(input_dict):
    feature_vals = []
    feature_vals.append(categories["Location"].index(input_dict["location"]))
    feature_vals.append(categories["Transaction"].index(input_dict["transaction_type"]))
    feature_vals.append(categories["Ownership"].index(input_dict["ownership_type"]))
    feature_vals.append(categories["Furnishing"].index(input_dict["furnish_type"]))
    feature_vals.append(categories["Facing"].index(input_dict["face_direction"]))

    if "Garden" in input_dict["overlookings"] or "Park" in input_dict["overlookings"] or "Scenery" in input_dict["overlookings"]:
        feature_vals.append(1)
    else:
        feature_vals.append(0)
    
    if "Main Road" in input_dict["overlookings"]:
        feature_vals.append(1)
    else:
        feature_vals.append(0)
    
    if "Pool" in input_dict["overlookings"] or "Lake" in input_dict["overlookings"] or "Sea" in input_dict["overlookings"]:
        feature_vals.append(1)
    else:
        feature_vals.append(0)
    
    feature_vals.append(input_dict["user_floor"] / input_dict["total_floors"])
    feature_vals.append(input_dict["total_floors"])
    feature_vals.append(input_dict["num_bathroom"])
    feature_vals.append(input_dict["num_balcony"])
    feature_vals.append(input_dict["num_parking"])
    feature_vals.append(input_dict["carpet_area"])

    return np.array(feature_vals)[np.newaxis, :]


if __name__ == "__main__":
    # display header and description
    st.title(":house: House Price Predictor")
    st.write("This model predicts indian house prices by acting like a large committee of real estate experts, where each makes a guess based on property details like size and location.")

    # create form to get independent features
    input_dict = {}
    input_dict["location"] = st.selectbox("Location:", options=categories["Location"])
    input_dict["transaction_type"] = st.selectbox("Type of Transaction:", options=categories["Transaction"])
    input_dict["ownership_type"] = st.selectbox("Type of Ownership:", options=categories["Ownership"])
    input_dict["furnish_type"] = st.selectbox("Type of Furnishing:",options=categories["Furnishing"])
    input_dict["face_direction"] = st.pills("Face Direction:", options=categories["Facing"], selection_mode="single", key="Pill1")
    input_dict["overlookings"] = st.pills("Overlooking:", options=categories["Overlooking"], selection_mode="multi", key="Pill2")
    input_dict["total_floors"] = st.number_input("Total Floors:", min_value=1, value="min", step=1)
    input_dict["user_floor"] = st.number_input("Your Floor:", min_value=1, max_value=input_dict['total_floors'], value="min", step=1)
    input_dict["num_bathroom"] = st.number_input("Number of Bathrooms:", min_value=0, value="min", step=1)
    input_dict["num_balcony"] = st.number_input("Number of Balconies:", min_value=0, value="min", step=1)
    input_dict["num_parking"] = st.number_input("Number of Car Parkings:", min_value=0, value="min", step=1)
    input_dict["carpet_area"] = st.number_input("Total Carpet Area:", value=0.0, format="%.2f")
    st.divider()

    # get prediction when button is pressed
    if st.button("Get Price", type="primary"):
        input_values = to_numeric(input_dict)
        predicted_price = model.predict(input_values)[0]

        st.write("Predicted Price:")
        if predicted_price < 1:
            st.header(f"\u20B9 {round(predicted_price * 100, 2)} Lac")
        else:
            st.header(f"\u20B9 {round(predicted_price, 2)} Cr")
