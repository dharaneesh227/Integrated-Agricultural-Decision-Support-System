from flask import Flask, render_template, request, jsonify
from District_Crop_Recommendation_Testing import DistrictCropRecommendation
from Decision_Tree_DCR import Question, Leaf, Decision_Node, class_counts, print_tree, print_leaf, classify
from Soil_Crop_Recommendation_Testing import SoilCropPrediction
from Yield_Prediction_Testing import YieldPrediction
from Price_Prediction_Testing import PricePrediction
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop_recommendation', methods=['POST', 'GET'])
def crop_recommendation():
    if request.method == 'POST':
        data=request.get_json()
        # print(data)
        state = data['state']
        district = data['district']
        season = data['season']

        crops = DistrictCropRecommendation(state, district, season)
        # return render_template('crop_recommendation_result.html', crops=crops)
        return jsonify(crops)
    # return render_template('crop_recommendation.html')
    return None


@app.route('/soil_crop_prediction', methods=['POST', 'GET'])
def soil_crop_prediction():
    if request.method == 'POST':
        data=request.get_json()
        # print(data)
        param1 = float(data['param1'])
        param2 = float(data['param2'])
        param3 = float(data['param3'])
        param4 = float(data['param4'])
        param5 = float(data['param5'])

        predicted_crop, city, curr_temperature, curr_humidity = SoilCropPrediction(param1, param2, param3, param4, param5)
        # return render_template('soil_crop_prediction_result.html', predicted_crop=predicted_crop, city=city,curr_temperature=curr_temperature, curr_humidity=curr_humidity)
        return jsonify(predicted_crop, city, curr_temperature, curr_humidity)
    # return render_template('soil_crop_prediction.html')
    return None


@app.route('/yield_prediction', methods=['POST', 'GET'])
def yield_prediction():
    if request.method == 'POST':
        data=request.get_json()
        # print(data)
        state = data['state']
        district = data['district']
        season = data['season']
        crop = data['crop']
        param1 = data['param1']

        predicted_yield = YieldPrediction(state, district, season, crop, param1)
        # return render_template('yield_prediction_result.html', predicted_yield=predicted_yield)
        return jsonify(predicted_yield)
    # return render_template('yield_prediction.html')
    return None

@app.route('/price_prediction', methods=['POST', 'GET'])
def crop_price_prediction():
    if request.method == 'POST':
        data=request.get_json()
        print(data)
        crop = data['crop']
        max, min, cur, forecast_val = PricePrediction(crop)
        # return render_template('crop_price_prediction_result.html', max=max, min=min, cur=cur, forecast_val=forecast_val)
        return jsonify(max, min, cur, forecast_val)
    # return render_template('crop_price_prediction.html')
    return None

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
