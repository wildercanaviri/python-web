from SPARQLWrapper import SPARQLWrapper, JSON
import json

class Busqueda:
    pass
    def __init__(self, palabra, opcion):
        self.palabra=palabra.replace(" ","_")
        self.opcion=opcion
    
    def obtenerPalabra(self):

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery("""
            PREFIX res: <http://dbpedia.org/resource/>
        PREFIX dbpedia: <http://dbpedia.org/ontology/>
        Select ?descripcion where {

        res:"""+self.palabra+""" dbpedia:abstract ?descripcion.
        FILTER (langMatches(lang(?descripcion),'"""+self.opcion+"""'))
        }

        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()


        decripcion_cantante=""

        for result in results["results"]["bindings"]:
            decripcion_cantante=result["descripcion"]["value"]
        return decripcion_cantante   

    


