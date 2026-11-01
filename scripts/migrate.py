#!/usr/bin/env python3
"""Migra i post da Blogger (www.giancampo.com) e beehiiv (blog.giancampo.com)
in content/blog/<slug>/index.md (page bundle Hugo), scaricando le immagini nel bundle.
Genera anche redirects.csv (vecchio URL -> nuovo URL) per Cloudflare Bulk Redirects.

Uso: pip install requests beautifulsoup4 markdownify && python3 scripts/migrate.py
"""
import csv, hashlib, json, os, re, sys, urllib.parse
from datetime import datetime
import requests, warnings
from bs4 import XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "content", "blog")
NEW_BASE = "https://www.giancampo.com"
BLOGGER = "https://www.giancampo.com"
BEEHIIV = "https://blog.giancampo.com"
S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0 (migration script)"
redirects = []
seen_titles = {}
# Post Blogger che hanno un equivalente su beehiiv (versione beehiiv = originale)
BLOGGER_TO_BEEHIIV = {
    "/2024/11/attribution-masterclass-my-notes-pt-1.html": "attribution-masterclass-my-notes",
    "/2024/11/attribution-masterclass-my-notes-pt-2.html": "attribution-masterclass-my-notes",
    "/2024/11/attribution-masterclass-my-notes-pt-3.html": "attribution-masterclass-my-notes",
}


def slugify(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s.lower()).strip()
    s = re.sub(r"[\s_-]+", "-", s)
    if len(s) > 80:
        s = s[:80].rsplit("-", 1)[0]
    return s.strip("-")


def norm(t):
    return re.sub(r"\W+", "", t.lower())


def save_images(soup, bundle):
    for i, img in enumerate(soup.find_all("img")):
        src = img.get("src") or img.get("data-src")
        if not src:
            continue
        src = urllib.parse.urljoin(BLOGGER, src)
        # Blogger: prendi la versione a risoluzione originale
        src = re.sub(r"/s\d+(-[a-z0-9-]+)?/", "/s0/", src)
        src = re.sub(r"=(w|s|h)\d+[^/]*$", "=s0", src)
        try:
            r = S.get(src, timeout=60)
            r.raise_for_status()
        except Exception as e:
            print(f"  ! immagine non scaricata {src}: {e}")
            continue
        ext = {"image/png": ".png", "image/jpeg": ".jpg", "image/gif": ".gif",
               "image/webp": ".webp", "image/svg+xml": ".svg"}.get(
            r.headers.get("content-type", "").split(";")[0], ".jpg")
        name = f"img-{i+1:02d}-{hashlib.md5(src.encode()).hexdigest()[:6]}{ext}"
        with open(os.path.join(bundle, name), "wb") as f:
            f.write(r.content)
        img["src"] = name
        for a in ("srcset", "data-src", "width", "height", "style"):
            img.attrs.pop(a, None)
        # rimuovi il link che avvolge l'immagine (Blogger lo aggiunge sempre)
        if img.parent.name == "a" and img.parent.get("href", "").startswith("http") and \
                re.search(r"(blogger|googleusercontent|beehiiv|bp\.blogspot)", img.parent["href"]):
            img.parent.unwrap()


