#!/usr/bin/env python3
"""Download high-res festival background images from Wikimedia Commons."""
import urllib.request, ssl, time, sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "deliverables/card-news-instagram/images"
OUT.mkdir(parents=True, exist_ok=True)

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# slug -> (filename, url, note)
TARGETS = [
    ("01-lotus-lantern-wiki.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/2/21/Lotus_Lantern_Festival_at_Jogyesa%2C_Seoul.jpg",
     "Jogyesa Temple Seoul - exact match"),
    ("02-global-culture-wiki.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/8/8f/Dongdaemun_Design_Plaza_at_night%2C_Seoul%2C_Korea.jpg",
     "DDP at night Seoul - exact venue"),
    ("03-jamsugyo-bridge-wiki.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/b/bf/Banpo_Bridge_Moonlight_Rainbow_Fountain_at_night_-_2023-08-14.jpg",
     "Banpo/Jamsugyo Rainbow Fountain at night - exact location"),
    ("04-rose-festival-wiki.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/a/af/Roses_in_Kana_Garden%2C_Hiratsuka%2C_Japan.jpg",
     "Roses in full bloom - thematic"),
    ("05-garden-expo-wiki.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/9/99/Seoul_botanic_park_04.jpg",
     "Seoul Botanic Park - Seoul venue"),
]

for i, (fname, url, note) in enumerate(TARGETS):
    out_path = OUT / fname
    if out_path.exists() and out_path.stat().st_size > 50_000:
        print(f"SKIP {fname} (already {out_path.stat().st_size//1024} KB)")
        continue
    delay = 8
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "TripCraftKorea/1.0 (https://example.com; contact@example.com) Python-urllib",
                "Accept": "image/jpeg,image/png,*/*",
            })
            with urllib.request.urlopen(req, context=CTX, timeout=90) as r:
                data = r.read()
            out_path.write_bytes(data)
            print(f"OK  {fname}  {len(data)//1024} KB  ({note})")
            break
        except urllib.error.HTTPError as e:
            print(f"  attempt {attempt+1}: HTTP {e.code} - sleeping {delay}s")
            time.sleep(delay)
            delay *= 2
        except Exception as e:
            print(f"ERR {fname}  {e}")
            break
    time.sleep(5)
