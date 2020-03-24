import os
import watchdog
import watchdog.events
import watchdog.observers

# set the user's download dir as current working dir
home_dir = os.path.expanduser("~")
download_dir = os.path.join(home_dir, 'Downloads')
os.chdir(download_dir)
print(os.getcwd())

#setup and start the observer
event_hndlr = watchdog.events.LoggingEventHandler()
observer = watchdog.observers.Observer()
observer.schedule(event_hndlr, download_dir, recursive=False)
observer.start()

#listen for new file

