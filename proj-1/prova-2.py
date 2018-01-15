import random
import string

import cherrypy
from cherrypy.lib import sessions
from jinja2 import Environment, FileSystemLoader
env1 = Environment(loader=FileSystemLoader('templates'))
class numberGenerator(object):
    @cherrypy.expose
    def index(self):
        tmpl = env1.get_template('template.html')
        return tmpl.render()

    @cherrypy.expose
    def generate(self, respuesta):
        cherrypy.session['sad']
        numeroRandom = random.randint(1,100)
        res= int(respuesta)
        print (numeroRandom, respuesta)
        if numeroRandom == res:
            return """<h1>has acertado!</h1>"""
        else:
            tmpl = env1.get_template('template.html')
            if numeroRandom < res:
                tmpl = env1.get_template('template.html')
                return tmpl.render(), """<h1>Has fallado! Prueba un numero mas bajo!</h1>"""
            else:
                return tmpl.render(), """<h1>Has fallado! Prueba un numero mas alto!</h1>"""



if __name__ == '__main__':
    cherrypy.quickstart(numberGenerator())