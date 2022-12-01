# MILA collectivo

An instance of [collectivo](https://github.com/MILA-Wien/collectivo/) for the Austrian cooperative [MILA](https://www.mila.wien/), which is available at:

- Frontend: https://mein.mila.wien/
- Backend: https://collectivo.mila.wien/
- Authentication: https://login.mila.wien/

## Custom extensions

- mila_members

## Development

For local development and testing, use:

```shell
docker compose -f ./docker-compose-dev.yml build
```

```shell
docker compose -f ./docker-compose-dev.yml up -d
```

For further information, see [collectivo](https://github.com/MILA-Wien/collectivo/).

## Secrets

A file `.env` has to be added with the following attributes:

```
KEYCLOAK_ADMIN = '...'
KEYCLOAK_ADMIN_PASSWORD = '...'
KEYCLOAK_CLIENT_SECRET_KEY = '...'

COLLECTIVO_DB_USER = '...'
COLLECTIVO_DB_PASSWORD = '...'

COLLECTIVO_SECRET_KEY = '...'
```
