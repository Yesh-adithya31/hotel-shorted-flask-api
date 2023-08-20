<a name="readme-top"></a>


<!-- ABOUT THE PROJECT -->
## About The Project

This project create based on Hotel Details with Food Rating, Staff Ratings, Environment Ratings and Using Machine Learning RandomForestRegressor classifier and Get Best Rating Values For user selected content. Get Data from Flask-API
This Flask app provides a simple API for users to retrieve hotel reviews and predictions based on different criteria and sorting options. Users can make requests to the defined endpoints using query parameters in the URLs. You can run this app, and when you access the provided routes in a web browser or via tools like curl, you'll receive the JSON responses containing the review data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Here this project developement using Flask Framework.

* [![Flask][Flask-url]][Flask]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need to install `PYTHON_VERSION=3.9` upword version.
* python
  ```sh
  install latest python version
  ```

### Installation

_This is the step you have to follow._

1. Get a free API Key at [https://github.com/Yesh-adithya31/hotel-shorted-flask-api](https://github.com/Yesh-adithya31/hotel-shorted-flask-api)
2. Clone the repo
   ```sh
   git clone https://github.com/Yesh-adithya31/hotel-shorted-flask-api.git
   ```
3. Install PIP packages
   ```py
   pip install -r requirements.txt
   ```
4. Run cloned project `app.py`
   ```py
   python app.py
   ```
   `OR`
   
   ```py
   py app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Explanation

1. Import necessary modules:
    ```py
    from flask import Flask, request, jsonify
    import pandas as pd
    ```
    * `Flask`: Import the Flask framework to create your API.
    * `request`: Import the `request` object to access query parameters sent with the requests.
    * `jsonify`: Import the `jsonify` function to convert Python dictionaries to JSON format.
    * `pandas`: Import the Pandas library to work with data in tabular format.
      
2. Create a Flask app:
    ```py
    app = Flask(__name__)
    ```
    * `app = Flask(__name__)`: Create a Flask app instance.
      
3. Load sorted results:
    ```py
    # Load the sorted results from the .pkl file
    sorted_results = pd.read_pickle('model/final_sorted_results.h5')
    ```
    * `sorted_results = pd.read_pickle('model/final_sorted_results.h5')`: Load the sorted review results from a pickle file.
      
4. Define routes and functions for endpoints:
    ```py
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
    ```
    * `/`: Define the root route, which returns a simple welcome message.
    * `/get_reviews`: Define an endpoint to retrieve sorted and filtered reviews based on city and sorting criteria. The query parameters `city` and `sorted` are used to filter and sort the results.
           * The sorted_by parameter is used to determine the sorting criteria (`food`, `staff`, or `env`).
    * `/get_most_review_food`: Define an endpoint to retrieve reviews based on the most reviewed foods. The query parameter food is used to filter the results.
      
5. Implement functions for each endpoint:
    * For `/get_reviews`, you're handling the city filtering and sorting based on the `sorted` parameter. You use the Pandas DataFrame operations to filter and sort the data accordingly.
      example:
              #### Hotel-Sorted-API
              ```sh
                  https://hotel-shorted-flask-api.onrender.com/get_reviews?city=Colombo&sorted=food
              ```
              #### Staff-Sorted-API
              ```sh
                  https://hotel-shorted-flask-api.onrender.com/get_reviews?city=Colombo&sorted=staff
              ```
              #### Environment-Sorted-API
              ```sh
                  https://hotel-shorted-flask-api.onrender.com/get_reviews?city=Colombo&sorted=env
              ```
    * For `/get_most_review_food`, you're handling the filtering based on the most reviewed foods using the `food` parameter.
      example:
              #### Most-Review-Food-API
              ```sh
                  https://hotel-shorted-flask-api.onrender.com/get_most_review_food?food=Biryani
              ```
6. Run the app:
   * `if __name__ == '__main__': app.run(debug=True)`: Start the Flask app when you run the script directly.

This `Flask API` provides endpoints to retrieve reviews based on different criteria and filtering options. You can access the API by running the script and visiting the defined routes in your browser or by using tools like `curl`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Flask]: https://flask.palletsprojects.com/en/2.3.x/
[Flask-url]: https://img.shields.io/badge/flask-78c7d1?style=for-the-badge&logo=flask&logoColor=white
