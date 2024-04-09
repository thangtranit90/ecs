# Use the official Ubuntu base image
FROM ubuntu

# Update the package lists and install Apache HTTP server
RUN apt-get update -y && \
    apt-get install apache2 -y

# Copy the index.html file from the Docker build context to the default Apache document root directory in the container
COPY index.html /var/www/html/

# Specify the command to run when the container starts, which starts the Apache HTTP server in the foreground
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

# Expose port 80 to allow incoming HTTP traffic to the container
EXPOSE 80
