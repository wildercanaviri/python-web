from Informacion import Busqueda
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inicio', methods=['GET','POST'])
def home():
   
    if request.method == 'POST':
        palabra=request.form['palabra']
        opcion=request.form['opcion'] 
        aux=Busqueda(palabra,opcion)
        resultado=aux.obtenerPalabra()
        return render_template('home.html',contenido=resultado)
    else:
        return render_template('home.html',contenido="")
if __name__ == '__main__':
    app.run(debug=True)
