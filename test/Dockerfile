FROM mcr.microsoft.com/playwright:v1.57.0-noble
WORKDIR /tests
COPY ./package.json package.json
RUN npm install
COPY ./tests ./tests
CMD ["npx", "playwright", "test"]