# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗  
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝  
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═  
# Zenthor AI-Crypto

## 🧠 Leírás

Zenthor AI-Crypto egy nyílt forráskódú, mesterséges intelligencián alapuló, konténerizált kriptokereskedési rendszer.  
Fő célja egy **valós idejű, skálázható, tanulóképes kereskedő infrastruktúra** létrehozása.

Ez a projekt kifejezetten oktatási és kutatási célokra készült, támogatja a *sandbox trading* (pl. Binance Futures Testnet) környezeteket.

---

## 🔧 Főbb funkciók

- ✅ Valós idejű árfolyam adatgyűjtés (Binance CCXT API)
- ✅ Technikai indikátorok számítása (Pandas, NumPy)
- ✅ Paper trading és tesztpozíció nyitás/zárás
- 🔜 Több tőzsde támogatás (Bybit, OKX)
- 🔜 Tőzsdék közötti arbitrázs modul
- 🔜 AI/ML predikciós modul (XGBoost, sklearn)
- 🔜 Dashboard megjelenítés (Streamlit, Grafana)

---

## ⚙️ Technológiák

- **Python 3.13**, `ccxt`, `pandas`, `streamlit`
- **Docker**, `docker-compose`, `GitHub Actions CI`
- **Kubernetes-ready** (Helm chart, deployment.yaml, service.yaml)
- **GitHub CI/CD**, `.github/workflows/docker-build.yml`

---

## 🗂️ Fájlstruktúra
zenthor-ai-cripto/
├── config/ # dev/test/prod JSON fájlok
├── core/ # config loader, jövőbeli core logika
├── binance_scalper/ # demo skalpoló modul
├── data_collector.py # alap CCXT adatgyűjtő modul
├── main.py # belépési pont (HTTP szerver + loop)
├── Dockerfile # konténeresítés
├── entrypoint.sh # környezetfüggő induló script
└── .github/workflows/ # GitHub Actions pipeline


---

## 🧪 Tesztelés / Futás

### Docker build & run (példa dev környezetre)

```bash
docker build --build-arg ENV=dev -t zenthor-ai-cripto .
docker run -e ENV=dev -p 8080:8080 zenthor-ai-cripto


CI/CD pipeline
Push-ra automatikus build indul (main branch):

.github/workflows/docker-build.yml lefuttatja a buildet

Ellenőrzi a JSON fájlokat

Tesztfuttatást végez

🛡️ Licenc
MIT – Lásd: LICENSE

⚠️ Felelősség kizárás: Ez a projekt kizárólag oktatási célra készült. Valódi pénzügyi műveletek végrehajtása kizárólag saját felelősségre történik.

| Verzió | Funkciók                                    |
| ------ | ------------------------------------------- |
| `v0.1` | Alap pipeline, adatgyűjtés, konténer építés |
| `v1.0` | Paper trading, demóstratégia                |
| `v1.1` | AI predikciók, arbitrázs logika             |
| `v2.x` | Valódi tőzsdei integráció, monitorozás      |


