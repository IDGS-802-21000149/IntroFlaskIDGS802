from flask import Flask,request,render_template
import forms 

app=Flask(__name__)

@app.route("/")
def index():
 return render_template("index.html")

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
   nom=""
   alumnos_form=forms.UserForm(request.form)
   if request.method == "POST":
      nom = alumnos_form.nombre.data
      apellidoPaterno = alumnos_form.apellidoPaterno.data
      correo = alumnos_form.email.data
      print("nombre: {}".format(nom))
      print("apellidoPaterno: {}".format(apellidoPaterno))
      print("correo: {}".format(correo))
   return render_template("alumnos.html",form=alumnos_form,nom=nom)

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
