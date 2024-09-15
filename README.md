Fruit.ai 
Backend
This repository contains the backend for Fruit.ai, a Flask application that supports CRUD operations for managing FAQs related to fruit health.

Project Structure
The backend is located at:

Copy code
fruit.ai\fruit.ai\backend
Setup Instructions
To set up and run the backend locally, follow these steps:

Create the backend folder and navigate to it:


mkdir backend
cd backend
Create and activate a virtual environment:


python -m venv venv
venv\Scripts\activate
Install necessary dependencies:


pip install Flask Flask-Cors
Running the Application
To start the Flask application, simply run:


flask run
The backend will run on http://localhost:5000 by default.

API Endpoints
The backend provides the following REST API endpoints to manage the FAQ section:

GET /faqs: Fetch all FAQs.
GET /faqs/
: Fetch a single FAQ by its ID.
POST /faqs: Create a new FAQ.
PUT /faqs/
: Update an existing FAQ by its ID.
DELETE /faqs/
: Delete a FAQ by its ID.
These endpoints are consumed by the frontend to enable users to interact with the FAQ page.

Virtual Environment
This project uses a Python virtual environment to manage dependencies. Ensure that you activate the virtual environment before running any commands:


venv\Scripts\activate
CORS Support
The project uses Flask-CORS to handle cross-origin requests from the frontend.

Contributing
We welcome contributions! Feel free to fork the repository and submit pull requests.
