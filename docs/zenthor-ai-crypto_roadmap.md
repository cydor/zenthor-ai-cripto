# Zenthor AI-Crypto – Fejlesztési Roadmap

## Fázis 0 – Előkészítés

### Jog & Compliance
A projekt célja hobbifejlesztés, oktatási célokra. A rendszer a GDPR és API használati feltételek figyelembevételével készül, éles pénzkezeléshez később jogi felülvizsgálat szükséges.

### Technológiai döntések

- Docker használata: a széles körű tooling és CI/CD támogatás miatt.
- k3d a Kubernetes fejlesztési környezethez: egyszerűbb és jobban integrálható, mint kind.
- CI/CD: GitHub Actions és Helm alapú automatikus telepítési pipeline kialakítása.

## Fázis 1 – MVP (1–3 hónap)

### Technológiai stack

- Python 3.13 + FastAPI + SQLAlchemy + SQLite vagy DuckDB.
- Redis (vagy memória cache) a valós idejű adatokhoz.
- GitHub Actions + Docker + k3d + Helm.

### Modulok

- `main.py`: FastAPI szolgáltatás egészségügyi és predikciós endpointokkal.
- `data_collector.py`: Binance API integráció CCXT segítségével.
- `indicators.py`: Technikai indikátorok (RSI, MACD, Bollinger Bands).
- `simulator.py`: Paper trading modul SQLite alapú portfólióval.
- `ml_model.py`: Baseline modellek (Linear Regression, XGBoost).

## Fázis 2 – AI Bővítés (4–6 hónap)

### Adat pipeline
- Collect → Clean → Transform lépések meghatározása és implementálása.

### Modellezés és tesztelés
- Baseline: XGBoost, Linear Regression.
- Kísérleti: LSTM, Prophet.
- Validáció: cross-validation és walk-forward analysis.
- Metrikák: Sharpe ratio, drawdown, precision@trade.
- Drift monitoring bevezetése.

## Fázis 3 – Élesítés és skálázás (6–9 hónap)

- Kulcskezelés Vault vagy környezeti változók segítségével.
- RBAC szabályok bevezetése Kubernetes-ben.
- HPA + Prometheus + Grafana használata.
- Loggolás: loguru vagy structlog.
- Riasztások: Telegram vagy Discord webhook.
- GitOps szinkronizáció: GitHub Actions + Helm upgrade.
- Rollback lehetőség Helm verziózással.
- Blue-Green deploy nem szükséges egyfelhasználós környezetben.

## CI/CD Jegyzetek

- A build → test → deploy folyamatot GitHub Actions hajtja végre.
- Helm chartot használunk a Kubernetes deploymentekhez.
- Pre-deploy és post-deploy tesztek beépítve.

## Felelősségáthárítás

> Ez a szoftver kizárólag oktatási és demó célokra készült. Az élő kereskedéshez szükséges jogi megfelelés, pénzügyi engedély és audit nem része a jelenlegi verziónak. A szoftvert mindenki saját felelősségére használhatja.
