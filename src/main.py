#
# pacchetti da installare
# sudo apt-get install xclip libffi-dev autoconf libtool autopoint
#
# in ambiente virtuale:
# pipx install kivy kivymd
#
# in ambiente non virtuale:
# pip install setuptools buildozer kivy kivymd cython certifi
#
# per inizializzare
# buildozer init
#
# selezionare il JDK corretto:
# update-java-alternatives -l
#
# per compilare:
# buildozer -v android debug
# 

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import certifi
import json
import logging

# formato del log
logformat = '%(asctime)s [%(levelname)s] %(filename)s: %(message)s'

# configurazione del logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='app.log', encoding='utf-8', format=logformat, level=logging.DEBUG)

class GlisWebApp(MDApp):

    def test_function(self):
        self.root.ids["mdlab"].text = 'Button clicked!'
        self.root.ids["mdbtn"].text = 'Clicked!'

    def askconfig(self):
        url = 'https://configserver.istricesrl.com?u=test'
        self.root.ids['mdlab'].text = 'caricamento in corso...'
        self.configrequest = UrlRequest(url, on_success=self.getconfig, on_failure=self.reqfailure, on_error=self.reqerror, ca_file=certifi.where())

    def getconfig(self, req, result):
        logger.info(f'risposta ricevuta: {result}')
        result = json.loads(result)
        self.root.ids['mdlab'].text = result['status']
        if 'error' in result:
            for errore in result['error']:
                self.root.ids['mdlab'].text += '\n' + errore

    def reqfailure(self, req, result):
        self.root.ids['mdlab'].text = 'richiesta fallita'

    def reqerror(self, req, error):
        self.root.ids['mdlab'].text = 'errore: ' + str(error)

    def build(self):

        self.title = 'GlisWeb app'
        self.theme_cls.primary_palette = 'Gray'
        self.theme_cls.primary_hue = '900'

        return Builder.load_file('main.kv')

GlisWebApp().run()
