from flask import Flask

@app.route("/")
def pagina_inicial():
    return "DevOps LAB"

if __name__ == '__main__':
    app.run()
  
