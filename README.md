

# Heart Disease Prediction

A Python project that predicts heart disease from patient data using a machine learning model. Provides both:

- **CLI tool**: Enter patient info or load CSV for batch prediction.
- **FastAPI backend**: Serves predictions via API.
- **Dockerized**: Run API, CLI, and frontend anywhere.

## Features
- Single patient prediction
- Batch prediction from CSV (`loaddetect`)
- Interactive CLI with rich outputs
- Web frontend (optional)
- Docker-ready

## Installation
Clone the repo and build Docker images:

```bash
git clone https://github.com/aalzrg/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
docker compose up -d --build
````

## Usage

* **CLI**:

```bash
docker compose run --rm cli
```

* **API**: Visit `http://localhost:8000/docs`
* **Frontend**: Visit `http://localhost:8080`

## CSV Batch Prediction

1. Place your CSV file(s) in a folder on your computer.
   Example: `C:\Users\BBY\Desktop\sooka\patients.csv`

2. Make sure the folder is mounted in your CLI container in `docker-compose.yml`:

```yaml
volumes:
  - /c/Users/BBY/Desktop/sooka:/data
```

3. Run the CLI and use the `loaddetect` command:

```text
loaddetect /data/patients.csv
```

The CLI will read all patients from the CSV and send requests to the API for predictions.

## Requirements

* Python 3.13
* FastAPI, Uvicorn, Requests, Pandas, Numpy, Joblib, Rich

## Notes

* No need to rebuild the CLI container if you only change CSV files.
* The `/data` mount allows the CLI to access any CSV files on your host machine.
* Make sure the CSV has correct column names expected by the CLI (`age`, `sex`, `cp`, etc.).

---
