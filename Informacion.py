from SPARQLWrapper import SPARQLWrapper, JSON
import json

class Busqueda:

    def __init__(self, palabra, opcion):
        self.palabra=palabra.replace(" ","_")
        self.opcion=opcion
    
    def obtenerInformacion(self):

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery("""
        
        PREFIX res: <http://dbpedia.org/resource/>
        PREFIX dbpedia: <http://dbpedia.org/ontology/>
        Select ?descripcion ?imagen where {

        res:"""+self.palabra+""" dbpedia:abstract ?descripcion.
        res:"""+self.palabra+""" dbpedia:thumbnail ?imagen.
        
        FILTER (langMatches(lang(?descripcion),'"""+self.opcion+"""'))
        }

        """)

      
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()


        descripcion_cantante=""
        direccion_imagen=""
        for result in results["results"]["bindings"]:
            descripcion_cantante=result["descripcion"]["value"]
            direccion_imagen=result["imagen"]["value"]

            

        if(not descripcion_cantante) :
                descripcion_cantante = "El cantante no tiene biografía, en el idioma seleccionado"
        
        arreglo=[descripcion_cantante,direccion_imagen]

        return arreglo

    


