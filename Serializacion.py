# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:43:26 2022

@author: Bryan De Anda
"""

import pickle

class Peliculas:
    def __init__(self, nombre, genero, director, protagonista):
        self.nombre = nombre
        self.genero = genero
        self.director = director
        self.protagonista = protagonista
        print("\nSe a agregado una pelicula nueva con el nombre de: ", self.nombre, "\n")
        
    def __str__(self):
        return "{} {} {} {}".format(self.nombre, self.genero, self.director, self.protagonista)
    
    
class ListaPeliculas:
    
    peliculas = []
    
    def __init__(self):
        listaDePeliculas = open("ficheroExterno", "ab+")
        listaDePeliculas.seek(0)
        
        try:
            self.peliculas=pickle.load(listaDePeliculas)
        except:
            print("El fichero esta vacio")
        finally:
            listaDePeliculas.close()
            del(listaDePeliculas)
    
    def AgregarPeliculas(self, p):
        self.peliculas.append(p)
        self.GuardarPeliculasExterno()
        
    def MostrarPeliculas(self):
        for p in self.peliculas:
            print(p)
        
    def GuardarPeliculasExterno(self):
        listaDePeliculas = open("FicheroExterno", "wb")
        pickle.dump(self.peliculas, listaDePeliculas)
        del(listaDePeliculas)
    
    def MostrarInfoFicheroExterno(self):
        print("\nLa información de las peliculas almacenadas es: \n")
        for p in self.peliculas:
            print("Nombre: ", p.nombre)
            print("Genero: ", p.genero)
            print("Director: ", p.director)
            print("Protagonista: ", p.protagonista, "\n")
    
    def BuscarPeliculaEnElFichero(self, nom):
        for p in self.peliculas:
            if p.nombre == nom:
                print("\nPelicula encontrada: ")
                print("Nombre: ", p.nombre)
                print("Genero: ", p.genero)
                print("Director: ", p.director)
                print("Protagonista: ", p.protagonista, "\n")
                break
            
            
miLista = ListaPeliculas()      
while True:
    try:
        print("----Menú de almacen de peliculas----")
        print("1) Ingresar una nueva pelicula")
        print("2) Mostrar todas las peliculas")
        print("3) Buscar una pelicula por su nombre")
        print("0) Salir")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            nomb = input("Ingresa el nombre de la pelicula: ")
            gen = input("Ingesa el genero de la pelicula: ")
            dire = input("Ingesa el director de la pelicula: ")
            prota = input("Ingesa el protagonista de la pelicula: ")
            peli = Peliculas(nomb, gen, dire, prota)
            miLista.AgregarPeliculas(peli)
        elif op == 2:
            miLista.MostrarInfoFicheroExterno()
        elif op == 3:
            nomb = input("Ingresa el nombre de la pelicula a buscar: ")
            miLista.BuscarPeliculaEnElFichero(nomb)
        elif op == 0:
            break
    except:
        print("\nLa opción no se encuentra en el menu\n")
    