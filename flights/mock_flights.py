# mock_flights.py

def get_mock_flights(origin, destination, date):
    return {
        "summary": {
            "departure_date": date,
            "from": {
                "iata": origin,
                "city": "Cidade Origem",
                "lat": -23.4356,
                "lon": -46.4731
            },
            "to": {
                "iata": destination,
                "city": "Cidade Destino",
                "lat": -22.9104,
                "lon": -43.1631
            },
            "currency": "BRL"
        },
        "options": [
            {
                "departure_time": f"{date}T06:30:00",
                "arrival_time": f"{date}T08:15:00",
                "price": {
                    "fare": 450.00
                },
                "aircraft": {
                    "model": "A320",
                    "manufacturer": "Airbus"
                }
            },
            {
                "departure_time": f"{date}T09:00:00",
                "arrival_time": f"{date}T10:50:00",
                "price": {
                    "fare": 380.50
                },
                "aircraft": {
                    "model": "737-800",
                    "manufacturer": "Boeing"
                }
            },
            {
                "departure_time": f"{date}T14:10:00",
                "arrival_time": f"{date}T16:05:00",
                "price": {
                    "fare": 520.75
                },
                "aircraft": {
                    "model": "A321neo",
                    "manufacturer": "Airbus"
                }
            },
            {
                "departure_time": f"{date}T18:45:00",
                "arrival_time": f"{date}T20:40:00",
                "price": {
                    "fare": 610.20
                },
                "aircraft": {
                    "model": "737 MAX",
                    "manufacturer": "Boeing"
                }
            },
            {
                "departure_time": f"{date}T22:30:00",
                "arrival_time": f"{date}T00:15:00",
                "price": {
                    "fare": 299.99
                },
                "aircraft": {
                    "model": "E195-E2",
                    "manufacturer": "Embraer"
                }
            }
        ]
    }
