import requests
from django.core.management.base import BaseCommand
from airports.models import Airport
from amopromo_test.settings import API_URL_EXTRACT, MOCK_AUTH_USER, MOCK_AUTH_USER_SENHA


class Command(BaseCommand):
    help = "Importa e atualiza os aeroportos domésticos via API"

    def handle(self, *args, **kwargs):
        self.stdout.write("Conectando à API de aeroportos...")

        try:
            response = requests.get(API_URL_EXTRACT, auth=(MOCK_AUTH_USER, MOCK_AUTH_USER_SENHA))
            response.raise_for_status()

        except requests.RequestException as e:
            self.stderr.write(f"Erro ao conectar na API: {e}")
            return

        data = response.json()

        created, updated = 0, 0

        for iata_code, info in data.items():
            obj, is_created = Airport.objects.update_or_create(
                code=iata_code,
                defaults={
                    'city': info.get('city'),
                    'state': info.get('state'),
                    'latitude': info.get('lat'),
                    'longitude': info.get('lon'),
                }
            )

            if is_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Aeroportos importados com sucesso! Criados: {created}, Atualizados: {updated}"
        ))
