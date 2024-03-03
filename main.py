from District_Crop_Recommendation_Testing import Question, Leaf, Decision_Node, print_tree, print_leaf, classify, class_counts, DistrictCropRecommendation
from Yield_Prediction_Testing import YieldPrediction
from Soil_Crop_Recommendation_Testing import SoilCropPrediction
from District_Crop_Recommendation_Testing import DistrictCropRecommendation
#from Decision_Tree_DCR import Question, Leaf, Decision_Node, class_counts, print_tree, print_leaf, classify

crops = []
crops = DistrictCropRecommendation("Tamil Nadu", "COIMBATORE", "Kharif")
print(crops)

predicted_crop, city, curr_temperature, curr_humidity = SoilCropPrediction(0, 11, 101, 10.2, 100)
print("\nCrop Prediction based on Soil Conditions")
print("\n", predicted_crop, city,  curr_temperature, curr_humidity)

predicted_yield = YieldPrediction('Tamil Nadu', 'ERODE', 'Kharif', 'Rice', 55347)
print("Predicted Yield Value: ", predicted_yield)