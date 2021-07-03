import io
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import B, Window
from pytube import YouTube
import urllib.request
from PIL import Image
import pytube
sg.theme("Topanga")

layout = [
    [sg.Text("Link:"),sg.Input(key='-LINK-')],
    [sg.Submit("Get Video"),sg.Cancel(key='CANCEL')],
    [sg.Text(key='-TITLE-',size=(30,1))],
    [sg.Image(key='-IMAGE-')],[sg.Button("Download")]
]

window = sg.Window("Yt downloader",layout)

while True:
    events,values = window.read()

    if events==sg.WIN_CLOSED or events=="CANCEL":
        break
    sg.Popup("Dev forgot the progress bar, so sit back and hang on!!")

    link = values['-LINK-']
    print(link)

    yt = YouTube(link)
    title = yt.title
    description = yt.description
    image_url = yt.thumbnail_url
    urllib.request.urlretrieve(image_url,"image.jpg")
    img = Image.open("image.jpg")
    x = yt.streams
    print(title)
    video = yt.streams.first()
    print(video)


    if events=="Get Video":
        img.thumbnail((400,400))
        bio = io.BytesIO()
        img.save(bio,format="PNG")
        window["-IMAGE-"].update(data =bio.getvalue())
        window['-TITLE-'].update(title)

    if events == "Download":
        video.download()

window.close()
