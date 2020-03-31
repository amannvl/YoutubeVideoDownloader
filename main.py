from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0

def progress(stream=None, chunk=None, file_handle=None,remaining=None):
    file_downloaded = (file_size-remaining)
    per = (file_downloaded/file_size)*100
    dBtn.config(text='{:00.0f} % downloaded'.format(per))

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)
        dBtn.config(text='Please Wait')
        dBtn.config(state=DISABLED)
        yt = YouTube(url, on_progress_callback=progress)
        print(yt.title)
        stream = yt.streams.first()
        file_size = stream.filesize
        print(file_size)
        stream.download()
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded successfully")
        urlField.delete(0, END)
    except Exception as e:
        print("error")

def startDownloadThread():
    thread = Thread(target = startDownload)
    thread.start()

#GUI from here
main = Tk()

main.title("My Youtube Downloader")

#main.iconbitmap('icon.xbm')

main.geometry("500x600")


file = PhotoImage(file='1.png')
headingIcon = Label(main , image = file)
headingIcon.pack(side=TOP)

urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill = X, padx = 10)


dBtn = Button(main, text="Start Download", font=("verdana", 18), relief='ridge', command=startDownloadThread)
dBtn.pack(side=TOP, pady=10)

main.mainloop()

