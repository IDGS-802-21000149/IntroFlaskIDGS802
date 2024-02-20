from flask import Flask,request,render_template,Response
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms 
from flask import g

app=Flask(__name__)
app.secret_key='esta es la clave secreta'

@app.route("/")
def index():
 return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
 return render_template("404.html"),404


@app.before_request
def before_request():
 g.prueba="Hola"
 print("antes de ruta")
 
@app.after_request
def after_request(response):
 print("antes de ruta")
 return response


@app.route('/idiomas', methods=['GET', 'POST'])
def idiomas():
    guardar_form = forms.GuardarIdiomaForm(request.form)
    consultar_form = forms.ConsultarIdiomaForm(request.form)
    texto_resultado = None

    if request.method == 'POST':
        if 'btn_guardar' in request.form and guardar_form.validate():
            # Guardar la palabra en el archivo de texto con el formato adecuado
            with open('diccionario.txt', 'a') as file:
                file.write(f"{guardar_form.espaniol.data}:{guardar_form.ingles.data}\n")
        elif 'btn_consultar' in request.form and consultar_form.validate():
            palabra_buscar = consultar_form.palabra.data
            idioma = consultar_form.idioma.data
            # Realizar la búsqueda en el archivo de texto
            with open('diccionario.txt', 'r') as file:
                for line in file:
                    palabra, traduccion = line.strip().split(':')
                    if idioma == "Ingles" and palabra == palabra_buscar:
                        texto_resultado = traduccion
                        break
                    elif idioma == "Espanol" and traduccion == palabra_buscar:
                        texto_resultado = palabra
                        break
                else: 
                    texto_resultado="Palabra no encontrada"

    return render_template('idiomas.html', guardar_form=guardar_form, consultar_form=consultar_form, texto_resultado=texto_resultado)



@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
   print("Dentro de alumnos")
   valor = g.prueba
   print(f"El dato es {valor} ")
   nom=""
   apa =""
   ama=""
   correo=""
   edad=""
   alumnos_form=forms.UserForm(request.form)
   if request.method == "POST" and alumnos_form.validate():
      apa = alumnos_form.apaterno.data
      ama = alumnos_form.amaterno.data
      correo = alumnos_form.correo.data
      mensaje="Bienvenido:{}".format(nom)
      flash(mensaje)
      print("nombre: {}".format(nom))
      print("apaterno: {}".format(apa))
      print("amaterno: {}".format(ama))
      print("correo: {}".format(correo))
      print("correo: {}".format(edad))

   return render_template("alumnos.html",form=alumnos_form,nom=nom,ama=ama,apa=apa,correo=correo,edad=edad)

@app.route("/maestros")
def maestros():
     return render_template("maestros.html")


@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1>Hola</h1>"+nom


@app.route("/numero/<int:n1>")
def numero(n1):
    return "<h1>El valor es {}</h1>".format(n1)

@app.route("/user/<string:nom>/<int:id>")
def user(nom,id):
    return "ID: {} NOMBRE: {}".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "<h1>La suma de:  {} mas: {} es = {}</h1>".format(n1,n2,n1+n2)

@app.route("/multiplica",methods=["GET","POST"])
def mult():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

        return "<h1>El resultado es: {}</h1>".format(str(int(num1)*int(num2)))
    
    else: 
        return '''
            <form action="/multiplica" method = "POST">
             <label>N1:</label>
             <input type="text" name="n1"/>
              <label>N2:</label>
             <input type="text" name="n2"/>
             <input type="submit"/>
            </form>
            '''
            
@app.route("/formulario1")
def calculo(): 
    return render_template("formulario1.html")         

@app.route("/resultado",methods=["GET","POST"])
def mult1():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

        return "<h1>El resultado es: {}</h1>".format(str(int(num1)*int(num2)))


if __name__ == "__main__":
    app.run(debug=True)
