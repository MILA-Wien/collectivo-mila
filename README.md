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
4. Add the following line to your `/etc/hosts/` file: `127.0.0.1 keycloak`
5. Run `docker compose -f ./docker-compose-dev.yml up -d`
6. Access your instance via https://127.0.0.1, and https://keycloak.local (accept security risk on each)


## Habidat

In order to set up the habidat integration, you need to start the container without a volume mounted to config and then run the following commands:

```
cd ./docker/habidat && docker cp habidat:/app/config ./config
```

Then you can start the container with the volume mounted to config.
