
from flask import Flask, request, jsonify

app = Flask(__name__)


def saludar(nombre):
    """
    @brief Genera un saludo personalizado.

    Esta función recibe el nombre de un usuario
    y devuelve un mensaje de bienvenida.

    @param nombre Nombre del usuario.
    @return Mensaje de saludo personalizado.
    """
    return f"Hola, {nombre}!"


@app.route("/")
def inicio():
    """
    @brief Página principal de la aplicación.

    @return Mensaje de bienvenida.
    """
    return "Bienvenido a la aplicación de documentación Flask."


@app.route("/saludar")
def saludo():
    """
    @brief Endpoint para saludar a un usuario.

    Recibe el nombre mediante un parámetro GET.

    @return Respuesta JSON con el saludo.
    """
    nombre = request.args.get("nombre", "Invitado")
    return jsonify({"mensaje": saludar(nombre)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
