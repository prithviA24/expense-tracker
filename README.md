# Expense Tracker

A full-stack web application to track personal expenses, built with Python and Flask, containerized with Docker, and deployed on GCP with a CI/CD pipeline via GitHub Actions.

---

## Features

- Add expenses with name, amount, category, and date
- View all expenses on the home page sorted by newest first
- See running total of all expenses
- Delete any expense
- SQLite database for persistent storage
- Dockerized for consistent deployment anywhere
- CI/CD pipeline that builds and pushes Docker image to Docker Hub on every push to `main`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite via Flask-SQLAlchemy |
| Frontend | HTML, CSS (Jinja2 templates) |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Infrastructure | GCP VM (Compute Engine) |

---

## Project Structure

```
expense-tracker/
│
├── .github/
│   └── workflows/
│       └── main.yml        # CI/CD pipeline
│
├── static/                 # CSS and static assets
│
├── templates/
│   ├── index.html          # home page — lists all expenses
│   └── add.html            # form to add a new expense
│
├── app.py                  # main Flask application — all routes
├── models.py               # SQLAlchemy Expense model
├── Dockerfile              # container configuration
├── requirements.txt        # Python dependencies
└── .gitignore              # excludes .env, expenses.db, venv
```

---

## Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/prithviA24/expense-tracker.git
cd expense-tracker
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your secret key**

Create a `.env` file in the root folder:
```
SECRET_KEY=your-secret-key-here
```

**5. Run the app**
```bash
python app.py
```

Visit `http://localhost:5000` in your browser. The `expenses.db` SQLite database is created automatically on first run.

---

## Docker Setup

**Build the image**
```bash
docker build -t expense-tracker .
```

**Run the container**
```bash
docker run -p 5000:5000 --env-file .env expense-tracker
```

**Pull from Docker Hub**
```bash
docker pull prithvia24/expense-tracker:latest
docker run -p 5000:5000 --env-file .env prithvia24/expense-tracker:latest
```

---

## Deploying to GCP VM

**SSH into your VM**
```bash
gcloud compute ssh expense-vm --zone=asia-south1-a
```

**Pull latest image and run**
```bash
docker pull prithvia24/expense-tracker:latest
docker run -d -p 80:5000 --env-file .env prithvia24/expense-tracker:latest
```

The `-d` flag runs the container in the background. The `-p 80:5000` flag maps port 80 on the VM (what users hit) to port 5000 inside the container where Flask listens.

---

## CI/CD Pipeline

Every push to `main` automatically:

1. Checks out the code
2. Sets up Python 3.10
3. Installs dependencies
4. Verifies Flask app imports correctly
5. Builds the Docker image
6. Logs in to Docker Hub using GitHub Secrets
7. Tags and pushes the image to Docker Hub as `latest`

**Required GitHub Secrets**

| Secret | Description |
|---|---|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Your Docker Hub password or access token |

---

## How It Works

1. User visits the home page — Flask queries all expenses from SQLite, calculates total, renders `index.html`
2. User clicks Add — Flask renders the add form with today's date pre-filled
3. User submits the form — Flask reads form data, creates an `Expense` object, saves to database via SQLAlchemy, redirects home
4. User clicks Delete — Flask fetches the expense by ID, deletes it from the database, redirects home

---

## Notes

- The SQLite database file `expenses.db` is excluded from version control via `.gitignore`
- The `.env` file is excluded from version control — never commit secrets
- For production with multiple users, replace SQLite with PostgreSQL on Cloud SQL by updating the `SQLALCHEMY_DATABASE_URI` in `app.py`
