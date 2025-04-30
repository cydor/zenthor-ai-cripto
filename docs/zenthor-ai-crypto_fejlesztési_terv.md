Fejlesztési Terv (Roadmap)
Célkitűzések
0.1 verzió (MVP):

Alap infrastruktúra kiépítése: Docker‑alapú konténerizáció, k3d‑alapú lokális Kubernetes környezet, GitHub Actions CI/CD pipeline.

Alapfunkciók implementálása:

Adatgyűjtés (pl. data_collector.py modul) – kriptopénz árfolyamok lekérése, első komoly elemzések (mozgóátlag, RSI, MACD stb.).

Alap kereskedési logika demószámla szimulációval.

Stabil deployment: Kubernetes konfigurációk (deployment.yaml & service.yaml) finomhangolása, pod monitorozás, zeróköltségű megoldások ingyenes VPS‑ek és közösségi felhők használatával.

1.0 verzió (Éles rendszer):

Fejlett AI/ML modulok integrálása:

Komplex prediktív algoritmusok, neurális hálók, idősoros előrejelzés.

Backtesting rendszer bevezetése, mely kompenzálja a tranzakciós, konverziós és adózási tényezőket.

Automatizált kereskedési modul:

Több tőzsdei API integráció, automatikus kereskedés éles környezetben (stop-loss, profit-taking mechanizmusok).

Részleges önfinomítás a visszacsatolási mechanizmusokon keresztül.

Infrastruktúra migráció:

Éles VPS‑re vagy megbízható fizetett cloud platformra történő átállás, skálázható Kubernetes clusterrel, HPA/VPA támogatással.

Ütemezés és Milestone-ok
Fázis 1: 0.1 verzió (0–3 hónap)
Hónap 0–1:

CI/CD pipeline, Dockerfile, Kubernetes (k3d) környezet kiépítése.

Alap GitHub Actions és lokális fejlesztési környezet beállítása.

Hónap 1–2:

data_collector.py modul és alap adatfeldolgozó logika implementálása (API integráció, technikai indikátorok).

Alap demószámla szimuláció és kereskedési logika megújítása.

Hónap 2–3:

Rendszerintegráció, CI/CD tesztek futtatása, fejlesztési hibák kijavítása.

Kubernetes deploy validálása ingyenes VPS‑eken/lokális clusterben.

Fázis 2: 1.0 verzió (4–9 hónap)
Hónap 4–6:

Haladó AI/ML modulok fejlesztése, prediktív modell integrációja.

Backtesting keretrendszer kialakítása, történelmi adatok alapján elemzés.

Hónap 6–9:

Éles kereskedési modul integrálása, API kapcsolatok kiterjesztése több tőzsdére.

Felhasználói interfész (dashboard, riasztási rendszer) és monitoring integrációja.

Migráció éles VPS‑re/megbízható cloud alapra, skálázás konfigurálása (HPA).

Határidők és Mérföldkövek
Infrastruktúra kész: 1 hónap végére.

Adatgyűjtés és alap kereskedési logika: 2 hónap végére.

0.1 verzió MVP átadás: 3 hónapos határidő.

Fejlett AI modulok és backtesting: 4–6 hónap között.

Éles kereskedési rendszer: 9 hónap végére.