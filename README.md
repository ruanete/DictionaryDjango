# DictionaryDjango
Dictionary web application implemented with web framework Django.

## Deployment
1. ```docker-compose up -d --build```
2. ```docker-compose exec dictionary_django python manage.py makemigrations dictionary_django```
3. ```docker-compose exec dictionary_django python manage.py migrate```
4. ```docker-compose exec dictionary_django python manage.py createsuperuser```
5. ```docker-compose down```

## Testing
```docker-compose exec dictionary_django python manage.py test```
