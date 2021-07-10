#### Get repository
 ``` 
git clone https://github.com/patrezelopes/desafio-dev.git
 ``` 

#### Create containers web e db
 ``` 
cd ./library_challenge
 ``` 

### Using docker:
 ``` 
docker-compose up --build -d
 ``` 

### Using virtual env
 ``` 
sudo apt install virtualenv
 ``` 

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
