# Stage 1: Build stage
FROM python:3.9-slim as build-stage

WORKDIR /app

RUN pip3 install Jinja2==3.0.3
COPY . .

# Stage 2: Final stage
FROM python:3.9-alpine as final-stage

WORKDIR /app

COPY --from=build-stage /app/* /app/

RUN pip3 install pymongo
RUN pip3 install Flask
RUN pip3 install Jinja2==3.0.3

RUN mkdir templates
RUN mv client.html templates
RUN mv supplier.html  templates
RUN mv welcome.html  templates
RUN mv courier.html  templates

EXPOSE 5000

CMD ["python", "app.py"]
