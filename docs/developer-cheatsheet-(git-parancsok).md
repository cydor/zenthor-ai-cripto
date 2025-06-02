# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗        
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝        
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═        
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐       
# ╠═╣║  │  ├┬┘│├─┘ │ │ │       
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘       
# ╔╗ ╦ ╦╦╦  ╔╦╗   ┬   ╦═╗╦ ╦╔╗╔
# ╠╩╗║ ║║║   ║║  ┌┼─  ╠╦╝║ ║║║║
# ╚═╝╚═╝╩╩═╝═╩╝  └┘   ╩╚═╚═╝╝╚╝

---

# 🧠 GIT és DOCKER fejlesztői jegyzet – *Zenthor AI-Crypto*

---

## 🔍 Változások ellenőrzése

```powershell
git status
```

> 💬 Megmutatja, mely fájlok változtak meg, mik nincsenek verziókezelés alatt, és mi van stage-elve commit előtt.

---

## ✅ Minden változás hozzáadása, commit és push

```powershell
git add .
git commit -m "♻️ összes fájl aktualizálása"
git push origin main
```

> 🔁 Ha sok fájl változott, és csak egy egyszerű, általános commit-ot szeretnél.

---

## ✅ Egy konkrét fájl commitolása

```powershell
git add .github/workflows/docker-build.yml
git commit -m "🛠️ CI: YAML teljesen hibamentesítve (yamllint clean)"
git push origin main
```

> 🔍 Használd, ha csak 1 vagy néhány fájlt módosítottál, így célzott lesz a commit.

---

## 🔁 Előző commit módosítása (pl. ha elfelejtettél valamit)

```powershell
git add <fájl>
git commit --amend --no-edit
```

> ⏪ Hozzáfűzi a változást az előző commit-hoz *anélkül*, hogy új commit jönne létre.

---

## 📁 Git fájlok ellenőrzése

```powershell
git ls-files config/
```

> 📂 Felsorolja a verziókövetés alatt lévő fájlokat egy adott mappában.

```powershell
git log -p config/dev.json
```

> 📜 Megmutatja a `config/dev.json` módosításainak előzményeit diff-el együtt.

---

## 🧪 YAML fájl szintaxis ellenőrzése

```powershell
yamllint .github/workflows/docker-build.yml
```

> ✅ Ellenőrzi a YAML fájlt szintaktikai hibákra (pl. behúzás, sortörés, dokumentum kezdete).

**Hasznos hibaüzenetek:**

* `mapping values are not allowed here` → rossz behúzás vagy `:` után rossz karakter
* `truthy value` → `yes` helyett `true`, `no` helyett `false` a YAML szerint

---

## 🐳 Docker parancsok – Lokális teszt (csak ha kell)

```powershell
docker build --build-arg ENV=dev -t zenthor-ai-cripto .
docker run --rm zenthor-ai-cripto cat /app/config/dev.json
```

> 🧪 Lokális build és futtatás. Csak akkor szükséges, ha nem akarod megvárni a GitHub Actions eredményt.

---

## 🧼 Használati javaslat (ha pár hetet kihagytál)

* **Minden módosítás után**: `git status`
* **Ha minden fájl módosult**: `git add .` és commit
* **Ha csak pár fájl**: add külön, commit külön
* **CI hiba esetén**: futtasd `yamllint` és olvasd a GitHub Actions logot
* **A `dev.json` fájlt mindig ellenőrizd a konténerben is**, ha config betöltési hiba van

---

## ✅ Használatra kész `docker-build.yml` (YAML validált)

Ha kéred, legközelebb be is másolom ide frissen, csak szólj!

---

Ha szeretnéd, elmenthetem neked ezt a dokumentumot `.docs/developer-cheatsheet.md` formátumban, amit be is commitolhatsz, és ott lehet a repódban állandó emlékeztetőként. Mondjam a parancsokat hozzá?
