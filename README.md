# AI Trip Planner

## What is AI Trip Planner?

AI Trip Planner is an intelligent assistant that helps you plan your trips by leveraging AI-powered tools and APIs. It can suggest places to visit, check weather conditions, convert currencies, and perform useful calculations to make your travel planning easier and smarter.

### How does it work?

The project uses a modular agentic workflow:
- **Agentic Workflow:** The core agent coordinates between different tools and modules to answer your travel-related queries.
- **Tools:** Includes modules for weather info, place search, currency conversion, and calculations.
- **Prompts:** Uses prompt templates to interact with AI models for generating suggestions and answers.
- **Configurable:** Easily set up with your own API keys and preferences.

---

## Getting Started

Follow these steps to set up and use the AI Trip Planner, even if you are a complete beginner.

### 1. Prerequisites

- Python 3.10 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)

### 2. Clone the Repository

Open a terminal and run:

```powershell
git clone <repository-url>
cd AI_trip_planner
```

### 3. Create and Activate a Virtual Environment

**On Windows:**
```powershell
python -m venv tripvenv
tripvenv\Scripts\activate
```

**On macOS/Linux:**
```sh
python3 -m venv tripvenv
source tripvenv/bin/activate
```

### 4. Install Required Packages

```powershell
pip install -r requirements.txt
```

### 5. Configure API Keys

Some features require API keys (e.g., for weather or place search). Create a `.env` file in the project root and add your keys:

```
GROQ_API_KEY=your-key-here
GOOGLE_API_KEY=your-key-here
# Add other keys as needed
```

### 6. Run the Application

To start the main program, run:

```powershell
python main.py
```

or

```powershell
python app.py
```

### 7. Using the Jupyter Notebook (Optional)

For experiments and interactive exploration, you can use the provided notebook:

```powershell
pip install notebook
jupyter notebook
```
Then open `notebook/experiments.ipynb` in your browser.

---

## Project Structure

- `main.py`, `app.py` — Main entry points
- `agent/` — Agentic workflow logic
- `tools/` — Tools for weather, currency, place search, etc.
- `utils/` — Helper utilities
- `config/` — Configuration files
- `prompt_liberary/` — Prompt templates
- `notebook/` — Jupyter notebooks

---

## Need Help?

If you get stuck, check the code comments or open an issue. Pull requests and suggestions are welcome!
