# 🗳️ Simple Voting App with FastAPI, Redis, and Docker Compose

This is a basic voting app built with FastAPI for the backend API, Redis for pub/sub messaging and counting, and Docker Compose for easy service orchestration.

Main objective it to build a simple app to understand the redis service. Also each component runs in a separate docker container so that we can test out docker compose

## 🧩 Features

- Submit votes via HTTP POST
- Real-time vote counting using Redis Pub/Sub
- View aggregated vote results through an API
- Dashboard UI (optional)
- All services containerized via Docker Compose

## 📁 Project Structure

```
.
├── api/
│   ├── main.py
│   └── Dockerfile
│   └── requirements.txt
├── counter/
│   └── counter.py
│   └── Dockerfile
│   └── requirements.txt
├── dashboard/
│   └── index.html
│   └── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Docker Desktop
- WSL 2 (if on Windows)
- curl or Postman (optional)

### 🔧 Run the App

```bash
docker-compose up --build
```

### 📮 API Endpoints

**POST** `/vote`
```json
{
  "option": "Cats"
}
```

**GET** `/results`
```json
{
  "Cats": "3",
  "Dogs": "2"
}
```

### 📊 Dashboard

Visit `http://localhost:8080`

## 🧼 Clean Up

```bash
docker-compose down
```