def write_post(source, title, date, html, tags, old_url, summary=""):
    key = norm(title)
    slug = slugify(title)
    if key in seen_titles:  # duplicato (stesso post su entrambe le piattaforme)
        print(f"  = duplicato, redirect verso esistente: {title}")
        redirects.append((old_url, seen_titles[key]))
        return
    bundle = os.path.join(OUT, slug)
    os.makedirs(bundle, exist_ok=True)
    soup = BeautifulSoup(html, "html.parser")
    for s in soup(["script", "style", "noscript", "iframe"]):
        if s.name == "iframe":
            s.replace_with(BeautifulSoup(f'<p><a href="{s.get("src","")}">{s.get("src","")}</a></p>', "html.parser"))
        else:
            s.decompose()
    # Blogger: le immagini con didascalia sono dentro <table class="tr-caption-container">
    for t in soup.select("table.tr-caption-container, table"):
        imgs = t.find_all("img")
        if not imgs:
            continue
        cap = t.select_one(".tr-caption")
        new = BeautifulSoup("", "html.parser")
        for im in imgs:
            pnode = new.new_tag("p"); pnode.append(im.extract()); new.append(pnode)
        if cap and cap.get_text(strip=True):
            if not imgs[0].get("alt"):
                imgs[0]["alt"] = cap.get_text(" ", strip=True)
            pnode = new.new_tag("p"); em = new.new_tag("em"); em.string = cap.get_text(" ", strip=True)
            pnode.append(em); new.append(pnode)
        t.replace_with(new)
    save_images(soup, bundle)
    body = md(str(soup), heading_style="ATX", bullets="*", code_language="")
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    fm = {"title": title, "date": date, "draft": False, "tags": tags,
          "source": source, "original_url": old_url}
    if summary and not summary.startswith("Exploring Digital Analytics"):
        fm["description"] = summary
    with open(os.path.join(bundle, "index.md"), "w") as f:
        f.write("---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()) + "\n---\n\n" + body)
    new_url = f"{NEW_BASE}/blog/{slug}/"
    seen_titles[key] = new_url
    redirects.append((old_url, new_url))
    print(f"  + {source}: {title} -> /blog/{slug}/")


def blogger():
    print("== Blogger")
    feed = S.get(f"{BLOGGER}/feeds/posts/default?alt=json&max-results=500", timeout=60).json()["feed"]
    for e in feed.get("entry", []):
        title = e["title"]["$t"]
        url = next(l["href"] for l in e["link"] if l["rel"] == "alternate")
        tags = [c["term"] for c in e.get("category", [])]
        path = urllib.parse.urlparse(url).path
        if path in BLOGGER_TO_BEEHIIV:
            redirects.append((url, f"{NEW_BASE}/blog/{BLOGGER_TO_BEEHIIV[path]}/"))
            print(f"  = coperto da beehiiv: {title}")
            continue
        html = (e.get("content") or {}).get("$t")
        if not html:  # feed impostato su "breve": prendo il corpo dalla pagina
            page = BeautifulSoup(S.get(url, timeout=60).text, "html.parser")
            body = page.select_one(".post-body") or page.select_one(".entry-content") or page.find("article")
            html = str(body) if body else e.get("summary", {}).get("$t", "")
        write_post("blogger", title, e["published"]["$t"], html, tags, url)
    print("== Blogger pagine statiche")
    try:
        pf = S.get(f"{BLOGGER}/feeds/pages/default?alt=json", timeout=60).json()["feed"]
        for e in pf.get("entry", []):
            url = next(l["href"] for l in e["link"] if l["rel"] == "alternate")
            slug = urllib.parse.urlparse(url).path.split("/")[-1].replace(".html", "") or slugify(e["title"]["$t"])
            page_dir = os.path.join(ROOT, "content", slug)
            os.makedirs(page_dir, exist_ok=True)
            html = (e.get("content") or {}).get("$t")
            if not html:
                pg = BeautifulSoup(S.get(url, timeout=60).text, "html.parser")
                b = pg.select_one(".post-body") or pg.find("article")
                html = str(b) if b else ""
            soup = BeautifulSoup(html, "html.parser")
            save_images(soup, page_dir)
            with open(os.path.join(page_dir, "index.md"), "w") as f:
                f.write(f'---\ntitle: {json.dumps(e["title"]["$t"])}\nmenu: main\n---\n\n' + md(str(soup), heading_style="ATX", bullets="*"))
            redirects.append((url, f"{NEW_BASE}/{slug}/"))
            print(f"  + pagina: {e['title']['$t']} -> /{slug}/")
    except Exception as ex:
        print(f"  ! pagine statiche: {ex}")


def beehiiv():
    print("== beehiiv")
    urls = set()
    try:
        sm = BeautifulSoup(S.get(f"{BEEHIIV}/sitemap.xml", timeout=60).text, "html.parser")
        urls = {l.text.strip() for l in sm.find_all("loc") if "/p/" in l.text}
    except Exception as ex:
        print(f"  ! sitemap: {ex}")
    if not urls:  # fallback: archivio
        for page in range(1, 10):
            soup = BeautifulSoup(S.get(f"{BEEHIIV}/archive?page={page}", timeout=60).text, "html.parser")
            found = {urllib.parse.urljoin(BEEHIIV, a["href"]).split("?")[0] for a in soup.find_all("a", href=True) if "/p/" in a["href"]}
            if not found - urls:
                break
            urls |= found
    for url in sorted(urls):
        soup = BeautifulSoup(S.get(url, timeout=60).text, "html.parser")
        title = (soup.find("meta", property="og:title") or {}).get("content") or soup.title.text
        date = None
        for s in soup.find_all("script", type="application/ld+json"):
            try:
                d = json.loads(s.string)
                d = d[0] if isinstance(d, list) else d
                date = d.get("datePublished") or date
            except Exception:
                pass
        date = date or (soup.find("time") or {}).get("datetime") or datetime.utcnow().isoformat()
        desc = (soup.find("meta", attrs={"name": "description"}) or {}).get("content", "")
        content = soup.select_one("#content-blocks") or soup.select_one("div.rendered-post") or soup.find("article")
        if not content:
            print(f"  ! contenuto non trovato: {url}")
            continue
        write_post("beehiiv", title.strip(), date, str(content), [], url, desc)


if __name__ == "__main__":
    beehiiv()   # beehiiv prima: in caso di duplicati vince la versione beehiiv
    blogger()
    with open(os.path.join(ROOT, "scripts", "redirects.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_url", "target_url", "status"])
        for old, new in redirects:
            w.writerow([old.replace("https://", ""), new, 301])
    print(f"\n{len(seen_titles)} post migrati, {len(redirects)} redirect in scripts/redirects.csv")
