from wtforms import Form
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators



class UserForm(Form):
    nombre=StringField("nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="ingresa nombre vailido")
    ])
    apaterno=StringField("apaterno")
    amaterno=StringField("amaterno")
    edad=IntegerField("edad",[validators.number_range(min=1,max=20,message="Valor no valido")])
    correo=EmailField("correo",[validators.Email(message="Ingrese un correo valido")])

    #materias=SelectField(choices=[('Espaniol','esp'),('Matematicas','mate'),('Ingles','Ing')])
    
