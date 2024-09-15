
# Installation
This API uses Django and DRF.
 - Install dependencies : `pip install -r requirements.txt`
 - Create the Database and the tables : `python manage.py migrate`
 - Load demo data :  `python manage.py loaddata demo` (10000 patients generated with Faker)
 - To be able to use the Django admin interface, a user must be created : `python manage.py createsuperuser --username admin --email admin@example.com`  (a password has to be set)
  
  # Running and testing
  - Demo of the API can be run with the Django dev server : `python manage.py runserver`
  - DRF provides a user friendly version of the RestFull API, accessible at `http://127.0.0.1:8000/patients/?email=derrick`
  - Curl command : `curl http://127.0.0.1:8000/patients/?email=derrick -H 'Content-Type: application/json'`
  - Some integration tests exist and can be run with `python manage.py test healthapp`. Tests use their own data and DB (`fixtures/tests.json`).
  - Data of the APP can be managed with Django Admin `http://127.0.0.1:8000/admin/`

# Known limitations
Due to the restricted time and the type of exercise, this API is not production ready :
 - The API is not authenticated, anyone can search and display patients
 - The "partial" match search uses a LIKE SQL query. It works with the technical constraints, but will results in unacceptable response times with more records
 - The API uses the provided SQLite DB (single threaded, not scalable...)
 - Only one search param is usable at a time
 - When searching by Clinician UUID or Clinician department, an InnerJoin is executed, so the list of clinicians associated with patients in the response is also filtered by these criteria. Only clinicians macthing the search will be listed

## Future evolutions
 - Replace the LIKE query with a FullText PostgreSQL search
 - Create other endpoints to manage 
 - Create a Docker version of the App to make easier deployments to different environments
 - Describe the infrastructure with Docker Compose : 
   - The DRF app with a ASGI server like Uvicorn
   - A PostgreSQL docker with a volume to persist data
   - A reverse proxy in front like Nginx