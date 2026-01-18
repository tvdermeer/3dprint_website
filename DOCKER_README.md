# Docker Deployment Instructions

This guide explains how to build and run the 3D Print Shop application using Docker.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop).

## Configuration

1. **Database Persistence**: The `docker-compose.yml` file is configured to use the `ecommerce.db` SQLite file from your project root. This ensures that your products, orders, and user data are saved on your host machine even if the containers are rebuilt.

2. **Environment Variables**:
   - The backend is configured to look for the database at `sqlite:///./ecommerce.db`.
   - The frontend is built with `VITE_API_BASE_URL=/api/v1` so it knows to route API requests through Nginx.

## Build and Run

1. **Start the application**:
   Run this command in the root directory of the project:
   ```bash
   docker-compose up -d --build
   ```
   - `-d`: Runs the containers in detached mode (in the background).
   - `--build`: Forces a rebuild of the images (useful if you've changed code).

2. **Access the application**:
   Open your browser and go to:
   - **Frontend**: [http://localhost](http://localhost)
   - **API Docs**: [http://localhost/api/docs](http://localhost/api/docs) (Proxied via Nginx)

3. **View Logs**:
   To see the output from the containers:
   ```bash
   docker-compose logs -f
   ```

4. **Stop the application**:
   ```bash
   docker-compose down
   ```

## Development vs Production

- This setup is close to production-ready for a small deployment.
- **Nginx** serves the static frontend files and proxies API requests to the backend.
- **SQLite** is used for simplicity. Ensure you backup the `ecommerce.db` file regularly.

## Troubleshooting

- **Database not found**: Ensure `ecommerce.db` exists in the project root before starting. If it doesn't, the backend will create a new empty one inside the container (which will be synced to your host if the volume mount works).
- **Port conflicts**: If port 80 is already in use on your machine, edit `docker-compose.yml` and change `"80:80"` to `"8080:80"`, then access via `http://localhost:8080`.
