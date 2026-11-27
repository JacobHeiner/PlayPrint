"""Refresh only PlayPrint's selected games; never export the RAWG database."""
import datetime
import json
import os
import pathlib
import urllib.parse
import urllib.request

key = os.environ.get("RAWG_API_KEY")
if not key:
    raise SystemExit("RAWG_API_KEY repository secret is missing.")
out = pathlib.Path("rawg-games")
out.mkdir(exist_ok=True)
def request(path, **params):
    url = "https://api.rawg.io/api/" + path + "?" + urllib.parse.urlencode(dict(params, key=key))
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            return json.load(response)
    except Exception:
        raise SystemExit("RAWG request failed; check API access and quota.") from None

def norm(s):
    return "".join(c for c in s.casefold() if c.isalnum())

def record(g):
    return {"rawgId": g["id"], "name": g["name"], "slug": g["slug"],
            "released": g.get("released"), "image": g.get("background_image"),
            "developers": [d["name"] for d in g.get("developers", [])],
            "platforms": [p["platform"]["name"] for p in g.get("platforms", [])],
            "genres": [x["name"] for x in g.get("genres", [])]}

titles = ["The Legend of Zelda: Ocarina of Time", "The Legend of Zelda: Twilight Princess",
"The Legend of Zelda: Majora’s Mask", "The Legend of Zelda: Breath of the Wild",
"The Legend of Zelda: Tears of the Kingdom", "Red Dead Redemption 2", "Halo 2", "Halo 3",
"Halo 5", "Halo Infinite", "Tinykin", "Valorant", "Boomerang Fu", "Lethal Company",
"Helldivers 2", "A Hat in Time", "Fortnite", "Super Mario 64", "Super Mario Odyssey"]
# Only exact title matches; ambiguous or missing titles remain manual.
rows = []
for title in titles:
    hits = request("games", search=title, search_exact="true", page_size=10).get("results", [])
    matches = [g for g in hits if norm(g["name"]) == norm(title)]
    if len(matches) != 1:
        continue
    g = record(request("games/" + str(matches[0]["id"])))
    g["playprintTitle"] = title
    rows.append(g)
# A small rotating selection of recent releases, not a bulk catalog.
today = datetime.date.today()
recent = request("games", dates=f"{today-datetime.timedelta(days=14)},{today}", ordering="-added", page_size=8)
for item in recent.get("results", [])[:8]:
    if not any(g["rawgId"] == item["id"] or norm(g["name"]) == norm(item["name"]) for g in rows):
        rows.append(record(request("games/" + str(item["id"]))))
for g in rows:
    (out / (str(g["rawgId"]) + ".json")).write_text(json.dumps(g, ensure_ascii=False), encoding="utf-8")
index = [{"rawgId": g["rawgId"], "name": g.get("playprintTitle", g["name"])} for g in rows]
(out / "index.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
# Remove obsolete rotating entries from the current tree.
keep = {str(g["rawgId"]) + ".json" for g in rows} | {"index.json"}
for p in out.glob("*.json"):
    if p.name not in keep:
        p.unlink()
print(f"Refreshed {len(rows)} selected games.")
