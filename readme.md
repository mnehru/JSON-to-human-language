# Workout AI Service

A FastAPI-based service that generates natural language summaries of weekly workout data using TinyLlama AI model.

## Features

- **Motivational Summaries**: For users, generates encouraging and energetic workout summaries.
- **Factual Reports**: For coaches, provides technical and analytical workout progress reports.
- **Customizable Temperature**: Different randomness levels for varied outputs based on audience.

## API Endpoint

### POST /generate-summary

Generates a workout summary based on audience and workout data.

**Request Body:**
```json
{
  "audience": "USER" | "COACH",
  "workout": {
    "Monday": {"exercise": "Push-ups", "reps": 20},
    "Tuesday": {"exercise": "Running", "distance_km": 5.0},
    ...
  }
}
```

**Response:**
```json
{
  "summary": "Your workout summary in natural language."
}
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mnehru/JSON-to-human-language.git
   cd workout-ai-service
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Usage

- Access the API at `http://localhost:8000/generate-summary`
- For interactive docs, visit `http://localhost:8000/docs`

## Deployment

This is a FastAPI application. For production deployment, consider using services like Heroku, Railway, or Vercel.

## License

MIT License 
