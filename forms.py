from wtforms import Form
from wtforms import StringField,TextAreaField,TextField,SelectField,RadioField
from wtforms import EmailField

class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("correo")
    apellidoPaterno=TextField("apeterno")
    materias=SelectField(choices=[('Espaniol','esp'),('Matematicas','mate'),('Ingles','Ing')])
    radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])