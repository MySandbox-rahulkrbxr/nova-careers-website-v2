# Nova Careers Website v2

A modern web application for managing and displaying job listings, built with Python, Flask, and SQLAlchemy.

## Features
- Browse available job listings
- View detailed job descriptions
- Submit job applications via web form
- Store and retrieve job data from a database

## Project Structure
```
app.py                  # Main Flask application
 database.py            # Database connection and queries
 requirements.txt       # Python dependencies
 pyproject.toml         # Poetry configuration (if used)
 static/                # Static assets (images, CSS, etc.)
 templates/             # HTML templates
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd nova-careers-website-v2
```

### 2. Install Dependencies
Using pip:
```bash
pip install -r requirements.txt
```
Or with Poetry:
```bash
poetry install
```

### 3. Configure Environment Variables
Set the following environment variable:
- `DB_CONNECTION_STRING`: Your database connection string (e.g., for PostgreSQL, MySQL, etc.)

Example (Unix/macOS):
```bash
export DB_CONNECTION_STRING='your-database-connection-string'
```

### 4. Run the Application
```bash
python app.py
```

The app will be available at `http://localhost:5000` by default.

## License
See [LICENSE](LICENSE) for details.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Contact
For questions or support, please contact the project maintainer.

