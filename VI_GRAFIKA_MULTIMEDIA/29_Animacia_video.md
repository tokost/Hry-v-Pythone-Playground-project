>## Animácia

Animácia je vlastne meniaci sa obrázok čo do tvaru, pozície, obsahu a farby.Je to vlastne ilúzia pohybu a zmeny statického objektu. 

Ako jednoduchú formu animácie môžeme považovať aj ovládanie a vykreslenie grafov. Používa sa tu knižnica matplotlib ktorá ponúka špecialny nástroj MATLAB. Knižnica Numpy je použitá na znázornenie grafických hodnôt osí:
* plt.bar() sa používa na vyjadrenie, že stĺpcový graf sa má vykresliť pomocou hodnôt osi X a osi Y.
* ptl.xlabel() sa používa na znázornenie osi x.
* plt.ylabel() sa používa na znázornenie osi y.
* plt.title() sa používa na označenie názvu stĺpcového grafu.

Vo vytvorenom gife môžeme vidieť že keď podržíme kurzor myši na osi x, osi y, stĺpci apod., tak na lište vidíme hodnoty pozície. Animácia sa však najviac prejaví pri použití ovládacích prvkov ktoré sú tiež umiestnené na spodnej lište.
~~~
from matplotlib import pyplot as plt

plt.bar([0.25,1.25,2.25,3.25,4.25],[50000,40000,70000,80000,200000],label="MAC",color='r',width=.4)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80000,20000,20000,50000,60000],label="Dominos",color='b',width=.4)

plt.legend(loc='upper right')
plt.xlabel('Months')
plt.ylabel('Sales Amount')
plt.title('Information')
plt.show()
~~~

