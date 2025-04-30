AI/ML Modul Specifikáció
Módszerek
Technikai indikátorok:

RSI, MACD, Bollinger Bands, mozgóátlagok, volumen-analízis.

Kezdeti modellek:

Statisztikai predikciók: Egyszerű regressziós modellek, idősori előrejelzés (például ARIMA).

Könnyű ML modellek: Döntési fák, random forest, vagy kisebb neurális hálók a korai fázisban.

Tanulási Stratégiák
Felügyelt tanulás:

Történelmi adatok (árfolyamok, volumen) alapján a modell betanítása és validálása.

Reinforcement Learning (későbbi integráció):

Keretrendszer kidolgozása, ahol a rendszer demószámlán szimulálva tanulja meg a kereskedést (pl. Q-learning, DQN).

Folyamatos tanulás és finomhangolás:

A trade visszacsatolások és teljesítménymutatók alapján a modell időszakonként újratanítása, a stratégiák finomhangolása.

Adatkészletek
Történelmi pénzügyi adatok:

Kriptovaluta árfolyamok, tőzsdei adatok (lehet publikus API-kon keresztül beszerezni, pl. Binance, Coinbase, Kraken).

Nyílt forráskódú projektek és GitHub források:

Releváns open source kripto kereskedési adatkészletek, piaci statisztikák.

Valós idejű adatok:

API-k segítségével friss adatok folyamatos lekérése a valós idejű elemzéshez.

Backtest Elvárások
Időtartam:

Legalább 2 év historikus adatok használata, hogy a modell robusztusságát mérjük különböző piaci körülmények között.

Metrikák:

Profitabilitás, volatilitás, drawdown, Sharpe-ratio, visszatérési mutatók.

Költségszámítás:

Tranzakciós költségek, slippage, adó- és konverziós költségek figyelembe vétele.

Szcenárió elemzés:

Stressztesztek, Monte Carlo szimulációk, különböző piaci állapotok (bull, bear, oldalazó piac) modellezése.