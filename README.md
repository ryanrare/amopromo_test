# Flight Search API

This project provides a REST API to search for flights between airports, using parameters such as origin, destination, and travel dates.

## 🚀 Requirements

Before running the project, make sure you have:

- [Docker](https://www.docker.com/get-started) installed
- [Docker Compose](https://docs.docker.com/compose/) installed
- Internet connection for pulling images

---

## 📦 Running the Project with Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/ryanrare/amopromo_test.git
   cd amopromo_test
1. It is necessary to create a .env file in the root of the project, with the environment variables that are referenced in the settings file.
2. **Build and start the container**

   ```bash
    docker compose up --build
    docker compose exec web python manage.py migrate
    sudo docker compose run --rm -it web python manage_cli.py

This will:

 - Build the Docker image for the API

 - Start the application on http://localhost:8000
 
 - Use a manege_cli.py for create user and generate token to API flingts

3. Verify the container is running

   ```bash
    docker ps
   

4. Export airports manually

   ```bash
   sudo docker compose run web python manage.py export_airports
You should see a container for the API.

## 📡 API Usage

1. Endpoint: Search Flights
   ```bash
    GET /api/flights/

### Query Parameters

| Parameter       | Required | Description                         | Example        |
|-----------------|----------|-------------------------------------|----------------|
| `from`          | Yes      | IATA code of origin airport         | `GRU`          |
| `to`            | Yes      | IATA code of destination airport    | `SDU`          |
| `departure_date`| Yes      | Departure date (YYYY-MM-DD)         | `2025-08-20`   |
| `return_date`   | No       | Return date (YYYY-MM-DD)            | `2025-08-25`   |


2. Example Request:
   ```bash
    curl "http://localhost:8000/api/flights/?from=GRU&to=SDU&departure_date=2025-08-20&return_date=2025-08-25"

3. Example Response:
    ```json
    [
      {
        "flight_number": "AB1234",
        "origin": "GRU",
        "destination": "SDU",
        "price": 250.50,
        "currency": "USD",
        "departure_time": "2025-08-20T08:30:00",
        "arrival_time": "2025-08-20T09:45:00"
      }
    ]
   
## ⚠ Troubleshooting

If you get:

ConnectionRefusedError: [Errno 111] Connection refused
This usually means:

This usually means:

- The API container is not running.  
- The request is being made before the server is ready.

### Fix:

1. **Make sure the container is running:**
    ```bash
    docker ps
    ```

2. **Retry the request after a few seconds.**

3. **If running from another container, use `host.docker.internal` instead of `localhost`:**
    ```bash
    curl "http://host.docker.internal:8000/api/flights/?from=GRU&to=SDU&departure_date=2025-08-20"
    ```
