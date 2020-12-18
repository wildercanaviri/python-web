from Informacion import Busqueda
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inicio', methods=['GET','POST'])
def home():
   
    if request.method == 'POST':
        palabra=request.form['palabra']
        opcion=request.form['opcion'] 
        aux=Busqueda(palabra,opcion)
        resultado=aux.obtenerInformacion()
        return render_template('home.html',contenido=resultado[0],texto=palabra,opcion_marcada=opcion, imagen=resultado[1])
    else:
        return render_template('home.html',contenido="",texto="", opcion_marcada="es",imagen="https://icon-library.com/images/default-profile-icon/default-profile-icon-17.jpg")
if __name__ == '__main__':
    app.run(debug=True)
