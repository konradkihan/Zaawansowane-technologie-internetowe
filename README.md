# Zaawansowane-technologie-internetowe
## Wymagania systemowe:
- Zainstalowany Docker
- Dostęp do internetu
## Uruchomienie:
```shell
docker network create 
docker compose up -d
docker exec -it zaawansowane-technologie-internetowe-web-1 python /app/zti/manage.py makemigrations
docker exec -it zaawansowane-technologie-internetowe-web-1 python /app/zti/manage.py migrate
```
## Dostęp:
[Z maszyny lokalnej](http://127.0.0.1:8000)
