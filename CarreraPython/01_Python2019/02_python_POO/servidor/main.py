from flask import Flask 

app = Flask(__name__)



@app.route('/')
def hellow_world():
    return 'Hola, mundo lanzando servidor web con Flask'



if __name__ == '__main__':
    app.run()


