# ajcuesta.github.io

Web personal de Antonio J. Cuesta, construida con [Hugo](https://gohugo.io) y [Hugo Blox](https://hugoblox.com) y publicada en GitHub Pages (inglés en `/`, español en `/es/`).

## Cómo actualizar el contenido

| Quiero… | Dónde |
|---|---|
| Añadir una publicación | Añade la entrada a `bibliography/ajcuesta.bib`, ejecuta `python3 scripts/bib2hugo.py` y haz commit. Para destacarla en portada, añade su clave a `FEATURED_KEYS` en el script. |
| Cambiar mi bio, formación, experiencia o enlaces | `data/authors/me.yaml` (inglés) y `data/es/authors/me.yaml` (español) |
| Editar la portada | `content/en/_index.md` y `content/es/_index.md` |
| Añadir prensa o divulgación | Nueva carpeta en `content/en/blogs/<nombre>/index.md` (y su equivalente en `content/es/blogs/`) |
| Añadir una línea de investigación | Nueva carpeta en `content/en/projects/` y `content/es/projects/` |
| Cambiar el CV | Sustituye `static/CVA.pdf` y `static/CVA_es.pdf` (y `static/uploads/` si se usa desde ahí) |

## Vista previa en local

Requisitos: Hugo extended **0.161.1**, Go, Node 22 y pnpm.

```bash
pnpm install
hugo server
```

## Despliegue

Cada push a `main` ejecuta `.github/workflows/deploy.yml` (compila con Hugo, genera el índice de búsqueda con Pagefind y publica en GitHub Pages). En *Settings → Pages*, la fuente debe ser **GitHub Actions**.
