# pipx install kivy kivymd

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import certifi
import json

class GlisWebApp(MDApp):

    def test_function(self):
        self.root.ids["mdlab"].text = 'Button clicked!'
        self.root.ids["mdbtn"].text = 'Clicked!'

    def askconfig(self):
        url = 'https://configserver.istricesrl.com?u=test'
        self.root.ids['mdlab'].text = 'caricamento in corso...'
        self.configrequest = UrlRequest(url, on_success=self.getconfig, on_failure=self.reqfailure, on_error=self.reqerror, ca_file=certifi.where())

    def getconfig(self, req, result):
        # converto result da json a dict
        result = json.loads(result)
        self.root.ids['mdlab'].text = result['status']

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
