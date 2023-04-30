from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://usuario:contraseña@servidor:puerto/nombre_base_de_datos')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Palabra(Base):
    __tablename__ = 'palabras'
    id = Column(Integer, primary_key=True)
    palabra = Column(String(50), nullable=False)
    significado = Column(String(200), nullable=False)

def agregar_palabra():
    palabra = input("Ingresa la palabra: ")
    significado = input("Ingresa el significado: ")
    nueva_palabra = Palabra(palabra=palabra, significado=significado)
    sesion.add(nueva_palabra)
    sesion.commit()

def editar_palabra():
    palabra = input("Ingresa la palabra que deseas editar: ")
    nueva_palabra = input("Ingresa la nueva palabra: ")
    nuevo_significado = input("Ingresa el nuevo significado: ")
    palabra_editar = sesion.query(Palabra).filter_by(palabra=palabra).first()
    palabra_editar.palabra = nueva_palabra
    palabra_editar.significado = nuevo_significado
    sesion.commit()

def eliminar_palabra():
    palabra = input("Ingresa la palabra que deseas eliminar: ")
    palabra_eliminar = sesion.query(Palabra).filter_by(palabra=palabra).first()
    sesion.delete(palabra_eliminar)
    sesion.commit()

def ver_palabras():
    palabras = sesion.query(Palabra).all()
    for palabra in palabras:
        print(f"{palabra.palabra}: {palabra.significado}")

def buscar_palabra():
    palabra = input("Ingresa la palabra que deseas buscar: ")
    palabra_buscar = sesion.query(Palabra).filter_by(palabra=palabra).first()
    if palabra_buscar:
        print(palabra_buscar.significado)
    else:
        print("La palabra no fue encontrada en el diccionario.")

def menu():
    while True:
        print("Seleccione una opción:")
        print("a) Agregar nueva palabra")
        print("b) Editar palabra exist
