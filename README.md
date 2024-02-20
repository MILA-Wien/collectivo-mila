This is an archived version of Collectivo MILA. The current version has been moved to: [https://github.com/collectivo-dev/collectivo](https://github.com/MILA-Wien/mila-server)

# Mein MILA - Collectivo

An instance of [Collectivo](https://github.com/MILA-Wien/collectivo/) for the Austrian cooperative [MILA Mitmach-Supermarkt](https://www.mila.wien/).

- Frontend: https://mein.mila.wien/
- Backend: https://collectivo.mila.wien/
- Authentication: https://login.mila.wien/

## Documentation

The documentation of Collectivo can be found at https://collectivo.io.

### Local testing

For local testing of this repository, follow these steps:

1. Install docker and docker-compose.
2. Clone this repository, the backend repository, and the frontend repository in the same project folder.
3. Copy `.env.example` to `.env` and adopt all the values.
4. Add the following line to your `/etc/hosts/` file: `127.0.0.1 keycloak`
5. Run `docker compose -f ./docker-compose-dev.yml up -d`

You can then access the following instances:

- Frontend: http://localhost:5173/
- Backend: http://localhost:8000/
    - Swagger: `api/docs/`
    - Healthcheck: `api/core/health/`
- Keycloak: http://localhost:8080/
- Docs: http://localhost:8003/

### Habidat

In order to set up the habidat integration, you need to start the container without a volume mounted to config and then run the following commands:

```
cd ./docker/habidat && docker cp habidat:/app/config ./config
```

Then you can start the container with the volume mounted to config.
