from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from airports.models import Airport
from .services import get_flights_from_mock_airline
from .utils import calculate_meta, calculate_price
from datetime import datetime


class FlightSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        origin = request.GET.get("from")
        destination = request.GET.get("to")
        departure_date = request.GET.get("departure_date")
        return_date = request.GET.get("return_date")

        if origin == destination:
            return Response({"error": "Aeroporto de origem e destino não podem ser iguais."}, status=400)

        try:
            origin_airport = Airport.objects.get(code=origin)
            destination_airport = Airport.objects.get(code=destination)
        except Airport.DoesNotExist:
            return Response({"error": "Um dos aeroportos não está cadastrado."}, status=400)

        today = datetime.now().date()
        try:
            dep_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
            ret_date = datetime.strptime(return_date, "%Y-%m-%d").date()
        except:
            return Response({"error": "Formato de data inválido. Use YYYY-MM-DD."}, status=400)

        if dep_date < today:
            return Response({"error": "Data de ida não pode ser anterior a hoje."}, status=400)

        if ret_date < dep_date:
            return Response({"error": "Data de volta não pode ser anterior à data de ida."}, status=400)

        outbound_flights = get_flights_from_mock_airline(origin, destination, departure_date)
        return_flights = get_flights_from_mock_airline(destination, origin, return_date)

        enriched_outbound = []
        for flight in outbound_flights["options"]:
            fare = flight["price"]["fare"]
            flight["price"] = calculate_price(fare)
            flight["meta"] = calculate_meta(flight, origin_airport, destination_airport)
            enriched_outbound.append(flight)

        enriched_return = []
        for flight in return_flights["options"]:
            fare = flight["price"]["fare"]
            flight["price"] = calculate_price(fare)
            flight["meta"] = calculate_meta(flight, destination_airport, origin_airport)
            enriched_return.append(flight)

        combinations = []
        for ida in enriched_outbound:
            for volta in enriched_return:
                combo_total = ida["price"]["total"] + volta["price"]["total"]
                combinations.append({
                    "outbound": ida,
                    "return": volta,
                    "price": {
                        "total": round(combo_total, 2)
                    }
                })

        combinations.sort(key=lambda x: x["price"]["total"])

        return Response({
            "origin": origin,
            "destination": destination,
            "departure_date": departure_date,
            "return_date": return_date,
            "combinations": combinations
        })
