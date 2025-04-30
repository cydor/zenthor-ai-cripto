# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
#
# Zenthor AI-Crypto Dockerfile
# Fejlesztési környezet Python 3.13 + containerized runtime

# ▶ Alap image: a hivatalos slim változat, kis méret, nincs felesleges extra
FROM python:3.13-slim

# ▶ Munkakönyvtár beállítása
# A konténeren belül minden itt fog futni, ez lesz az alapértelmezett context
WORKDIR /app

# ▶ Környezeti típus beállítása: alapértelmezett érték: dev
ARG ENV=dev
ENV ENV=$ENV

# ▶ Csak a requirements.txt másolása először
# Ha csak a kód változik, de a dependencies nem, a Docker cache miatt nem kell újra pip install-t futtatni
COPY requirements.txt .

# ▶ Függőségek telepítése
# --no-cache-dir → kisebb image méret, nem menti le a cache-t
RUN pip install --no-cache-dir -r requirements.txt

# ▶ Projektfájlok másolása
# Ezután jön a teljes projekt (main.py, modulok, logo.txt stb.)
COPY . .

# ▶ Entrypoint script végrehajthatóvá tétele (Windows alatt ez kötelező itt)
RUN chmod +x entrypoint.sh

# ▶ Port kitétele a konténeren belül
# 8080 → nem root port, FastAPI vagy saját HTTP szerver itt fusson
EXPOSE 8080

# ▶ Alkalmazás futtatása
# Ez a konténer indulásakor fut le. Feltételezi, hogy van egy main.py belépési pont.
CMD ["python", "main.py"]
LABEL maintainer="zenthor <zenthor@gmail.com>"
LABEL version="0.1"

# ▶ Indítás bash wrapperen keresztül (érzékeli a környezetet)
ENTRYPOINT ["./entrypoint.sh"]
