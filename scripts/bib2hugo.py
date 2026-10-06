#!/usr/bin/env python3
"""Genera las páginas de publicaciones de Hugo Blox a partir de un archivo .bib.

Uso (desde la raíz del repositorio):
    python3 scripts/bib2hugo.py                       # usa bibliography/ajcuesta.bib
    python3 scripts/bib2hugo.py otro.bib

Crea content/<idioma>/publications/<clave>/{index.md,cite.bib} para cada entrada.
Para actualizar la web: añade la entrada nueva a bibliography/ajcuesta.bib,
ejecuta este script y haz commit. Es idempotente (regenera todo).

Ajustes habituales (más abajo): FEATURED_KEYS para destacar artículos,
MAX_AUTHORS para recortar las listas largas de grandes colaboraciones.
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "bibliography" / "ajcuesta.bib"
LANGS = {"en": "Publications", "es": "Publicaciones"}
ME_SURNAME = "cuesta"          # apellido que se enlaza con tu perfil (slug "me")
MAX_AUTHORS = 12               # por encima: primeros 3 + tú + "et al."
FEATURED_JOURNALS = {"Nature Astronomy"}   # se destacan siempre
# Artículos destacados (los de «Selected publications» de tu CV, además de Nature Astronomy)
FEATURED_KEYS = {"cuesta2022cosmology", "cuesta2016clustering", "cuesta2015calibrating", "cuesta2016neutrino"}
MONTHS = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}


def parse(text):
    entries = []
    for block in re.split(r"\n\s*\n(?=@)", text.strip()):
        m = re.match(r"@(\w+)\{([^,]+),", block)
        if not m:
            continue
        f = {k.lower(): re.sub(r"\s+", " ", v).strip()
             for k, v in re.findall(r"\n\s*(\w+)\s*=\s*\{(.*)\},?(?=\n)", block)}
        f["title"] = f["title"].strip("{}")
        entries.append({"type": m.group(1).lower(), "key": m.group(2), "f": f, "raw": block.strip() + "\n"})
    return entries


def person(a):
    last, _, first = a.partition(",")
    return f"{first.strip()} {last.strip()}".strip()


def authors_of(f):
    names = [a.strip() for a in f["author"].split(" and ")]
    me = next((i for i, a in enumerate(names) if ME_SURNAME in a.lower()), None)
    out = ["me" if i == me else person(a) for i, a in enumerate(names)]
    if len(out) > MAX_AUTHORS:
        head = out[:3]
        if me is not None and me >= 3:
            head.append("me")
        out = head + [f"et al. ({len(names)} authors)"]
    return out, len(names)


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def page(e, lang):
    f, key = e["f"], e["key"]
    authors, n = authors_of(f)
    month = MONTHS.get(f.get("month", "jan")[:3].lower(), 1)
    journal = f.get("journal", f.get("booktitle", ""))
    featured = journal in FEATURED_JOURNALS or key in FEATURED_KEYS
    ptype = "paper-conference" if e["type"] == "inproceedings" else "article-journal"
    fm = ["---", f"title: {q(f['title'])}", "authors:"]
    fm += [f"  - {q(a)}" if a != "me" else "  - me" for a in authors]
    fm += [f'date: "{f["year"]}-{month:02d}-01T00:00:00Z"',
           f"publication_types: [{q(ptype)}]",
           "publication:", f"  name: {q(journal)}"]
    if f.get("volume"):
        fm.append(f"  volume: {q(f['volume'])}")
    if f.get("number"):
        fm.append(f"  issue: {q(f['number'])}")
    if f.get("pages"):
        fm.append(f"  pages: {q(f['pages'])}")
    fm.append(f"featured: {'true' if featured else 'false'}")
    if f.get("doi"):
        fm += ["hugoblox:", "  ids:", f"    doi: {q(f['doi'])}"]
    links = []
    m = re.search(r"Erratum: (\S+?)\}?$", f.get("note", ""))
    if m:
        links.append(("erratum", m.group(1)))
    if links:
        fm.append("links:")
        for t, u in links:
            fm += [f"  - type: {t}", f"    url: {q(u)}"]
    fm.append("---")
    body = []
    if n > MAX_AUTHORS:
        if lang == "es":
            body.append(f"*Artículo de colaboración con {n} autores. La lista completa está en el archivo BibTeX (botón «Cite»).*")
        else:
            body.append(f"*Collaboration paper with {n} authors. The full author list is in the BibTeX file (\"Cite\" button).*")
    return "\n".join(fm) + "\n\n" + "\n".join(body) + "\n"


def main():
    entries = parse(BIB.read_text(encoding="utf-8"))
    for lang, title in LANGS.items():
        base = ROOT / "content" / lang / "publications"
        if base.exists():
            shutil.rmtree(base)
        base.mkdir(parents=True)
        (base / "_index.md").write_text(
            f"---\ntitle: {title}\ncms_exclude: true\nview: citation\n---\n", encoding="utf-8")
        for e in entries:
            d = base / e["key"]
            d.mkdir()
            (d / "index.md").write_text(page(e, lang), encoding="utf-8")
            (d / "cite.bib").write_text(e["raw"], encoding="utf-8")
    print(f"{len(entries)} publicaciones x {len(LANGS)} idiomas generadas")


if __name__ == "__main__":
    main()
