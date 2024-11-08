# Start with Ubuntu as the base image
FROM ubuntu:latest

# Install Nginx web server and remove the package manager's cache in order to reduce image size
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy the custom Nginx config file into the Docker container
COPY nginx.conf /etc/nginx/nginx.conf

# instructing the Docker to listen on ports 8080 and 8081 which avoid conflict with other busy ports such as 80 for HTTP or 443 for HTTPS
EXPOSE 8080 8081

# Start Nginx in the foreground (so it keeps running)
CMD ["nginx", "-g", "daemon off;"]
