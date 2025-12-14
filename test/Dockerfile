FROM mcr.microsoft.com/playwright:v1.57.0-noble

RUN apt-get update \
 && apt-get install -y curl \
 && rm -rf /var/lib/apt/lists/*
 
# Set working directory
WORKDIR /tests

# Copy package.json and install dependencies
COPY ./package.json package.json
RUN npm install

# Copy your test scripts
COPY ./tests ./tests

# Copy the entrypoint script
COPY ./entrypoint.sh /tests/entrypoint.sh
RUN chmod +x /tests/entrypoint.sh

# Use entrypoint script
ENTRYPOINT ["/tests/entrypoint.sh"]