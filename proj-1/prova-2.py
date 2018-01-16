import random
import string

import cherrypy

from jinja2 import Environment, FileSystemLoader
env1 = Environment(loader=FileSystemLoader('templates'))
tmpl = env1.get_template('template.html')
numeroRandom = random.randint(1,100)
class numberGenerator(object):
    @cherrypy.expose
    def index(self):
        return tmpl.render()

    @cherrypy.expose
    def generate(self, respuesta):
        res= int(respuesta)
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