# 🧭 AI Trip Planner Agent

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-green?logo=langchain)]
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange?logo=streamlit)]
[![OpenAI](https://img.shields.io/badge/OpenAI-API-lightgrey?logo=openai)]
[![License](https://img.shields.io/github/license/harmish/agentic_ai_project)](LICENSE)

---

## 🌟 Introduction

**AI Trip Planner Agent** is an intelligent travel planning assistant powered by advanced LLMs, LangChain, and real-time APIs. It generates personalized, budget-aware, and context-rich travel itineraries for any destination, combining both popular and offbeat experiences.

### Key Highlights

- 🔗 Integrates with real-time APIs (weather, currency, places, etc.)
- 🧠 Powered by LangChain and LLMs for smart reasoning
- 💸 Budget-aware, with live cost breakdowns and currency conversion
- 🗺️ Suggests both tourist hotspots and hidden gems
- 📅 Flexible: supports custom durations, group sizes, and preferences
- 🌐 Multi-modal: works via Streamlit UI and REST API

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A([User Prompt])
    B([AI Trip Planner Agent])
    C([LLM (Groq or OpenAI)])
    I([Response Generator])
    J([User Output])

    subgraph LangChain_Tools
        D1([Weather API])
        D2([Currency API])
        D3([Google Places & Foursquare])
        D4([Tavily Search])
    end

    A --> B
    B --> C
    B --> D1
    B --> D2
    B --> D3
    B --> D4
    B --> I
    I --> J
```

---

## 🚀 Features

- **Personalized Itineraries:** Custom plans for any city, duration, and budget
- **Live Weather & Currency:** Real-time weather and currency conversion
- **Attraction Discovery:** Tourist spots, local gems, restaurants, and activities
- **Cost Breakdown:** Detailed, up-to-date cost estimates
- **Multiple Modes:** Tourist and offbeat plans
- **API Integrations:** Google Places, Foursquare, OpenWeatherMap, ExchangeRate, Tavily, and more
- **Easy to Use:** Streamlit UI and REST API endpoints

---

## 🏁 Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/harmish/agentic_ai_project.git
cd agentic_ai_project/AI_trip_planner
```

### 2. Set Up the Environment

Install [uv](https://github.com/astral-sh/uv):

```sh
pip install uv
```

Create and activate a virtual environment:

```sh
uv venv env --python cpython-3.10.18-windows-x86_64-none
.\env\Scripts\activate
```

### 3. Install Dependencies

```sh
uv pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the root directory with your API keys:

```env
GROQ_API_KEY="your_groq_api_key"
GOOGLE_API_KEY="your_google_api_key"
GPLACES_API_KEY="your_google_places_api_key"
FOURSQUARE_API_KEY="your_foursquare_api_key"
TAVILY_API_KEY="your_tavily_api_key"
OPENWEATHERMAP_API_KEY="your_openweathermap_api_key"
EXCHANGE_RATE_API_KEY="your_exchange_rate_api_key"
```

**Get your API keys:**

- [Groq](https://console.groq.com/)
- [Google Cloud](https://console.cloud.google.com/apis/credentials)
- [Google Places](https://developers.google.com/maps/documentation/places/web-service/get-api-key)
- [Foursquare](https://developer.foursquare.com/)
- [Tavily](https://docs.tavily.com/)
- [OpenWeatherMap](https://home.openweathermap.org/api_keys)
- [ExchangeRate](https://www.exchangerate-api.com/)

### 5. Run the Application

**Streamlit UI:**

```sh
streamlit run streamlit_app.py
```

**FastAPI Backend:**

```sh
uvicorn main:app --reload --port 8000
```

---

## 💡 Example Usage

**Prompt:**  
`Plan me a trip to Mumbai under 80000 rs`

**Agent Output:**

```
🌍 AI Travel Plan
# Generated: 2025-07-12 at 14:44  
# Created by: Harmish's Travel Agent

---

Here’s a comprehensive travel plan for a week-long trip to Mumbai, India, tailored to your budget of ₹80,000. This plan includes both popular tourist attractions and offbeat locations, along with detailed cost breakdowns.

General Information
Destination: Mumbai, India
Duration: 7 Days (August 1 - August 7)
Budget: ₹80,000
Weather: Mumbai has a tropical climate. August is part of the monsoon season, with frequent rains and humid weather. Average temperatures range from 24°C to 30°C.

Day-by-Day Itinerary
Plan A: Generic Tourist Places
Day 1: Arrival & Exploring South Mumbai
  Hotel: ITC Grand Central (₹6,000/night)
  Places to Visit: Gateway of India, Colaba Causeway, Marine Drive
  Restaurants: Breakfast: The Oberoi (₹800/person), Lunch: Bademiya (₹500/person), Dinner: Leopold Cafe (₹700/person)
  Activities: Evening stroll at Marine Drive
...
[Full itinerary and cost breakdown as in your example]
...
This plan is designed to stay within your budget of ₹80,000 while providing a mix of cultural, historical, and recreational experiences in Mumbai. Let me know if you’d like more details!
```

---

## ⚠️ Common Issues

- **API Key Errors:** Ensure all API keys are correct and enabled for the required services.
- **API Quotas:** Some APIs have free tier limits; exceeding them may cause failures.
- **Network Issues:** Check your internet connection if API calls fail.
- **Dependency Conflicts:** Use the recommended Python version and install dependencies in a clean virtual environment.
- **Google API Authorization:** Make sure the required APIs are enabled in your Google Cloud project.

---

## 📚 Documentation & References

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview)
- [Foursquare Places API](https://developer.foursquare.com/docs)
- [Tavily API](https://docs.tavily.com/)
- [ExchangeRate API](https://www.exchangerate-api.com/)

---

## 🔒 Security Notes

- **Never commit your `.env` file or API keys to public repositories.**
- **Regenerate your API keys if you suspect they are compromised.**
- **Restrict API keys to only the services and domains you need.**
- **Review third-party API usage and privacy policies.**

---

Enjoy planning your next adventure with the AI Trip Planner Agent!