# PDF Generate with LaTeX and Python

The following code was made to generate a PDF document using LaTeX with Python. To compile this script you should have installed textlive-core.

You can visualize the generated document in **doc/full.pdf**, also if you want to see the Tex generated document see **doc/full.tex**

**The visual document can be changed due to lorem library**

## Structure

```
.
├── doc/
│   ├── full.pdf
│   └── full.tex
├── .gitignore
├── main.py
├── README.md
├── requirements.txt

```

## Runing Project

### Installing Dependecies

* pip install -r requirements.txt
* pacman -Sy textlive-core (Arch/Manjaro)

### Running Project

* python main.py