# INTEGRATED AGRICULTURAL DECISION SUPPORT SYSTEM
# Developed by Jisnu, Dharaneesh and Krishneth

import numpy as np
import joblib

# Algorithm used for training the model: Decision Tree Learning

def YieldPrediction(state, district, season, crop, area):
    # Load the saved model
    
    # print("\n\n")
    # print("=================== CROP YIELD PREDICTION =======================")

    loaded_model = joblib.load('yield_prediction_model_tn.joblib')#yield_prediction_model_tn.joblib

    # Load the saved OneHotEncoder
    loaded_encoder = joblib.load('ohe_yield_prediction.joblib')#ohe_yield_prediction.joblib

    # Get the user inputs for testing

    user_input = np.array([['Tamil Nadu', district, season, crop, area]])
    # print(user_input)

    # user_input = np.array([['Tamil Nadu', 'ERODE', 'Kharif', 'Rice', 55347]])

    #['Tamil Nadu', 'ERODE', 'Kharif', 'Rice', 55347]

    # Convert the categorical columns to one-hot encoding using the loaded encoder
    user_input_categorical = loaded_encoder.transform(user_input[:, :4])

    # Combine the one-hot encoded categorical columns and numerical columns
    user_input_final = np.hstack((user_input_categorical.toarray(), user_input[:, 4:].astype(float)))

    # Make the prediction using the loaded model
    prediction = loaded_model.predict(user_input_final)

    # Print the prediction
    #print(f"Prediction: {prediction[0]}")
    print(prediction[0])
    return prediction[0]

# Input parameters:

# State name
# District Name
# Season
# Crop Name
# Area

# Function call
# predicted_yield = YieldPrediction('Tamil Nadu', 'ERODE', 'Kharif', 'Rice', 55347)
# print("Predicted Yield Value: ", predicted_yield)