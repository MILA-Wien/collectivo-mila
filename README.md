# Mein MILA

An instance of [collectivo](https://github.com/MILA-Wien/collectivo/) for the Austrian cooperative [MILA](https://www.mila.wien/), which is available at:

- Frontend: https://mein.mila.wien/
- Backend: https://collectivo.mila.wien/
- Authentication: https://login.mila.wien/

## Documentation

The documentation of collectivo can be found [here](https://github.com/MILA-Wien/collectivo/).

For local testing of this repository, follow these steps:

1. Install docker and docker-compose.
2. Clone the repository.
3. Copy `.env.example` to `.env` and adopt all the values.
4. Add the following line to your `/etc/hosts/` file: `127.0.0.1 keycloak keycloak.local collectivo.local collectivo.ux`
5. Run `docker compose -f ./docker-compose-dev.yml up -d`
6. Access your instance via https://collectivo.ux, https://collectivo.local, and https://keycloak.local (accept security risk on each)
