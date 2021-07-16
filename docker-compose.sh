#!/bin/bash
echo "version: '3.8'
services:
  server:
    container_name: song_server
    image: bludobson/song_server:latest
    build: ./server
    ports:
    - target: 5000
      published: 5000
    environment:
      DATABASE_URI: ${DATABASE_URI}
    deploy:
      replicas: 4
  artist_api:
    container_name: artist_api
    image: bludobson/artist_api:latest
    build: ./artist_api
    deploy:
      replicas: 2
  random_api:
    container_name: random_api
    image: bludobson/random_api:latest
    build: ./random_api
    environment:
      str_len: 4
    deploy:
      replicas: 2
  song_api:
    container_name: song_api
    image: bludobson/song_api:latest
    build: ./song_api
    deploy:
      replicas: 2" > docker-compose1.yaml