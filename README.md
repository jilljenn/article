# GDrive Markdown → PDF

## Tree

    .
    ├── quickstart.py
    ├── secret.py
    ├── conf.yaml
    ├── <folder_name>
    │   ├── biblio.bib (optional)
    │   ├── article.tex (optional; should include \input{content})
    │   ├── article.md (retrieved from GDrive)
    │   ├── content.tex (generated from pandoc)

## secret.py

    CLIENT_SECRET_FILE = 'From your GDeveloper Console'
    APPLICATION_NAME = 'XXX'

## conf.yaml

    folder: <folder_name>
    gdrive: <GDrive_ID_here>

## Makefile

    all:
        python quickstart.py
        cd <folder_name> && pandoc -N --bibliography biblio.bib --biblatex article.md -o content.tex
        cd <folder_name> && pdflatex article && biber article && pdflatex article
        cd <folder_name> && open -a "Preview" article.pdf  # If MacBook
