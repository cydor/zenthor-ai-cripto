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
# 🐍 Python slim image – gyorsabb és kisebb
FROM python:3.13-slim

# ▶ Munkakönyvtár beállítása
# A konténeren belül minden itt fog futni, ez lesz az alapértelmezett context
WORKDIR /app

# ▶ Környezeti típus beállítása: alapértelmezett érték: dev
ARG ENV=dev
ENV ENV=$ENV

# ▶  Külön csak requirements.txt – hogy pip install cache-elhető legyen
# 🔽 Ha csak a kód változik, de a dependencies nem, a Docker cache miatt nem kell újra pip install-t futtatni
COPY entrypoint.sh ./entrypoint.sh
COPY requirements.txt .
ENV PIP_CACHE_DIR=/root/.cache/pip 
#Ez cache-elni fogja a következő buildnél (ha nem változott semmi). Ha BuildKit is aktív, ez különösen jól jön.
# ▶   Függőségek cache-elhető telepítése
# 📦--no-cache-dir → kisebb image méret, nem menti le a cache-t
RUN pip install --no-cache-dir -r requirements.txt

RUN ls -lah . && echo "✅ Ellenőrzés: fájlok jelen vannak a build contextben"


# ▶ Projektfájlok másolása
# 📁 Teljes projekt másolása csak ezután (main.py, modulok, logo.txt stb.)
# Biztonság kedvéért külön a config is
#COPY config/ ./config/
# ▶ Teljes projektfájlok bemásolása
COPY . .

# ▶ Fájlok ellenőrzése, újramásolás ha kell
RUN echo "🔍 Fájlok ellenőrzése..." \
 && for f in config/dev.json main.py; do \
      echo "⏳ Ellenőrzés: $f"; \
      if [ ! -f "$f" ]; then \
        echo "❌ $f hiányzik, újramásolás..."; \
        cp "./$f" "./$f" || echo "⚠️ Nem sikerült másolni $f"; \
      else \
        echo "✅ $f megvan."; \
      fi; \
   done \
 && echo "✅ Fájlok ellenőrzése kész."


# ▶ Debug: mutasd meg a config tartalmát
RUN echo "📂 config/dev.json tartalma:" && cat config/dev.json



RUN echo "🗂️ Debug: config mappa tartalma:" && ls -l config/
RUN echo "📁 config/dev.json tartalma:" && cat config/dev.json


# ▶ Entrypoint script végrehajthatóvá tétele (Windows alatt ez kötelező itt)
# 🛡️ Fájljog (csak ha van entrypoint.sh)
RUN chmod +x entrypoint.sh

# ▶ Port kitétele a konténeren belül
# 8080 → nem root port, FastAPI vagy saját HTTP szerver itt fusson
# 🌐 Port kinyitása
EXPOSE 8080

# ▶ Alkalmazás futtatása
# Ez a konténer indulásakor fut le. Feltételezi, hogy van egy main.py belépési pont.
#CMD ["python", "main.py"]
#CMD ["python", "ci_test_main.py"]
CMD ["python", "ci_test_data_collector.py"]
CMD ["sleep", "5"]


LABEL maintainer="zenthor <zenthor@gmail.com>"
LABEL version="0.1"

# ▶ Indítás bash wrapperen keresztül (érzékeli a környezetet)
# 🔁 Wrapper script – ha van környezeti logika
ENTRYPOINT ["./entrypoint.sh"]

