# Flask Health App

This is a simple Flask application designed to manage health-related scores and goals. It features a backend with a database to store and retrieve user scores and goals.

## Project Structure

```
flask-health-app
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   └── templates
│       ├── base.html
│       └── index.html
├── migrations
│   └── README.md
├── .env.example
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Features

- **Update Score**: A route to update user scores in the database.
- **Retrieve Goals**: A route to fetch new health goals for users.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd flask-health-app
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.