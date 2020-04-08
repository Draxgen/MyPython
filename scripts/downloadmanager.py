import time
import os
import logging
import sys
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os.path

class FileOrganizerEventHandler(FileSystemEventHandler):
    
    # folders and their extensions
    _folderAndExt = {
        "Coding" : ['.vi','.py','.c','.cpp','.java'],
        "Images" : ['.jpg','.jpeg','.bmp','.gif','.png'],
        "Documents" : ['.doc','.docx','.txt','.ppt','.xlsx'],
        "Installers" : ['.exe','.msi'],
        "Audio" : ['.mp3','.flac','.wav'],
        "Video" : ['.mp4'],
        "Torrents" : ['.torrent']
    }

    def on_created(self, event):
        # ignore new folders
        if event.is_directory:
            return
        
        # recognize the file
        breakLoop = False
        file_name = os.path.basename(event.src_path)
        folder_path = os.path.dirname(event.src_path)
        file_ext = os.path.splitext(file_name)[1]
        for key in self._folderAndExt:
            for x in self._folderAndExt[key]:
                if x == file_ext:
                    # create a new folder if it doesn't exist
                    if not os.path.exists(os.path.join(folder_path, key)):
                        os.makedirs(os.path.join(folder_path, key))
                    # move the file to correct folder
                    timeout = time.time() + 10 # wait 10s max for access to file 
                    while True:
                        try:
                            os.rename(event.src_path, os.path.join(folder_path, key, file_name))
                            break
                        except:
                            time.sleep(1)
                        if time.time() > timeout:
                            break
                    # set breakLoop variable to break the outer for loop
                    breakLoop = True
                    break
            if breakLoop: break

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # get Downloads folder path
    downloadFolder = os.path.expanduser(r'~\Downloads')

    # listen for new file events
    event_handler = FileOrganizerEventHandler()
    
    # start Observer
    observer = Observer()
    observer.schedule(event_handler, downloadFolder)
    observer.start()
    

    # start endless loop (interuppted by ctrl-C)
    try:
        while True:
            time.sleep(1)
    except(KeyboardInterrupt):
        observer.stop()
    observer.join()