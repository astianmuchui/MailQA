# MailWise
![diagram-export-9_1_2023, 8_25_55 AM](https://github.com/KevKibe/Hackathon-Application/assets/86055894/60d79103-3602-45e0-ba5b-56d0fdcb5332)
## User Journey
- The user logs in to the app using their Google account.
- The app requests authorization from Google to access the user's Gmail emails.
- The user grants permission to the app.
- The app receives an access token from Google.(this happens on the backend)
- The app redirects the user to the chatbot page.
- The user types a query into the chatbot.
- The chatbot processes the query and sends it to our API.
- The API returns a response to the chatbot.
- The chatbot displays the response to the user.

## Instructions to activate API
```cd API``` in the terminal
run ```python -m venv venv``` in terminal
run ```venv/Scripts/activate``` in the terminal
run ```pip install -r requirements.txt``` in the terminal
run```uvicorn api:app --host 127.0.0.1 --port 8000 --reload``` in the terminal
