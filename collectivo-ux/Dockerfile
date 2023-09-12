# Use node as base image
FROM node:18 AS build-env

# Create app directory
WORKDIR /app

ENV TZ=Europe/Vienna
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install app dependencies
ENV VERSION=v0.7.2
RUN git clone --depth 1 --branch ${VERSION} https://github.com/MILA-Wien/collectivo-ux .

# Copy extensions into the root of the collectivo app
COPY ./collectivo.json /app/src/collectivo.json
COPY ./extensions /app/src/extensions
COPY ./favicon.ico /app/public/favicon.ico

RUN  yarn install --frozen-lockfile

# If you are building your code for production
RUN yarn build

# Running
FROM nginx:alpine
COPY --from=build-env /app/dist /usr/share/nginx/html
COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/custom.conf
COPY ./docker/collectivo-ux-entrypoint.sh /docker-entrypoint.d/10-collectivo-ux-entrypoint.sh
