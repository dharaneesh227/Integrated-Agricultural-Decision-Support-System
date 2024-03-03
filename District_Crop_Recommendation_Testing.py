import joblib
from Decision_Tree_DCR import Question, Leaf, Decision_Node, class_counts, print_tree, print_leaf, classify

def DistrictCropRecommendation(state, district, season):

    # print("\n\n")
    # print("=================== CROP RECOMMENDATION BASED DISTRICT AND SEASON =======================")

    dt_model_final = joblib.load('D:\mini project\sem8\Flask Server\district_crops.pkl')

    testing_data = [[state, district, season]]

    for row in testing_data:
        Predict_dict = (print_leaf(classify(row, dt_model_final))).copy()

    crop_list = []

    for key, value in Predict_dict.items():
        if int(value) > 5:
            crop_list.append(key)
    return crop_list

# Function Call
# Input Parameters => state, district, season
# crops = district_crop_recommendation("Tamil Nadu", "COIMBATORE", "Kharif")
# print(crops)
