# 🚌 Public Transit Tracker

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A web application for tracking London public transit with real time bus arrivals, weather information, and route planning.

## Features

- 🚌 Real time bus arrivals (TfL API)
- 🌤️ Weather information
- 🗺️ Interactive route planning
- 📍 Location services
- 🚨 Traffic updates
- 👤 User authentication

## Quick Start

1. **Clone and setup**
   ```bash
   git clone https://github.com/mahmoudmoe53/Public_Transit_Tracker.git
   cd Public_Transit_Tracker
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your API keys and database settings.

3. **Initialize database**
   ```bash
   python -c "from lib.init_db import initialize_db; initialize_db()"
   ```

4. **Run application**
   ```bash
   flask run
   ```

## Configuration

Create `.env` file:

```env
# Database
DB_HOST=localhost
DB_NAME=transit_tracker
DB_USERNAME=your_db_user
DB_PASSWORD=your_db_password

# API Keys
GOOGLE_API_KEY=your_google_maps_api_key
WEATHER_API_KEY=your_openweather_api_key
TOMTOM_API_KEY=your_tomtom_api_key
FLASK_SECRET_KEY=your_secret_key
```

## API Keys Required

- **Google Maps API**: [Get here](https://console.cloud.google.com/) - Route planning
- **OpenWeatherMap**: [Get here](https://openweathermap.org/api) - Weather data
- **TomTom API**: [Get here](https://developer.tomtom.com/) - Traffic updates
- **TfL API**: [Get here](https://api.tfl.gov.uk/) - Bus arrivals (free)

## Development Notes

⚠️ **Important**: This application uses placeholder coordinates (`51.445, -0.4103`) for development purposes since it was built for localhost testing. In production, implement proper user location detection.

## Project Structure

```
Public_Transit_Tracker/
├── lib/                # Core modules
├── templates/          # HTML templates
├── app.py             # Main Flask app
└── requirements.txt   # Dependencies
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/name`)
5. Open Pull Request


## Known Issues

- Uses placeholder coordinates for localhost development
- API rate limits apply (check individual service limits)
- Requires active internet connection for all features

---

**⭐ Star this repo if you find it useful!**
