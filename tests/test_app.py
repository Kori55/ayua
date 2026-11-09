
from app import app, saludar


def test_saludar():
    assert saludar("Sebastian") == "Hola, Sebastian!"


def test_saludar_invitado():
    assert saludar("Invitado") == "Hola, Invitado!"


def test_pagina_inicio():
    client = app.test_client()
    respuesta = client.get("/")

    assert respuesta.status_code == 200
    assert b"Bienvenido" in respuesta.data


def test_endpoint_saludar():
    client = app.test_client()
    respuesta = client.get("/saludar?nombre=Sebastian")

    assert respuesta.status_code == 200
    assert respuesta.json["mensaje"] == "Hola, Sebastian!"
