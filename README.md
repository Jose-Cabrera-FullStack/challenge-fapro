API to retrieve UF values
This is a Flask API that retrieves the value of the UF (Unidad de Fomento) for a specific year, using data from the Servicio de Impuestos Internos (SII) website.

Setup
To set up the project, follow these steps:

Clone the repository
Create a virtual environment using your preferred tool (e.g. virtualenv, conda, etc.)
Activate the virtual environment
Install the dependencies with pip install -r requirements.txt
Run the server with python app.py
The server should now be running and accessible at http://localhost:5000.

Endpoints
GET /uf/<year>
Retrieves the value of the UF for the specified year. The year must be a four-digit number between 2014 and the current year.

Response
200 OK with a JSON object containing the UF values for each day of the year.
400 Bad Request if the year is not valid.
404 Not Found if the UF values for the specified year could not be found.
Example
http
Copy code
GET /uf/2022
json
Copy code
{
    "2022-01-01": 29880.9,
    "2022-01-02": 29880.9,
    "2022-01-03": 29880.9,
    ...
    "2022-12-30": 30975.98,
    "2022-12-31": 30975.98
}
Architecture
The codebase follows the Model-View-Controller (MVC) architectural pattern. The breakdown of the components is as follows:

Model: fetch_data_from_api in request_to_csv.py fetches the UF data from the SII website and returns it as a Pandas DataFrame.
View: There is no view layer in this API, as it only provides a RESTful interface.
Controller: app.py defines the routes and endpoints for the API, and is responsible for handling incoming requests and generating appropriate responses.
Design Patterns
The codebase has been designed following the SOLID principles, particularly the Single Responsibility Principle and the Dependency Inversion Principle. This promotes modularity and makes the codebase easier to understand, maintain, and extend.

Testing
Unit tests for the fetch_data_from_api function and the get_uf endpoint are included in the tests directory. To run the tests, run the command pytest in the root directory of the project.

Future Improvements
Some potential improvements for the API include:

Adding caching to reduce the number of requests made to the SII website.
Adding pagination to the response to avoid returning too much data at once.
Adding support for other currencies and financial indicators.