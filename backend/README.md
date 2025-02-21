# CyberGraphGuard Backend

## Overview
CyberGraphGuard is a cybersecurity threat detection system backend built with **FastAPI**. It processes security logs, detects threats using graph-based analysis, and provides API endpoints for interacting with the system.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: ArangoDB (Graph Database)
- **Machine Learning**: NVIDIA cuGraph, GraphRAG
- **Authentication**: JWT (JSON Web Tokens)
- **Networking & Alerts**: SMTP for email notifications


## Installation
### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn
- ArangoDB

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourrepo/cybergraphguard-backend.git
   cd cybergraphguard-backend
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```sh
   uvicorn app.main:app --reload
   ```
5. Alternatively, you can run the server using the provided script:
   ```sh
   chmod +x run.sh
   ./run.sh
   ```
6. Access the API documentation:
    - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Structure
```
backend/
├── app/
│   ├── routes/          # API Endpoints
│   │   ├── logs.py      # Manage security logs
│   │   ├── analysis.py  # Threat detection API
│   │   ├── auth.py      # JWT authentication
│   ├── models/         # Pydantic Models
│   │   ├── log_entry.py
│   │   ├── user.py      # User model for authentication
│   ├── services/       # Business Logic & AI Analysis
│   │   ├── threat_detection.py  # Threat detection logic
│   │   ├── graph_analysis.py    # Graph-based threat analysis
│   │   ├── ml_model.py          # Machine Learning for threat detection
│   │   ├── notification.py      # Send alerts & notifications
│   ├── database/        # Database Connection & Models
│   │   ├── db.py
│   │   ├── user_db.py   # User management
│   ├── main.py         # Application entry point
├── .env                # Environment variables
├── requirements.txt    # Required Python packages
├── run.sh              # Script to run the server
├── README.md           # Project documentation
```

## Dependencies
The project requires the following Python libraries:
```
fastapi
uvicorn
python-arango
python-dotenv
networkx
joblib
numpy
jose
passlib
smtplib
```

## API Endpoints
### Logs Management
- **POST /logs** → Add security log
- **GET /logs** → Retrieve all logs

### Threat Detection
- **POST /threats** → Add a detected threat
- **GET /threats** → Retrieve detected threats

### Graph Analysis
- **GET /graph/{ip}** → Retrieve IP relations graph

### Reports
- **GET /report** → Generate cybersecurity threat report

### Authentication
- **POST /auth/register** → Register a new user
- **POST /auth/login** → User login & get JWT token

## Database Schema (ArangoDB Graph Model)
### Nodes:
- **IP Addresses**
- **Users**
- **Events**
- **Threats**

### Edges:
- **REQUESTED** (User → IP)
- **CONNECTED_TO** (IP → IP)
- **PART_OF_ATTACK** (Event → Threat)

## Environment Variables (.env)
```
DATABASE_URL=your_arangodb_url
JWT_SECRET=your_secret_key
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_email@example.com
SMTP_PASS=your_email_password
```

## Contribution
1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

## License
This project is licensed under the MIT License.

---
**Next Steps:** Implement ArangoDB integration and refine graph-based threat analysis.
