# -*- coding: utf-8 -*-

import eyed3
import eyed3.mp3
import os
from os.path import isfile


#Ruta base en la que se encuentran las carpetas deseadas
base_path = r"D:/Musica"

#Carpetas en las que queremos que se ejecute el script
#folders = os.listdir(base_path) #Autotag every file in the base folder
folders = [u"Auxili", u"La Raiz"]

#Examinamos todos los archivos de todas las carpetas especificadas
for artist in folders:

	#Creamos los paths de cada artista y obtenemos los álbumes que hay en el mismo
	artist_path = base_path + os.sep + artist

	if ((artist == "*.*") or (artist == "*..*")):
		continue

	print "Artista: ", artist

	for album in os.listdir(artist_path):

		album_path = artist_path + os.sep + album
		if os.path.isdir(album_path) and ((album != "*.*") or (album != "*..*")):
			
			#Obtenemos las canciones de cada álbum
			for song in os.listdir(album_path):
				filename = album_path + os.sep + song

				#Si son canciones, editamos los metadatos
				if(eyed3.mp3.isMp3File(filename)):

					s = eyed3.load(filename)

					#IMPORTANTE: Necesitamos estar seguro de que la versión es como mínimo 2.3.
					#La versión 2.2 da problemas y no muestra el resultado en el Expl. de Windows
					s.tag.version = (2, 3, 0)
					
					#Editamos las etiquetas
					s.tag.title = unicode(song[:-4]) #El -4 es para eliminar el ".mp3" final
					s.tag.album = unicode(album)
					s.tag.artist = unicode(artist)
					s.tag.save()

		print "Terminado album: ", album
	print "Terminado artista: ", artist

print "Actualización de etiquetas finalizada. "



