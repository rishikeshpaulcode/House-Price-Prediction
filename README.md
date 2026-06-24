# House Price Predictor App

A Streamlit-based Indian house price prediction app built with a trained Random Forest model. The model is fully trained on Indian real estate data and predicts house prices based on property details such as location, transaction type, ownership, furnishing, floor information, and area.

## Key Features

- Predicts Indian residential property prices using a Random Forest regression model
- Interactive Streamlit interface for easy input of property features
- Supports Indian-specific categories like location, transaction type, ownership, furnishing, and facing direction
- Handles multi-option overlooking choices like garden, park, or pool
- Converts user inputs into model-ready numeric features automatically

## Links
- Kaggle notebook: https://www.kaggle.com/code/rishikeshpaul/house-price-prediction
- Streamlit app: https://house-price-prediction-8iotgqez6uangh5cvngnjv.streamlit.app

## Files Included

- `app.py` — main Streamlit app that loads the model, displays the UI, and returns predictions
- `requirements.txt` — Python dependencies required to run the app
- `src/categories.json` — source of valid category values used by the app
- `src/House_Price_Predictor.pkl` — serialized Random Forest model used for prediction

## Requirements

- Python 3.8+ (recommended)
- `pip` installed

## Installation

1. Create or activate a Python virtual environment.
2. Install required packages:

```bash
pip install -r requirements.txt
```

## Running the App

From the project directory, launch Streamlit:

```bash
streamlit run app.py
```

Then open the local URL shown in your browser to use the house price predictor.

## How It Works

The app collects the following property inputs:

- Location
- Type of transaction
- Ownership type
- Furnishing type
- Facing direction
- Overlooking options
- Total floors
- User floor
- Number of bathrooms
- Number of balconies
- Number of parking spaces
- Carpet area

These inputs are transformed into a numeric feature vector. The trained Random Forest model uses this information to estimate a house price for Indian real estate.

## Notes

- The model is trained specifically on Indian property data, so it is intended for Indian housing market predictions.
- Predictions are returned in Indian currency format:
  - Values below 1 crore are shown in lakhs
  - Values of 1 crore or greater are shown in crores
