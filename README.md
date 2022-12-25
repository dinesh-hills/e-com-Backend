# e-com-Backend

### Prerequisities
- python


### Installation

Using docker (recommended):

```docker
docker compose up --build
```

Using pip:

```bash
pip install -r requirements.txt
```

### Starting the server
> Using docker compose, the server would have started at localhost:8000

Using python
```python
python manage.py runserver
```
> --optionally you can add runserver host:port

- django dev server starts default at localhost:8000

> Create superuser to login to the admin site.
```python
python manage.py createsuperuser
```
### Authentication
- /auth/users
> hit this endpoint to create a new user.
- /auth/jwt/create
> Generate refresh and access token by posting a valid username and password.
- /auth/jwt/refresh
> To generate new access token.
> Note: For dev purpose the access token lifetime is set to 1 day. change this with SIMPLE_JWT config in Ecom_store/settings/common.py

### Endpoints to explore
on developement environment, django rest framework provides a beautiful api web interface to interact and test your api functions.

- /store
> go to this endpoint on your browser and top left you could find "Api root" on click it gives you all the avaiable endpoints from the root /store eg. /store/products/:id/reviews/:id.

Raise issues incase of any issues. xd

[Twitter](https://www.twitter.com/dineshhills)
