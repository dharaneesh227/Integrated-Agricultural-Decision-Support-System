# INTEGRATED AGRICULTURAL DECISION SUPPORT SYSTEM
# Developed by Jisnu, Dharaneesh and Krishneth

import pickle
import numpy as np
import requests, json

# Algorithm used for training the model: Naive Bayes Classifier -> Classifies into 22 classes of crops

def SoilCropPrediction(n, p, k, ph, rainfall,latitude,longitude):
    # res = requests.get('https://ipinfo.io/')
    # data = res.json()
    # print("\n\n")
    # print("=================== CROP RECOMMENDATION BASED ON SOIL CONDITIONS =======================")
    # city = data['city']
    # print("Current Location:    ", city)
    # location = data['loc'].split(',')
    # latitude = location[0]
    # print("Latitude:   ", latitude)
    # longitude = location[1]
    # print("Longitude:   ", longitude)

    api_key = "5b2691c07d8a7d9776ffb21270ca7474"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "lat=" + latitude + "&lon=" + longitude +  "&appid=" + api_key
    # print(complete_url)

    response = requests.get(complete_url)
    #print(response)

    x = response.json()
    #print(x)

    # Default temperature and humidity values
    current_temperature = 24
    current_humidity = 49

    if x["cod"] != "404":
        y = x["main"]
        current_temperature =round((y["temp"]-273), 2)
        #current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        # print("Temperature(C) = " + str(current_temperature) + "\nHumidity(%) = " + str(current_humidity))
    # else:
        # print("City Not Found ")

    # For displaying use: 
    # Current temperature of the city : current_temperature
    # Current humidity of the city: current_humidity
    # Current raifall of the city: current_rainfall
    # Current city name: city

    loaded_model = pickle.load(open('NBClassifier.pkl', 'rb'))

    # data = np.array([[83, 45, 60, 28, 70.3, 7.0, 150.9]])
    # Array Format => [N, P, K, Temperature, Humidity, pH, Rainfall]
    # Current Coimbatore soil features
    # N, P, K, pH variables
    # N = 62
    # P = 52
    # K = 16
    # pH = 6.2
    # current_rainfall = 200
    data = np.array([[n, p, k, current_temperature, current_humidity, ph, rainfall]])
    prediction = loaded_model.predict(data)
    print(prediction)
    #Final Crop prediction result variable => prediction
    #print("\nSuitable crop for given soil conditions: ", prediction[0], "\n\n")

    # return prediction[0], city, current_temperature, current_humidity
    return prediction[0], current_temperature, current_humidity

#pred, cit, curt, curhum = crop_recommendation(62, 52, 26, 6.2, 200)
#pred, cit, curt, curhum = crop_recommendation(22, 36, 48, 8.2, 120)

# Input parameters
# ================
# Nitrogen Content
# Phosphorous Content
# Potassium Content
# pH of the Soil
# Current Rainfall of the area/district

#Input parameters Format => (N, P, K, Temperature, Humidity, pH, Rainfall)

# predicted_crop, city, curr_temperature, curr_humidity = SoilCropPrediction(0, 11, 101, 10.2, 100)
# print("\nCrop Prediction based on Soil Conditions")
# print("\n", predicted_crop, city,  curr_temperature, curr_humidity)

# Output parameters
# =================
# Recommended crop
# City name
# Temperature
# Humidity