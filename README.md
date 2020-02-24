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

Download the JSON file with your OAuth 2.0 credentials from your GDeveloper console, and put its path in this file:

    CLIENT_SECRET_FILE = '<path to JSON credentials>'
    APPLICATION_NAME = 'XXX'

## conf.yaml

Fill the corresponding.

    folder: <folder_name>
    gdrive: <GDrive_URL_ID_here>

## Makefile

    all:
        python quickstart.py
        cd <folder_name> && pandoc -N --bibliography biblio.bib --biblatex article.md -o content.tex
        cd <folder_name> && pdflatex article && biber article && pdflatex article
        cd <folder_name> && evince article.pdf
