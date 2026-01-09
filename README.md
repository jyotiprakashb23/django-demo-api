Django Demo Project
A Django web application with PostgreSQL database, fully containerized using Docker.
Prerequisites
Before you begin, ensure you have the following installed on your system:

Docker (version 20.10 or higher)
Docker Compose (version 1.29 or higher)

Project Structure
django-demo/
├── backend/              # Django application code
├── .venv/               # Python virtual environment
├── docker-compose.yml   # Docker Compose configuration
├── Dockerfile           # Docker image configuration
├── .dockerignore        # Docker ignore file
├── .env                 # Environment variables (not tracked in git)
└── README.md            # This file

Getting Started

1. Clone the Repository
   
git clone https://github.com/YOUR_USERNAME/django-demo.git
cd django-demo

2. Set Up Environment Variables
   
Create a .env file in the root directory with the following variables:
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_pass
DATABASE_URL=postgresql://django_user:django_pass@db:5432/django_db

3. Build and Start the Application
docker-compose up --build

4. Access the Application
http://localhost:8000




