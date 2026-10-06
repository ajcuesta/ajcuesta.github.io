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
        text: Curriculum
        url: uploads/CVA.pdf
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
      title: "About me"
      text: |-
        I was born in Granada, where I trained as a physicist specializing in Astrophysics and Cosmology. After completing a doctoral thesis on the properties of dark matter halos—using cosmological simulations run at supercomputing centers—I was hired in New Haven, Connecticut (USA) to study dark energy via the Sloan Digital Sky Survey's BOSS mapping project, employing Bayesian statistical techniques to analyze the large-scale structure of the Universe. Subsequently, I secured a position in Barcelona, where I continued my work on baryon acoustic oscillations while developing new skills, such as the cosmological determination of neutrino mass and the study of the Hubble Tension. Finally, I found my professional home at the University of Córdoba, where I successfully navigated several selection processes to obtain the tenured faculty position (Associate Professor) I hold today.

        I am currently working on a project that makes it possible to test for the viability of particles beyond the Standard Model through large-scale astronomical surveys (conducted by ground-based and space-based observatories) using cosmological data. 

        Some of my favorite physics-related quotes are:

        *"Suppose that physics, or rather nature, is considered analogous to a great chess game with millions of pieces in it, and we are trying to discover the laws by which the pieces move."* ― Richard Feynman, The Character of Physical Law.

        *"The important thing is not to stop questioning. [...] It is enough if one tries merely to comprehend a little of this mystery every day. Never lose a holy curiosity."*, and also *"The most incomprehensible thing about the universe is that it is comprehensible."* ― Albert Einstein.

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
      title: "Research lines"
      subtitle: "What I work on"
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
      title: "Featured publications"
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation
  - block: collection
    content:
      title: "Recent publications"
      text: "[All publications →](/publications/)"
      count: 8
      filters:
        folders:
          - publications
    design:
      view: citation
  - block: markdown
    id: teaching
    content:
      title: "Teaching"
      subtitle: "Here are a few topics I've been teaching recently:"
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
      title: "Press & outreach"
      text: "[All press and outreach →](/blogs/)"
      count: 5
      filters:
        folders:
          - blogs
    design:
      view: date-title-summary
  - block: markdown
    id: contact
    content:
      title: "Contact"
      text: |-
        Do you have any questions or suggestions? Don't hesitate to write to me! I am always open to new ideas and collaborations.

        [**Send me an email**](mailto:ajcuesta@uco.es){.btn}
    design:
      columns: '1'
---
