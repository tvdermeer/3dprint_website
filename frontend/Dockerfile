# Build stage
FROM node:20-slim AS build-stage

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build the app with the API base URL set to use the relative path (handled by Nginx proxy)
ENV VITE_API_BASE_URL=/api/v1
RUN npm run build

# Production stage
FROM nginx:alpine AS production-stage

# Copy the built artifacts from the build stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
