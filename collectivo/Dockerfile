# Use collectivo as parent image
FROM milawien/collectivo:v0.6.3

# Change to root user to install extensions
USER root

# Copy requirements into the container
COPY ./requirements.txt /tmp/requirements.txt

# Install requirements and remove temporary files
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

# Copy extensions into the root of the collectivo app
COPY ./extensions /collectivo_app

# Run the app without root access
USER django-user
