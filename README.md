# 🌍 Climate Change Weather App
---
A Django-based web application that fetches and displays real-time and forecasted weather data for selected cities around the world. 
This app helps visualize climate patterns and trends to promote awareness of global climate change.

## 📌 Features

- 🌦️ Current weather: temperature, pressure, humidity, and wind speed
- 📍 Location input with city and country code
- 🕓 Hourly and monthly forecast
- 📊 Charts and data visualizations (optional)
- 🌐 Built with Django (backend) and HTML/CSS (frontend)
- 🌈 Clean, responsive user interface

## ⚙️ Technologies

- **Backend:** Python, Django, OpenWeatherMap API
- **Frontend:** HTML, CSS
- **Database:** SQLite (default Django DB)
- **Other:** Virtualenv for environment management

## 🚀 Setup Instructions

### 1. Clone the project
--
git clone https://github.com/Janeanny1/climate_change.git
cd climate-change-weather-app

## Create and activate virtual environment
---
python -m venv .venv
.\.venv\Scripts\activate  # On Windows

## Install dependencies
---
pip install -r requirements.txt

## Apply migrations
---
python manage.py migrate

## Run the server
---
python manage.py runserver
Then visit: http://127.0.0.1:8000/

## 📁 Project Structure
---
Climate-change/
│
├── .venv/                      # Python virtual environment (not pushed to Git)
│
├── manage.py                   # Django's CLI entry point
│
├── README.md                   # Project documentation
│
├── climate_app/                # Main Django project configuration
│   ├── __init__.py             # Makes this a Python package
│   ├── settings.py             # Project-wide settings (DB, apps, middleware, templates)
│   ├── urls.py                 # Root URL configuration for routing
│   └── wsgi.py                 # Entry point for WSGI-compatible web servers (e.g., Gunicorn)
│
├── weather/                    # Core Django app for climate/weather logic
│   ├── __init__.py
│   ├── admin.py                # Django admin configuration (optional)
│   ├── apps.py                 # App configuration class
│   ├── models.py               # Data models (currently may be empty or unused)
│   ├── tests.py                # Unit tests for the app
│   ├── views.py                # Core logic to fetch, process, and render weather data
│   ├── urls.py                 # App-specific URL routes (linked from project urls.py)
│   ├── templates/              # HTML templates (Django will look here for views)
│   │   └── weather/
│   │       └── index.html      # Your main HTML UI using Bootstrap + Font Awesome
│   └── static/                 # (Optional) For custom CSS, JS, images
│       └── weather/
│           ├── style.css       # Custom styles (optional)
│           └── icons/          # Any local images/icons (optional)


## 🔑 API Key
---
This project uses the OpenWeatherMap API. 
Be sure to add your API key in weather/views.py or load it securely using environment variables.

## GitHub Repository Link
---
GitHub Repository - climate_change

## 📌 License
---
MIT License. See LICENSE file for details.

## 👤 Author
---
Janet Anne Malikita
GITHUB Link 

💻Happy coding!

