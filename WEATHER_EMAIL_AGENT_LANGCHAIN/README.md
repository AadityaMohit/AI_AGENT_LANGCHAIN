# Weather & Email Combined Agent

An AI agent that combines weather information retrieval with email sending capabilities. It can fetch weather data for any city and send that information via email.

## Features

- Get real-time weather information for any city using OpenWeather API
- Send emails with weather data automatically
- Natural language queries - just ask for weather and email in one request
- Powered by Google's Gemini model via LangChain

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r ../requirement.txt
   ```

2. **Get API Keys:**
   - **Google API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **OpenWeather API Key**: Get free API key from [OpenWeatherMap](https://openweathermap.org/api)

3. **Email Configuration:**
   - For Gmail: Enable 2-Factor Authentication and generate an App Password
   - See `../email_agent/SETUP_GUIDE.md` for detailed email setup instructions

4. **Create/Update `.env` file** in the root directory:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password_here
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

## Usage

Run the agent:
```bash
python app.py
```

### Example Queries

The agent understands natural language requests to:
- Get weather and send it via email in one command
- Combine weather lookup with email sending

**Examples:**
- "Get the weather in Bangalore and send it to aadityamohit0308@gmail.com"
- "What's the weather in New York? Send it to user@example.com with subject 'NYC Weather'"
- "Get weather for Tokyo and email it to me at myemail@gmail.com"
- "Check the weather in London and send it to john@example.com"

The agent will:
1. First fetch the weather information for the specified city
2. Then compose and send an email with that weather data

## How It Works

This agent combines two tools:
1. **get_weather**: Fetches current weather from OpenWeather API
2. **send_email**: Sends emails via SMTP

The AI agent intelligently:
- Parses your request to extract the city name and recipient email
- Calls the weather tool to get the data
- Formats the weather information
- Calls the email tool to send it to the recipient

## Project Structure

```
LangChain/
├── weather_email_agent/    # Combined agent (this folder)
│   ├── app.py
│   └── README.md
├── weather_agent/          # Weather-only agent
├── email_agent/            # Email-only agent
└── .env                    # Shared environment variables
```


