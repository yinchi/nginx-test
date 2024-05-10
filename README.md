# Minimal Nginx reverse proxy + Flask example

This repo provides 3 Flask apps and a Nginx reverse proxy to switch between them:

```
/ -> http://home
|- /app1 -> http://app1
|- /app2 -> http://app2
```

To run:

```bash
docker compose down
docker compose build
docker compose up
```