Nasledovný príklad animácie predpokladá inštálaciu knižnice [celluloid](https://pypi.org/project/celluloid/) a priblížime si ju tiež formou príkladu :
~~~
from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np

# create figure object
fig = plt.figure()
# load axis box
ax = plt.axes()
# set axis limit
ax.set_ylim(0, 1)
ax.set_xlim(0, 10)

camera = Camera(fig)
for i in range(10):
    ax.scatter(i, np.random.random())
    plt.pause(0.1)
    camera.snap()

animation = camera.animate()
animation.save('animation.gif', writer='PillowWriter', fps=2)
~~~
Jej výstupom je spustatelný súbor animation.gif .

**Animáciu s použitím Tkinter** si ukážeme tiež na príklade:

~~~
import tkinter
import time
 

Window_Width=800

Window_Height=600

Ball_Start_XPosition = 50

Ball_Start_YPosition = 50

Ball_Radius = 30

Ball_min_movement = 5

Refresh_Sec = 0.01
 

def create_animation_window():
  Window = tkinter.Tk()
  Window.title("Python Guides")

  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window
 

def create_animation_canvas(Window):
  canvas = tkinter.Canvas(Window)
  canvas.configure(bg="Blue")
  canvas.pack(fill="both", expand=True)
  return canvas
 

def animate_ball(Window, canvas,xinc,yinc):
  ball = canvas.create_oval(Ball_Start_XPosition-Ball_Radius,
            Ball_Start_YPosition-Ball_Radius,
            Ball_Start_XPosition+Ball_Radius,
            Ball_Start_YPosition+Ball_Radius,
            fill="Red", outline="Black", width=4)
  while True:
    canvas.move(ball,xinc,yinc)
    Window.update()
    time.sleep(Refresh_Sec)
    ball_pos = canvas.coords(ball)
    # unpack array to variables
    al,bl,ar,br = ball_pos
    if al < abs(xinc) or ar > Window_Width-abs(xinc):
      xinc = -xinc
    if bl < abs(yinc) or br > Window_Height-abs(yinc):
      yinc = -yinc
 

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_ball(Animation_Window,Animation_canvas, Ball_min_movement, Ball_min_movement)
~~~
Pre vytvorenie tejto ilúzie sú kľučové tri príkazy. Tvar gule v tomto príklade vytvoríme príkazom Canvas.create_oval(). pohyb gule príkazom Canvas.move() a pozastavenie vykonávania pohybu na daný pocčet sekund time.sleep().

Ďalším príkladom je jednoduchá animácia náhodného výberu a zmeny farby pozadia po stlačení tlačítka. Použijeme pri tom funkcie 
* random.choice() vráti zoznam s náhodne vybratou farbou.
* ws.title sa používa na označenie názvu okna.
* Button() sa používa na spustenie príkazu na generovanie náhodných farieb.
~~~
from tkinter import *
import random

def gen_color():
    ws.configure(background=random.choice(["black", "red" , "green" , "blue"]))
    
ws =Tk()
ws.title("Python Guides")
ws.geometry('500x500'

button=Button(ws,text='Click Me',command = gen_color).pack()
ws.mainloop()
~~~

Prvky animácie môžeme využiť aj v prípade GUI. Príkladom je grafické znázornenie načitávania údajov, spúštania programu alebo internetovej stránky.
~~~
from tkinter import *
from tkinter.ttk import *

ws=Tk()
Progress_Bar=Progressbar(ws,orient=HORIZONTAL,length=250,mode='determinate')

def Slide():
    import time
    Progress_Bar['value']=20
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=50
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=80
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=100

Progress_Bar.pack()
Button(ws,text='Run',command=Slide).pack(pady=10)
mainloop()
~~~
Animáciu môžeme tiež využiť aj v prípade zobrazenia hodín. Potrebujeme k tomu importovať časovú knižnicu ktorá nám umožní vytvárať údaje hodin, minút a sekund. N a ďalšom príklade to využijeme pri počítadle času ktoré upozorní na uplynutie zadanej hodnoty.
~~~
import time
from tkinter import *
from tkinter import messagebox

ws = Tk()

ws.geometry("300x300")

ws.title("Python Guides")

Hour=StringVar()
Minute=StringVar()
Second=StringVar()

Hour.set("00")
Minute.set("00")
Second.set("00")

Hour_entry= Entry(ws, width=3, font=("Arial",18,""),
				textvariable=Hour)
Hour_entry.place(x=80,y=20)

Minute_entry= Entry(ws, width=3, font=("Arial",18,""),
				textvariable=Minute)
Minute_entry.place(x=130,y=20)

Second_entry= Entry(ws, width=3, font=("Arial",18,""),
				textvariable=Second)
Second_entry.place(x=180,y=20)

def OK():
	try:
		
		temp = int(Hour.get())*3600 + int(Minute.get())*60 + int(Second.get())
	except:
		print("Please Input The Correct Value")
	while temp >-1:
		
		Mins,Secs = divmod(temp,60)

	
		Hours=0
		if Mins >60:
			
	
			Hours, Mins = divmod(Mins, 60)
		
		
		Hour.set("{0:2d}".format(Hours))
		Minute.set("{0:2d}".format(Mins))
		Second.set("{0:2d}".format(Secs))

		
		ws.update()
		time.sleep(1)

		
		if (temp == 0):
			messagebox.showinfo("Time Countdown", "Time up ")
		
		
		temp -= 1

button = Button(ws, text=' countdown', bd='5',
			command= OK)
button.place(x = 100,y = 110)

ws.mainloop()
~~~

V GUI sa tiež často používa animácia na označenie či je daný prvok dostupný alebo nie.V našom prípade budeme túto formu animácie demonštrovať na tlačítku ktoré tu plní funkciu vypínača.
~~~
from tkinter import *
ws = Tk()
ws.title("Python Guides")

def convert():
    if(a1['state']==NORMAL):
        a1["state"] = DISABLED
        a2["text"]="enable"
    elif (a1['state']==DISABLED):
        a1["state"]=NORMAL
        a2["text"]="disable"

#--Buttons
a1=Button(ws, text="button")
a1.config(height = 8, width = 9)
a1.grid(row=0, column=0)    
a2 = Button(text="disable", command=convert)
a2.grid(row=0,column=1)
ws.mainloop()
~~~
Ale to už je aj príklad ošetrenia jednotlivých grafických prvkov GUI a pridanie funkcionality t.j. čo sa má vykonať po ich aktivácii. 

[Video k téme](https://www.google.com/search?q=tkinter+animation&oq=tkinter+animation&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCggHEAAYDxgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBDjUxNzU4MjQ1NGowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:e0b481bf,vid:kvd6i1mXec8)

[Celý kurz videii na túto tému](https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV)

Na animácii je založená celá tvorba hier. Tak si aspoň náznakovo ukážme ako to funguje. V príklade je kód na animáciu pastavičky kedy je riešené spomalenie rýchlosti jej animácie bez toho aby sme menili frekvenciu zmeny snímkov t.j. aby sme museli spomaliť snímku oproti zvyšku hry.
~~~
import pygame
import glob


def fps():
    fr = "V.3 Fps: " + str(int(clock.get_fps()))
    frt = font.render(fr, 1, pygame.Color("coral"))
    return frt


class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super(MySprite, self).__init__()
        self.action = action
        # This is to slow down animation # takes the frame now and...
        self.elapsed = 0
        self.images = []
        self.temp_imgs = []
        self.load_images()
        self.count = 0

    def load_images(self):
        l_imgs = glob.glob(f"png\\{self.action}*.png")
        for img in l_imgs:
            if len(img) == len(l_imgs[0]):
                self.images.append(pygame.image.load(img))
            else:
                self.temp_imgs.append(pygame.image.load(img))
        self.images.extend(self.temp_imgs)
        self.index = 0
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.count += 1
        if self.index == len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        if self.count > 2: # tu sa robi spomalenie animacie
                #self.image = self.images[self.index]
                self.index += 1
                self.count = 0

    def group_sprites(self):
        return pygame.sprite.Group(self)


def group():
    "Dictionary of group of sprites"
    dici = {}
    actions = "idle walk run jump dead"
    actions = actions.split()
    for action in actions:
        dici[action] = MySprite(action).group_sprites()
    return dici


def main():
    global clock
    global font

    SIZE = 600, 600
    FPS = 60
    pygame.init()
    action = group()
    my_group = action["idle"]
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Game v.3")
    font = pygame.font.SysFont("Arial", 60)
    clock = pygame.time.Clock()
    keyactions = (
        (pygame.K_LEFT, "walk"),
        (pygame.K_UP, "jump"),
        (pygame.K_SPACE, "idle"),
        (pygame.K_RIGHT, "run"),
        (pygame.K_DOWN, "dead"))

    loop = 1
    while loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                for k, a in keyactions:
                    if event.key == k:
                        my_group = action[a]

        my_group.update()
        screen.fill((0, 0, 0))
        my_group.draw(screen)
        screen.blit(fps(), (10, 0))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
~~~
Program predpokladá inštaláciu knižnice pygame (pip install pygame) a glob (pip install glob2) a obrázky su umiestnené v adresári png.


>## Video

https://www.google.com/search?q=tkinter+video&oq=tkinter+video&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBDjUyNDUyNTgwMGowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8

Existuje spôsob, ako prehrať video súbory ako AVI , MP4 atď. V tomto príklade použijeme knižnicu OpenCV ktorú nainštalujeme takto pip install opencv-python

OpenCV (Open Source Computer Vision) je knižnica počítačového videnia, ktorá obsahuje rôzne funkcie na vykonávanie operácií s obrázkami alebo videami.
Aby sme pri OpenCV mohli zobraziť video, musíme vytvoriť objekt VideoCapture. VideoCapture(index) Podľa hodnoty indexu sa určuje či je použitá ručná kamera alebo webkamera resp. či pojde o načítanie videa zo súboru. Video zachytávame snímku po snímke.
~~~
* cv2.VideoCapture(0): Znamená prvú kameru alebo webovú kameru.
* cv2.VideoCapture(1): Znamená druhú kameru alebo webovú kameru.
* cv2.VideoCapture(“\\cesta_k_suboru\\nazov_suboru.mp4”): Znamená video súbor
~~~
~~~
# importujú sa knižnice
import cv2
import numpy as np

# Vytvorí sa objekt VideoCapture a prečíta sa vstupný súbor
cap = cv2.VideoCapture('c:\\users\\tomast\\documents\\sss-trencin\\multimedia\\shooting_training.mp4')

# Skontrolujte, či je fotoaparát otvorený alebo nie,
if (cap.isOpened()== False):
	print("Error opening video file")

# Vstupný súbor sa číta pokiaľ sa celý neprečíta
while(cap.isOpened()):
	
	# Celý súbor sa číta snímka po snímke
	ret, frame = cap.read()
	if ret == True:
	# Zobrazí sa výsledný frame - 
		cv2.imshow('Frame', frame)
		
	# Keša na klávesnici stlačí Q ukončí sa prehrávanie
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

# Preruší sa slučka
	else:
		break

# Ak sa všetko When everything done, release
# the video capture object
cap.release()

# Uzatvoria sa všetky frames
cv2.destroyAllWindows()
~~~
### Video aj so zvukom

Toto je spôsob, akým sa dá urobiť video aj so zvukom pomocou knižnice tkvideo. Existujú aj lepšie spôsoby ako tento problém riešiť, ale pre naše účely nám to bude postačovať. Najprv musíte získať zvuk pomocou get_audio() a potom začnete s funkciou start(). Vo vašom kóde zrejme budete musieť zmeniť názov súboru a cestu. Treba ale predtým inštalovať pip install moviepy, pip install tkvideo a pip install pygame.
~~~
# video_and_audio.py

import tkinter as tk
from tkvideo import tkvideo
import pygame
import os


def get_audio(file):
    from moviepy.editor import VideoFileClip

    # Load the MP4 file
    video = VideoFileClip(file + ".mp4")

    # Extract the audio
    audio = video.audio

    # Save the audio as an MP3 file
    audio.write_audiofile(file + ".mp3")


def start(file):
    if not file + ".mp3" in os.listdir("."):
        get_audio(file)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file + ".mp3")
    root = tk.Tk()
    # root.geometry("640x480")

    videoPlayer = tk.Label(root)
    videoPlayer.pack()
    video = tkvideo(file + ".mp4", videoPlayer, loop=1, size=(640, 480))
    video.play()
    pygame.mixer.music.play()
    root.mainloop()


start("c:\\users\\tomast\\documents\\sss-trencin\\multimedia\\froggo")
~~~

Toto je jednoduchá knižnica na prehrávanie video súborov v tkinteri. Táto knižnica tiež poskytuje možnosť prehrať, pozastaviť, preskočiť a vyhľadať konkrétne časové pečiatky.
~~~
import datetime
import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo


def update_duration(event):
    """ updates the duration after finding the duration """
    duration = vid_player.video_info()["duration"]
    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration


def update_scale(event):
    """ updates the scale value """
    progress_value.set(vid_player.current_duration())


def load_video():
    """ loads the video """
    file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)

        progress_slider.config(to=0, from_=0)
        play_pause_btn["text"] = "Play"
        progress_value.set(0)


def seek(value):
    """ used to seek a specific timeframe """
    vid_player.seek(int(value))


def skip(value: int):
    """ skip seconds """
    vid_player.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get() + value)


