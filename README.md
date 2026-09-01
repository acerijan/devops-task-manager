# DevOps Task Manager API - Internship Project (KTM Bees Pvt. Ltd.)

A simple Flask-based Task Manager API built as the central practical project for a DevOps internship at **KTM Bees Pvt. Ltd.**, used to demonstrate an end-to-end DevOps workflow: version control, containerization, orchestration, CI/CD automation, and cloud deployment.

## Project Overview

Instead of building isolated exercises for each tool, this project uses **one application** as a thread running through the entire DevOps pipeline:

```
Python (Flask) App
    ↓
Git / GitHub (version control)
    ↓
Linux / Networking / Bash (foundations & automation)
    ↓
Docker (containerization)
    ↓
Kubernetes + Helm (orchestration, local via OrbStack)
    ↓
GitHub Actions (CI/CD)
    ↓
AWS EC2 (cloud deployment)
```

## Tech Stack

- **Language/Framework:** Python 3.11, Flask
- **Testing:** pytest
- **Version Control:** Git, GitHub
- **Containerization:** Docker (OrbStack runtime on macOS)
- **Orchestration:** Kubernetes, Helm (local cluster via OrbStack)
- **Artifact Registry:** Docker Hub
- **CI/CD:** GitHub Actions
- **Cloud:** AWS EC2 (Ubuntu 22.04 LTS)
- **Config Management:** python-dotenv, environment variables

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check / status message |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a new task (`{"name": "..."}`) |
| DELETE | `/tasks/<id>` | Delete a task by ID |
| GET | `/grade/<score>` | Returns a letter grade for a numeric score |
| GET | `/stats` | Returns total and completed task counts |

## Project Structure

```
devops-task-manager/
├── app.py                     # Main Flask application
├── test_app.py                 # pytest test suite
├── requirements.txt
├── run.sh                      # Bash automation script (startup + health check)
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env                        # Local environment variables (not committed)
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI pipeline
├── k8s/
│   └── deployment.yaml          # Kubernetes Deployment + Service manifests
├── task-manager-chart/          # Helm chart for the app
└── multi-lang/                  # Basic programming concept demos across languages
    ├── java/
    │   ├── Grade.java
    │   └── Dockerfile
    ├── php/
    │   ├── grade.php
    │   └── Dockerfile
    ├── go/
    │   ├── grade.go
    │   └── Dockerfile
    └── sql/
        └── tasks.sql
```

## Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

App runs at `http://localhost:5000`.

```bash
curl http://localhost:5000/
curl -X POST -H "Content-Type: application/json" -d '{"name":"Learn Docker"}' http://localhost:5000/tasks
curl http://localhost:5000/tasks
```

### Using the startup script
```bash
chmod +x run.sh
./run.sh
```

## Environment Variables

Config is managed via a `.env` file (not committed to Git) and read with `python-dotenv`:

```
FLASK_ENV=development
PORT=5000
SECRET_KEY=your-secret-key
```

In Docker, variables are passed at runtime instead of baked into the image:
```bash
docker run -d -p 5000:5000 -e SECRET_KEY=your-key -e PORT=5000 task-manager-app
```

In GitHub Actions, secrets are stored in the repo's encrypted **Settings → Secrets** and referenced via `${{ secrets.SECRET_KEY }}`.

## Running with Docker

```bash
docker build -t task-manager-app .
docker run -d -p 5000:5000 --name task-manager task-manager-app
docker ps
curl http://localhost:5000/
```

## Running on Kubernetes (local, via OrbStack)

```bash
kubectl apply -f k8s/deployment.yaml
kubectl get pods
kubectl get svc task-manager-service
curl http://localhost:5000/
```

### Using Helm
```bash
helm install task-manager-release ./task-manager-chart
helm list
```

> Note: Kubernetes was demonstrated on a local single-node cluster (OrbStack). Multi-node production cluster deployment on dedicated cloud infrastructure was studied conceptually and is planned as a follow-up after the internship's external defense.

## CI/CD (GitHub Actions)

Every push to `main` automatically triggers `.github/workflows/ci.yml`, which:
1. Checks out the code
2. Sets up Python 3.11
3. Installs dependencies
4. Runs the `pytest` test suite

Results are visible under the repo's **Actions** tab.

## Deploying to AWS EC2

1. Launch an Ubuntu 22.04 LTS EC2 instance (`t2.micro`/`t3.micro`, free-tier eligible)
2. Open inbound ports 22 (SSH, My IP) and 5000 (Custom TCP, Anywhere) in the security group
3. SSH into the instance and install Docker + Git
4. Clone this repository and build/run the container:

```bash
git clone https://github.com/<your-username>/devops-task-manager.git
cd devops-task-manager
sudo docker build -t task-manager-app .
sudo docker run -d -p 5000:5000 --name task-manager task-manager-app
```

5. Verify externally: `curl http://<EC2-Public-IP>:5000/`
6. Terminate the instance once evidence is captured, to avoid unnecessary cloud costs.

## Multi-Language Concept Demos

The `multi-lang/` folder contains minimal programs (Java, PHP, Go, SQL) implementing the same grading logic, each demonstrating that core programming concepts (variables, conditionals, loops) transfer across languages. Java, PHP, and Go each include their own Dockerfile for containerized execution.

## Testing

```bash
pytest test_app.py -v
```

## Author

**Rijan** — BCA Student, Tribhuvan University
DevOps Intern, KTM Bees Pvt. Ltd.
Mentor: Prabin Shrestha