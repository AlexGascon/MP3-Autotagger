# MP3-Autotagger

# Introduction
MP3-Autotagger is a Python program that automatically sets the main tags (title, album, artist) of every MP3 file in a specified folder.

In order to do so, the scanned folder must follow a specifical structure: it must have a folder for every artist, and inside them, a folder for every album. Inside those albums folders is where the MP3 files should be. MP3-Autotagger will use this folders' names as the values for "Artist" and "Album" tags, and the MP3 filename as the value for the title tag. 

![Folder structure example](http://i.imgur.com/ZKFwsqB.png)

# How to use
1. **Install eyeD3 library:** it's used for MP3 tag editing, so its absolutely necessary in our program. 
2. **Change the base path:** We have to change the *base_path* variable to the location of the folder in which are contained all the artists one.
3. **Select the artists we want to autotag**: Select the folders contained in the base path that we want to auto-tag by adding their names to the *folders* array. If we want to autotag every file in the base folder, simply set *folders* to *os.listdir(base_path)*
4. **Execute the script**: execute the script and wait for it to finish


#### Fture improvements
- Currently, UNICODE is not supported. If any folder or file has a non-ascii character, the execution will break.
- Autotag non-MP3 audio files. This will be implemented in a near future, but isn't currently available as the program considers that every non-mp3 file isn't a music one.
- Executable/command line program. Actually, MP3-Autotagger only works by downloading and executing the source code. In a near future, there will be an easier way to execute it.

