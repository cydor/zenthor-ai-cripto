# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗        
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝        
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═        
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐       
# ╠═╣║  │  ├┬┘│├─┘ │ │ │       
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘       
# ╔╗ ╦ ╦╦╦  ╔╦╗   ┬   ╦═╗╦ ╦╔╗╔
# ╠╩╗║ ║║║   ║║  ┌┼─  ╠╦╝║ ║║║║
# ╚═╝╚═╝╩╩═╝═╩╝  └┘   ╩╚═╚═╝╝╚╝

# Alapértelmezett (dev mód):
docker build -t zenthor-ai-cripto .
💡 Csak a kívánt környezethez tartozó JSON kerüljön be .dockerignore alapján!

#Dockerfile-on belül választható környezet – dev, prod, test
# Explicit prod:
# ▶ Környezeti típus  alapértelmezett érték: dev
#ARG ENV=dev
#ENV ENV=$ENV
docker build --build-arg ENV=prod -t zenthor-ai-cripto .

# Futtatás:
docker run -e ENV=prod -p 8080:8080 zenthor-ai-cripto


# Build és Run parancsok – Zenthor AI-Crypto

## Docker build

```bash
docker build -t zenthor-ai-cripto .
docker build --build-arg ENV=prod -t zenthor-ai-cripto .

## Docker PROD Build & RUN
docker build --build-arg ENV=prod -t zenthor-ai-cripto .
docker run -e ENV=prod -p 8080:8080 zenthor-ai-cripto

## Docker DEV Build & RUN # Alapértelmezett (dev mód)
docker build -t zenthor-ai-cripto .
docker run -e ENV=dev -p 8080:8080 zenthor-ai-cripto


## Docker TEST Build & RUN
docker build --build-arg ENV=test -t zenthor-ai-cripto .
docker run -e ENV=test -p 8080:8080 zenthor-ai-cripto

## 🔄 BuildKit aktiválása (gyorsabb buildhez)
```bash
DOCKER_BUILDKIT=1 docker build -t zenthor-ai-cripto .
💡 BuildKit gyorsabb, cache-barát és jobban kezeli párhuzamos pip install-t is.

## Docker PROD Build & RUN
docker build --build-arg ENV=prod -t zenthor-ai-cripto .
DOCKER_BUILDKIT=1 docker run -e ENV=prod -p 8080:8080 zenthor-ai-cripto .

## Docker DEV Build & RUN # Alapértelmezett (dev mód)
docker build -t zenthor-ai-cripto .
DOCKER_BUILDKIT=1 docker run -e ENV=dev -p 8080:8080 zenthor-ai-cripto


## Docker TEST Build & RUN
docker build --build-arg ENV=test -t zenthor-ai-cripto .
DOCKER_BUILDKIT=1 docker run -e ENV=test -p 8080:8080 zenthor-ai-cripto

