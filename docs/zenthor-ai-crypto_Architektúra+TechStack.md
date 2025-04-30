. Architektúra + Tech Stack
Infrastruktúra
Alap környezet:

Docker: A kód konténerizált futtatása a python:3.13-slim image alapján, mely minimalista és hatékony.

Kubernetes: Lokális fejlesztéshez/teszteléshez a k3d használata; később éles VPS‑ek, vagy cloud alapú Kubernetes cluster.

CI/CD: GitHub Actions – container alapú pipeline futtatással, gyors cache-eléssel (actions/cache@v4).

Fizetési/infrastruktúra stratégia:

Kezdeti fázis: Ingyenes VPS-ek, közösségi cloud szolgáltatások, lokális k3d környezet.

Éles rendszer: Megbízható, fizetett VPS‑ek/cloud platform optimalizált erőforrás-kezeléssel (HPA, monitoring eszközök).

Komponensek
Alkalmazás réteg:

main.py: A fő belépési pont, amely összehangolja a modulokat.

Modulok:

Data Collector: data_collector.py – API hívások, adatok előfeldolgozása.

Kereskedési logika: Automatizált kereskedési döntések, demószámla szimuláció.

Előrejelző modul: Technikai indikátorok és előrejelző modellek.

Backend infrastruktúra:

Dockerfile: Olyan rétegezett build, mely a requirements.txt alapján telepíti a függőségeket, majd másolja a kódot.

Kubernetes Deploy:

deployment.yaml: 2 replica (teszteléshez), resource limit, liveness probe, command: ["python", "main.py"].

service.yaml: NodePort-alapú service a könnyű külső eléréshez.

HPA/VPA: A jövőbeni skálázási követelményekhez.

CI/CD
GitHub Actions Pipeline:

Workflow lépések:

Kód letöltése (actions/checkout@v2),

Cache lépés (actions/cache@v4),

Python környezet beállítása (actions/setup-python@v2),

Függőségek telepítése,

Tesztek futtatása (pl. python -m unittest discover),

Docker CLI telepítése és image build.

Cache optimalizáció: A pip cache gyors telepítést biztosít, így csökkentve a build időt.

Monitoring & Logging:

Későbbi integráció: Prometheus, Grafana, ELK stack az éles környezethez a hatékony rendszerfelügyelet érdekében.

Tech Stack
Programozási nyelv: Python (3.13)

Konténerizáció: Docker

Kubernetes: k3d (lokális fejlesztés), éles esetben valódi cluster

CI/CD: GitHub Actions

Adatfeldolgozás: Pandas, NumPy

Web framework (később): Flask/Django, ha lesz felhasználói dashboard

Monitoring: Prometheus/Grafana a jövőbeni skálázáshoz