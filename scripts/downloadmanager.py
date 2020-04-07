import time
import os
import logging
import sys
from watchdog.events import LoggingEventHandler
from watchdog.events import FileCreatedEvent
from watchdog.observers import Observer

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = os.path.expanduser(r'~\Downloads')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except(KeyboardInterrupt):
        observer.stop()
    observer.join()