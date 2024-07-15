import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "Downloads"
to_dir = "C:/Users/Gustavo/Desktop/Aulas programação(Jogos)/C-113 Aula"

dir_tree = {
"Image_Files":['.jpg','.jpeg','.png','.gif','.jfif'],
"Video_Files":['.mp4','.mpv','.avi','.mov'],
"Document_Files":['.pdf','.txt','.csv'],
"Setup_Files":['.exe', '.cmd']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path)
event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive = True)

observer.start()

while True:
    time.sleep(120)
    print("executando")




