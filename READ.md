documentazione utile
====================
https://kivymd.readthedocs.io/en/latest/
https://buildozer.readthedocs.io/en/latest/installation.html
https://www.evemilano.com/blog/python-venv/

preparazione dell'ambiente
==========================

ambiente virtuale Python
------------------------

creazione:
python3 -m venv .

attivazione:
source bin/activate

pacchetti:
pip install setuptools buildozer kivy kivymd cython certifi

buildozer
---------

inizializzare:
buildozer init

cose da modificare nel file spec:


compilare:
buildozer android debug
