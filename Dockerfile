###################
#                                 #
# zenthor_ai_crypto    #
#                                 #
###################

# Python 3.13 alap image
FROM python:3.13-slim

# Állítsd be a munkakönyvtárat
WORKDIR /app

# Másold át a requirements.txt fájlt (ha még nem létezik, hozz létre egyet)
# Másolj csak a requirements fájlt, hogy ha csak a kód változik,
# a függőségek telepítését ne kelljen újra végrehajtani
COPY requirements.txt .


# Telepítsd a függőségeket – ez a lépés cache-elhető lesz, ha 
# a requirements.txt nem változik
RUN pip install --no-cache-dir -r requirements.txt


# Másold át a teljes projektet a konténerbe
COPY . .

# Alkalmazás indítása – a main.py futtatása
# Alkalmazás indítása – itt feltételezzük, hogy lesz egy main.py, ami összekapcsolja a modulokat.
CMD ["python", "main.py"]
