# 🌦️ Weather Backend (Django + Open‑Meteo)

This is the **Django backend service** for the Weather React App.  
It acts as a middleware layer between the React frontend and the **Open‑Meteo API**, handling requests, fetching weather data, and returning clean JSON responses.

---

## 🔗 Live Deployment

- **Backend (Render):** [Weather Backend](https://weather-backend-ugpk.onrender.com/)  
- **Frontend (React on Vercel):** [Weather Frontend](https://weather-frontend-sigma-ten.vercel.app/)

---

## ✨ Features

- **City Search Endpoint**: Query weather data by city name.
- **Open‑Meteo Integration**: Fetches real‑time weather conditions (temperature, humidity, wind speed).
- **Clean JSON Response**: Simplified output for easy consumption by frontend.
- **Middleware Role**: Decouples frontend from external API, adds flexibility for future extensions.

---

## 🛠️ Tech Stack

| Category       | Technology   | Description                                      |
| -------------- | ------------ | ------------------------------------------------ |
| **Backend**    | **Django**   | Python web framework for building APIs.          |
| **API**        | **Open‑Meteo** | Free weather API providing forecast data.        |
| **Deployment** | **Render**   | Cloud platform hosting the Django backend.       |

---

## ⚙️ Local Setup

### Prerequisites

- Python 3.10+
- pip / virtualenv

---

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dhanyasri612/weather-backend.git
   cd weather-backend
   
2. Create virtual environment & activate:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
  

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   
4. Run migrations:

   ```bash
   python manage.py migrate

5. Start development server:

   ```bash
   python manage.py runserver
   
6.API will be available at: 

http://127.0.0.1:8000/weather/?city=London
