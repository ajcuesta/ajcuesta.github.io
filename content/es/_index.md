---
title: ''
summary: ''
date: 2026-10-05
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: Currículum
        url: uploads/CVA_es.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: large
        shape: circle
  - block: markdown
    id: about
    content:
      title: "Sobre mí"
      text: |-
        Nací en Granada, donde me formé como físico especializado en Astrofísica y Cosmología. Tras completar una tesis doctoral sobre propiedades de los halos de materia oscura usando simulaciones cosmológicas realizadas en centros de supercomputación, fui contratado en New Haven, Connecticut (Estados Unidos) para el estudio de la energía oscura mediante el cartografiado BOSS del Sloan Digital Sky Survey usando técnicas de estadística bayesiana sobre la estructura a Gran Escala del Universo. Posteriormente conseguí un contrato en Barcelona, donde pude continuar mi trabajo en oscilaciones acústicas de bariones, a la vez que desarrollé nuevas habilidades como la determinación cosmológica de la masa de los neutrinos o el estudio de la Tensión de Hubble. Finalmente, encontré mi destino en la Universidad de Córdoba, donde superé varios procesos selectivos hasta alcanzar la plaza de funcionario público (Profesor Titular de Universidad) que ahora ocupo.

        Actualmente estoy trabajando en un proyecto que permite evaluar la existencia de partículas más allá del Modelo Estándar mediante grandes cartografiados astronómicos (realizados por observatorios terrestres y desde el espacio) usando datos cosmológicos.

        Algunas de mis frases favoritas relacionadas con la Física son:

        *"Suppose that physics, or rather nature, is considered analogous to a great chess game with millions of pieces in it, and we are trying to discover the laws by which the pieces move."* ― Richard Feynman, The Character of Physical Law.

        *"The important thing is not to stop questioning. [...] It is enough if one tries merely to comprehend a little of this mystery every day. Never lose a holy curiosity."*, y también *"The most incomprehensible thing about the universe is that it is comprehensible."* ― Albert Einstein.

        *"Remember to look up at the stars and not down at your feet. [...] It matters that you don't just give up. While there's life, there is hope."* ― Stephen W. Hawking.

        *"Whatever the final laws of nature may be, there is no reason to suppose that they are designed to make physicists happy."* ― Steven Weinberg.

        *"An expert is a person who has made all the mistakes that can be made in a very narrow field."* ― Niels Bohr.

        *"Mathematics began to seem too much like puzzle solving. Physics is puzzle solving, too, but of puzzles created by nature, not by the mind of man."* ― Maria Goeppert-Mayer

        *"The cosmos is within us. We are made of star-stuff. We are a way for the universe to know itself."* ― Carl Sagan.
    design:
      columns: '1'
  - block: collection
    id: research
    content:
      title: "Líneas de investigación"
      subtitle: "En qué trabajo"
      filters:
        folders:
          - projects
    design:
      view: article-grid
      fill_image: false
      columns: 3
      show_date: false
      show_read_time: false
      show_read_more: true
  - block: collection
    id: papers
    content:
      title: "Publicaciones destacadas"
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation
  - block: collection
    content:
      title: "Publicaciones recientes"
      text: "[Todas las publicaciones →](/es/publications/)"
      count: 8
      filters:
        folders:
          - publications
    design:
      view: citation
  - block: markdown
    id: teaching
    content:
      title: "Docencia"
      subtitle: "Asignaturas que he impartido recientemente:"
      text: |-
        - [Astrofísica y Cosmología 🇪🇸](https://www.uco.es/eguiado/guias/2026-27/100513es_2026-27.pdf)
        - [Física Nuclear y de Partículas 🇪🇸/🇬🇧🇺🇸](https://www.uco.es/eguiado/guias/2026-27/100512es_2026-27.pdf)
        - [Machine Learning aplicado a la Física 🇪🇸](https://www.uco.es/eguiado/guias/2026-27/646012es_2026-27.pdf)
        - [Física Atómica y Molecular 🇬🇧🇺🇸](https://www.uco.es/eguiado/guias/2025-26/100515en_2025-26.pdf)
    design:
      columns: '1'
  - block: collection
    id: press
    content:
      title: "Prensa y divulgación"
      text: "[Toda la prensa y divulgación →](/es/blogs/)"
      count: 5
      filters:
        folders:
          - blogs
    design:
      view: date-title-summary
  - block: markdown
    id: contact
    content:
      title: "Contacto"
      text: |-
        ¿Tienes alguna pregunta o sugerencia? ¡No dudes en escribirme! Siempre estoy abierto a nuevas ideas y colaboraciones.

        [**Escríbeme**](mailto:ajcuesta@uco.es){.btn}
    design:
      columns: '1'
---
