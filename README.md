#### Get repository
 ``` 
git clone https://github.com/patrezelopes/desafio-dev.git
 ``` 

#### Create containers web e db

 ``` 
cd ./library_challenge
 ``` 

### Change default database if using docker or virtual env
'''
DATABASES = {
    'default': {
    # using_env:
    # using_docker:
    }}
''' 

### If using docker:
 ``` 
docker-compose up --build -d
 ``` 

##### Alter role to create db on unit tests
 ```
docker exec -it agriness_lib_db_1 psql -h localhost -U agriness -d agriness_db 

ALTER USER agriness CREATEDB;

exit
 ```

##### To see unit test
 ``` 
docker-compose up --build 
 ``` 

### If using virtual env

### Linux terminal
 ``` 
sudo apt install python3-pip python3-dev libpq-dev virtualenv postgresql postgresql-contrib
 ``` 

### using postgres
'''
psql -h localhost -U postgres 

'''
CREATE ROLE agriness WITH ENCRYPTED PASSWORD 'password' LOGIN;

ALTER ROLE agriness WITH ENCRYPTED PASSWORD '4gr1n3ss' LOGIN;

SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE 
    -- don't kill my own connection!
    pid <> pg_backend_pid()
    -- don't kill the connections to other databases
    AND datname = agriness_db';

CREATE DATABASE agriness_db OWNER agriness ENCODING 'UTF8' TEMPLATE template0 LC_COLLATE 'pt_BR.UTF8' LC_CTYPE 'pt_BR.UTF8';
GRANT ALL PRIVILEGES ON DATABASE agriness_db TO postgres;

ALTER USER agriness CREATEDB;

exit
'''

### Access Database
'''
psql -h localhost -U postgres -d agriness_db
'''


#### creating a virtual env using python 3
 ``` 
virtualenv env_library --python=python3
 ``` 

#### Activating virtual env
 ``` 
source env_library/bin/activate
 ``` 

#### Installing dependencies
 ``` 
pip install -r requirements.txt
 ``` 

#### Building a database changes
 ``` 
python manage.py makemigrations library
 ``` 

#### applying  changes

 ``` 
python manage.py migrate
 ``` 

#### Creating a superuser for tests
 ``` 
python manage.py createtestuser
 ``` 

#### Loading fixture data to test the application
 ``` 
python manage.py loaddata library/fixtures/books.json
python manage.py loaddata library/fixtures/clients.json
python manage.py loaddata library/fixtures/rents.json

or 

python manage.py loaddata library/fixtures/*.json

 ``` 

#### Unit tests
 ``` 
python manage.py test
 ``` 

#### Running application
 ``` 
python manage.py runserver 0.0.0.0:8000
 ``` 

### Access
if you access from ip, replace localhost to <your_ip> in all this document

[click login](http://localhost:8000)

### Login
user: teste, password: teste
[click login](http://localhost:8000/api-auth/login)


### Register a new application
Access [link register](http://localhost:8000/authenticate/applications/register/) and register application with this values:

|  Application fields|  |
| --- | --- 
| name |agriness_auth
|client_id|FMWr3BkTUuYQRdP2gAVmj1a7DdnvOGg25apiHgkb
|client_secret|APwMBjwNmQaSDza6iHzNhZvraSmWl4GYpAUdrbR0gKB2aQ675Qnd6t7zSGvrEXErfkpjThEPcyjzhl8vP5CZJ0L48T36AZVkfsrrTbYB0w9WDdpKDUKwVmzNzAoUzoKl
|client_type | confidential
|authorization_grant_type | authorization_grant_type
|redirect_uris | http://localhost:8000/
|algorithm | No OIDC support


## Endpoint:
### Books List 
[Book list: http://localhost:8000/books](http://localhost:8000/books)
Method GET
 ```
 [
  {
    "url": "http://localhost:8000/books/1/",
    "name": "Harry Potter e a Pedra Filosofal",
    "author": "J.K. Rowling"
  },
  {
    "url": "http://localhost:8000/books/2/",
    "name": "O Código Da Vinci",
    "author": "Dan Brown"
  },
  {
    "url": "http://localhost:8000/books/3/",
    "name": "A Guerra dos Tronos",
    "author": "R. R. Martin"
  }
...
]
```

### Reserve a Book
[Book list: http://localhost:8000/books/<book_id>/reserve](http://localhost:8000/books/1/reserve)
Method POST
 ```
 [
  {
    "url": "http://localhost:8000/books/1/",
    "name": "Harry Potter e a Pedra Filosofal",
    "author": "J.K. Rowling"
  },
  {
    "url": "http://localhost:8000/books/2/",
    "name": "O Código Da Vinci",
    "author": "Dan Brown"
  },
  {
    "url": "http://localhost:8000/books/3/",
    "name": "A Guerra dos Tronos",
    "author": "R. R. Martin"
  }
...
]
```

#### Curl test to set a reserve

```
curl --request POST \
  --url http://localhost:8000/books/3/reserve/ \
  --header 'Authorization: Bearer NQAnnY7VOag3sHTqwAU2RExsw4IzKV' \
  --header 'Content-Type: application/json' \
  --data '{
		"client":"3",
		"rented_at":"2021-06-04T11:46Z"
}'
```
### CLient List
[Client list: http://localhost:8000/client](http://localhost:8000/client)
```
[
  {
    "url": "http://localhost:8000/client/1/",
    "name": "Patreze Lopes"
  },
  {
    "url": "http://localhost:8000/client/2/",
    "name": "José da Silva"
  },
  {
    "url": "http://localhost:8000/client/3/",
    "name": "Maria Souza"
  }
...
]
```
### CLient Reserves List
[Reserves by client: http://localhost:8000/client/<client_id>/books](http://localhost:8000/client/1/books)
```
[
  {
    "client": "Patreze Lopes",
    "book": "A Guerra dos Tronos",
    "rented_at": "2021-06-04T11:46:00Z",
    "finerate": "0.28600"
  },
  {
    "client": "Patreze Lopes",
    "book": "Harry Potter e a Pedra Filosofal",
    "rented_at": "2021-07-01T11:46:00Z",
    "finerate": "0.12400"
  }
...
]
```


**for more**
##### Run django shell
run web python manage.py shell

##### Down containers web e db
docker-compose down
