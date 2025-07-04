# Strategic Account Management Platform

This repository contains a minimal prototype of a Strategic Account Management (SAM) tool. The stack uses a Flask backend with a React/TypeScript frontend. PostgreSQL and Redis are included via Docker Compose.

## Running locally

1. Ensure Docker and Docker Compose are installed.
2. From the repository root, run:
   ```bash
   docker compose up --build
   ```
3. The backend will be available at `http://localhost:5000` and the frontend at `http://localhost:3000`.

## Development

The backend code lives under `./backend` and the frontend under `./frontend`.
