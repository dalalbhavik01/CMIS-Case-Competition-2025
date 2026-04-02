# CMIS Case Competition 2025 Platform

This repository contains the application powering the **CMIS Case Competition 2025**. It features a complete event management system with a FastAPI backend, a modern Next.js admin/student dashboard, and robust database support via PostgreSQL. 

## 🚀 Tech Stack

### Frontend
- **Framework:** Next.js 14 (App Router)
- **UI & Styling:** React 18, Tailwind CSS
- **Additional Libraries:** `@dnd-kit` (drag and drop), `react-datepicker`

### Backend
- **Framework:** FastAPI
- **Database ORM:** SQLAlchemy (with PostgreSQL)
- **Authentication:** JWT, python-jose, passlib (bcrypt)
- **AI Integration:** Google Generative AI (Gemini)
- **Additional Integrations:** FastAPI-Mail, APScheduler, PyPDF/FPDF2

### Infrastructure
- **Containerization:** Docker & Docker Compose
- **Database Engine:** PostgreSQL 16

## 📂 Project Structure

```
├── backend/              # FastAPI application
│   ├── routers/          # API endpoints
│   ├── scripts/          # Backend-specific utility/testing scripts
│   ├── main.py           # Application entry point
│   └── models.py         # SQLAlchemy DB models
├── frontend/             # Next.js web application
│   ├── src/app/          # Page router and React components
│   └── public/           # Static assets
├── docs/                 # Competition documentation and case studies
├── scripts/              # Project-level automation and seeding scripts
├── docker-compose.yml    # Docker container configuration
└── .env.example          # Environment variable template
```

## 🛠️ Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js (v20+) if running the frontend bare-metal
- Python 3.10+ if running the backend bare-metal

### Running Locally Configuration (Docker)

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd CMIS
   ```
2. Configure environment variables:
   Copy the example environment into a `.env` file for both backend and root:
   ```bash
   cp .env.example .env
   cp frontend/.env.local.example frontend/.env.local # if applicable
   ```
   *Make sure to fill in your `GEMINI_API_KEY`, Mail Settings, and `DATABASE_URL`.*

3. Spin up the containers:
   ```bash
   docker-compose up --build
   ```

### Accessing the application
- **Frontend Dashboard:** `http://localhost:3000`
- **Backend API & Swagger Docs:** `http://localhost:8000/docs`
- **Database:** Exposed on `localhost:5432`

## 🧰 Scripts & Tooling
Any automation, database seeding, test user creation, or historical logs can be found in the `scripts/` directory.

## 📄 License
This codebase was created for the CMIS Case Competition 2025 framework. All rights reserved.
