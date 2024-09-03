URL Shortener

A simple URL shortener service built with Flask. This service receives a URL and shortens it using a third-party API.
Overview

This project provides a basic implementation of a URL shortener using Flask. Users can submit a URL to the API endpoint, which will then return a shortened version of the URL using an external shortening service.
Features

    Receives a URL via a POST request.
    Shortens the URL using a third-party API.
    Returns the shortened URL.

Installation

To get started with this project, follow these steps:

    Clone the Repository

    bash

git clone https://github.com/yourusername/url-shortener.git

Navigate to the Project Directory

bash

cd url-shortener

Create a Virtual Environment (Optional but recommended)

bash

python -m venv venv

Activate the Virtual Environment

    On Windows:

    bash

venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install the Required Packages

bash

    pip install -r requirements.txt

Configuration

Replace YOUR_API_KEY in the app.py file with your actual API key from the URL shortening service you are using.
Usage

    Start the Flask Application

    bash

python app.py

Send a POST Request to Shorten a URL

Use a tool like curl or Postman to send a POST request to http://localhost:5000/shorten with the following JSON body:

json

{
  "url": "https://www.example.com"
}

Receive the Shortened URL

The response will include the shortened URL:

json

    {
      "shortened_url": "https://short.url/abcd1234"
    }

Example

Here is an example using curl:

bash

curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}'

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For larger changes, please open an issue to discuss them first.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Authors

    Your Name - yourgithubprofile

Acknowledgements

    Thank you to the URL shortening service provider for their API.
