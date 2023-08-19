from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the sorted results from the .pkl file
sorted_results = pd.read_pickle('model/final_sorted_results.h5')

@app.route('/')
def home():
    return "Welcome to the Hotel Best Review Finder Prediction API!"

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    sorted_by = request.args.get('sorted')
    city_filter = request.args.get('city')
    
    if city_filter is None:
        return jsonify({"error": "City parameter is missing."}), 400
    
    if sorted_by is None:
        return jsonify({"error": "Sorting parameter is missing."}), 400
    
    filtered_results = sorted_results[sorted_results["City"] == city_filter]
    
    sorted_results_filtered = []
    
    if sorted_by == "food":
        sorted_results_filtered = filtered_results.sort_values(by="Food_Prediction", ascending=False)
    elif sorted_by == "staff":
        sorted_results_filtered = filtered_results.sort_values(by="Staff_Prediction", ascending=False)
    elif sorted_by == "env":
        sorted_results_filtered = filtered_results.sort_values(by="Environment_Prediction", ascending=False)    

    result_data = sorted_results_filtered.to_dict(orient='records')
    return jsonify(result_data)

@app.route('/get_most_review_food', methods=['GET'])
def get_most_reviews_food():
    food_filter = request.args.get('food')
    
    if food_filter is None:
        return jsonify({"error": "Food parameter is missing."}), 400
    
    filtered_results = sorted_results[sorted_results["Most_reviewed_foods"] == food_filter]

    sorted_results_filtered = filtered_results.sort_values(by="Food_Prediction", ascending=False)
        
    result_data = sorted_results_filtered.to_dict(orient='records')
    return jsonify(result_data)

if __name__ == '__main__':
    app.run(debug=True)