def play_pause():
    """ pauses and plays """
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"


def video_ended(event):
    """ handle video ended """
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)


root = tk.Tk()
root.title("Tkinter media")

load_btn = tk.Button(root, text="Load", command=load_video)
load_btn.pack()

vid_player = TkinterVideo(scaled=True, master=root)
vid_player.pack(expand=True, fill="both")

play_pause_btn = tk.Button(root, text="Play", command=play_pause)
play_pause_btn.pack()

skip_plus_5sec = tk.Button(root, text="Skip -5 sec", command=lambda: skip(-5))
skip_plus_5sec.pack(side="left")

start_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
start_time.pack(side="left")

progress_value = tk.IntVar(root)

progress_slider = tk.Scale(root, variable=progress_value, from_=0, to=0, orient="horizontal", command=seek)
# progress_slider.bind("<ButtonRelease-1>", seek)
progress_slider.pack(side="left", fill="x", expand=True)

end_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
end_time.pack(side="left")

vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

skip_plus_5sec = tk.Button(root, text="Skip +5 sec", command=lambda: skip(5))
skip_plus_5sec.pack(side="left")

root.mainloop()
~~~

V tomto [príklade](https://www-geeksforgeeks-org.translate.goog/how-to-show-webcam-in-tkinter-window-python/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) sme do aplikácie GUI umiestnili tlačidlo „Otvoriť fotoaparát“. Pri každom kliknutí na toto tlačidlo sa kamera otvorí, zatiaľ čo pri každom stlačení únikového tlačidla sa kamera vypne. Nižšie je uvedený kompletný kód na jednom mieste pre pohodlie čitateľov, aby mohli spustiť kód a zabaviť sa. Treba pip install tkinter, pip install opencv-python a pip install pillow. 
~~~
# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk

from tkinter import *
import cv2
from PIL import Image, ImageTk

# Define a video capture object
vid = cv2.VideoCapture(0)

# Declare the width and height in variables
width, height = 800, 600

# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Create a GUI app
app = Tk()

# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())

# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()

# Create a function to open camera and
# display it in the label_widget on app


def open_camera():

	# Capture the video frame by frame
	_, frame = vid.read()

	# Convert image from one color space to other
	opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	# Capture the latest frame and transform to image
	captured_image = Image.fromarray(opencv_image)

	# Convert captured image to photoimage
	photo_image = ImageTk.PhotoImage(image=captured_image)

	# Displaying photoimage in the label
	label_widget.photo_image = photo_image

	# Configure image in the label
	label_widget.configure(image=photo_image)

	# Repeat the same process after every 10 seconds
	label_widget.after(10, open_camera)


# Create a button to open the camera in GUI app
button1 = Button(app, text="Open Camera", command=open_camera)
button1.pack()

# Create an infinite loop for displaying app on screen
app.mainloop()
~~~

### Skombinovanie vlastného videa s vlastným audiom

Ak budeme potrebovať pridať k našemu videu zvukovú stopu a nepoužijeme k tomu niektorý z profesionálnzch nástrojov ako napr. [VideoPad](https://www.nchsoftware.com/videopad/index.html) môžeme si vytvoriť malý program a použiť takýto postup:
1. Nastavenie
Najprv musíme importovať požadované moduly z moviepy. Budeme používať VideoFileClip, AudioFileClip, a concatenate_videoclips. Budeme tiež musieť importovať os modul, aby sme získali prístup k adresáru našich súborov. Ak tieto knižnice nemáme nainštalované treba tak urobiť (pip install moviepy).
~~~
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os
~~~
2. Získať názov nového videa
Ďalej požiadame používateľa o názov nového videa. Toto sa použije na pomenovanie konečného súboru videa.
~~~
# Get the desired video title
title = input("Enter a title: ")
~~~
3. Otvoriť súbory videa a Audia
Teraz otvoríme spolu so zadaním úplnej cesty video a audio súbory, ktoré chceme skombinovať. Na otvorenie súborov použijeme VideoFileClipa .AudioFileClip
~~~
# Open the video and audio
video_clip = VideoFileClip("video.mp4")
audio_clip = AudioFileClip("audio.mp3")
~~~
4. Spojíme súbory
Keď sme klipy otvorili, môžeme ich spojiť pomocou concatenate_videoclips. Tým sa skombinuje videoklip so zvukovým klipom a vytvorí sa jeden klip s oboma prvkami.
~~~
# Export the final video with audio
final_clip.write_videofile(title + ".mp4")
~~~