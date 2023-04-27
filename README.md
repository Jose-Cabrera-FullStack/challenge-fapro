UF Value API
This project provides a simple Flask-based API for retrieving the Unidad de Fomento (UF) value for a given year. The UF is an index used in Chile to adjust prices for inflation.

Installation
This project requires Python 3.7 or higher. Clone this repository and navigate to the project directory. Then, install the required dependencies by running the following command:

Copy code
pip install -r requirements.txt
Usage
To start the server, run the following command:

Copy code
python app.py
This will start the server on http://127.0.0.1:5000/.

To retrieve the UF value for a given year, make a GET request to the following URL:

arduino
Copy code
http://127.0.0.1:5000/uf/<year>
where <year> is the year for which you want to retrieve the UF value. For example, to retrieve the UF value for 2015, you would make a GET request to the following URL:

arduino
Copy code
http://127.0.0.1:5000/uf/2015
The server will return a JSON response with the UF value for the given year. If the UF value for the given year is not available, the server will return an error response.

Testing
This project includes unit tests that can be run using the following command:

Copy code
pytest
Design Principles
This project follows the SOLID design principles to improve code quality, readability, and maintainability. The project separates concerns by following the Model-View-Controller (MVC) architecture pattern, where fetch_data_from_api() acts as the model, app.py acts as the controller, and the routes and responses act as the view. The project also uses dependency injection and mocking to improve testability and maintainability.