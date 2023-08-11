#### Audio

Práca so zvukom obsahuje nasledovné činnosti:
* **Prehrávanie** širokej škály zvukových formátov vrátane polí WAV, MP3 a NumPy
* **Nahrávanie** z mikrofónu do poľa NumPy alebo Pythonu
* **Uladanie** nahraného zvuku v rôznych formátoch vrátane WAV a MP3
* **Transformáciu** svojich zvukových súborov do rôznych zvukových formátov

Zvukové súbory v Pythone môžeme prehrávať tiež pomocou jeho knižníc. Najprv si ukážeme metódy niektorých knižníc ktoré umožňujú iba samotné prehrávanie a nahrávanie zvuku. Potom sa pozrieme na niektoré knižnice, ktoré ponúkajú za cenu niekoľkých riadkov kódu navyše viac funkcií. 
Knižnica Tkinter nám na prehrávanie zvukov a hudby ponúka dva moduly :
1. **pygame** ktorý je multiplatformový modul na vytváranie hier a GUI.
2. **playsound** ktorý je multiplatformový modul a názov funkcie je playsound()

Súbor mp3 v ktorom sa nachádza náš zvuk by mal byť v rovnakom priečinku kde sa bude nachádzať náš pythonovský program na jeho spracovanie resp. k tomuto súboru je potrebné poznať úplnú cestu. Súbor mp3 ktorý použijeme v našom príklade obsahuje [pesnicku](Bobi.mp3). Predpokladom na použitie pygame resp. playsound je aby tieto knižnice boli nainštalované. Použijeme sa na to tento príkaz
~~~
pip install pygame resp. playsound
~~~
Na vlastné prehratie skladby je používaný príkaz ktorého syntax vyzerá nasledovne:
~~~
mixer.music.load(“skladba.mp3”)
~~~
Tento príkaz je umiestnený v definícii funkcie s názvom play() ktorá je volaná postlačení tlačítka. Takto máme súčasne demonštrované ako sa vlastne ošetrujú jednotlivé prvky grafiky a aby po ich aktivovaní vykonali požadovanú činnosť. 
~~~
# import potrebnych kniznic
from tkinter import *
import pygame

# vytvorenie pracovnej plochy- platna s nadpisom
root = Tk()
root.title('GeeksforGeeks sound player')
root.geometry("500x400")

# inicializacia pygame
pygame.mixer.init() 

def play():
	pygame.mixer.music.load("Bobi.mp3")
	pygame.mixer.music.play(loops=0)

title=Label(root,text="GeeksforGeeks",bd=9,relief=GROOVE,
			font=("times new roman",50,"bold"),bg="white",fg="green")
title.pack(side=TOP,fill=X)

play_button = Button(root, text="Play Song", font=("Helvetica", 32), command=play)
play_button.pack(pady=20)
root.mainloop()
~~~

Nasledovný príklad je totožný s predchádzajúcim príkladom avšak na prehratie audio záznamu používa knižnicu playsound ktorého príkaz má nasledovnú syntax:
~~~
playsound(sound, block=True)
~~~
~~~
# importing required module
from playsound import playsound
from tkinter import *
                      
root = Tk()
root.title('GeeksforGeeks sound player') #giving the title for our window
root.geometry("500x400")
                      
# making function
def play():
    playsound('Bobi.mp3')
                      
# title on the screen you can modify it
title=Label(root,text="GeeksforGeeks",bd=9,relief=GROOVE,
font=("times new roman",50,"bold"),bg="white",fg="green")
title.pack(side=TOP,fill=X)
                      
# making a button which trigger the function so sound can be playeed
play_button = Button(root, text="Play Song", font=("Helvetica", 32),relief=GROOVE, command=play)
                      
play_button.pack(pady=20)
info=Label(root,text="Click on the button above to play song ",
font=("times new roman",10,"bold")).pack(pady=20)
                      
root.mainloop()
~~~
K ďalším knižniciam ktoré na tomto mieste ešte spomenieme patria:
* **simpleaudio** ktorá umožňuje prehrávať súbory WAV a polia NumPy a dáva nám naviac možnosť kontrolovať, či sa súbor stále prehráva.
* **winsound** ktorá umožňuje prehrávať súbory WAV a v systéme Windows pripojiť aj reproduktory.
* **python-sounddevice** a **pyaudio** ktoré poskytujú väzby na knižnicu **PortAudio** ktorá umožňuje prehrávanie súborov WAV medzi rôznymi platformami.
* **pydub** vyžaduje na prehrávanie zvuku knižnicu pyaudio a umožňuje prehrávať veľké množstvo zvukových formátov ak je nainštalovaný [ffmpeg](https://ffmpeg.org/download.html) (súbor nástrojov pre spracovanie audia a videa).

Úplný zoznam knižníc Python súvisiacich so zvukom nájdete na [stránke wiki o zvuku v jazyku Python](https://wiki.python.org/moin/Audio/) .

### simpleaudio - nefunguje mi to pod windows ???

Simpleaudio je multiplatformová knižnica na prehrávanie (mono a stereo záznamov) súborov WAV.
~~~
# treba mat vsetky kniznice - trochu zlozite pre Windows
import simpleaudio as sa 

filename = 'myfile.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing
~~~
Pri nahrávkach je ukladanie každej zvukovej vzorky (jednotlivý zvukový dátový bod týkajúci sa tlaku vzduchu) ako 2-bytová hodnota pri frekvencii 44 100 resp. 8000 vzorkách za sekundu. Niektoré z knižníc prehráva a zaznamenáva zvuk ako byt-y, zatiaľ čo iné na ukladanie nespracovaných zvukových údajov používajú polia NumPy. Dôležitým rozdielom medzi týmito dvoma typmi údajov je, že byt-ové objekty s, zatiaľ čo polia NumPy sú meniteľné, a preto je **NumPy vhodnejšie na generovanie zvukov a na komplexnejšie spracovanie signálu**. Pre viac informácií o tom, ako pracovať s NumPy, si pozrite naše NumPy [tutoriály](https://realpython.com/tutorials/numpy/) . Simpleaudio umožňuje prehrávať ako polia  tak aj byt-y a používa na to simpleaudio.play_buffer(). Samozrejme že aj Numpy je potrebné mať pred tým nainštalované (pip install numpy).
V príklade vygenerujeme pole NumPy zodpovedajúce tónu 440 Hz a prehráme ho pomocou simpleaudio.play_buffer():

### winsound

Ak používate Windows, môžete použiť vstavaný winsoundmodul na prístup k jeho základnému zariadeniu na prehrávanie zvuku. Prehrávať je možné však iba súbor WAV.
~~~
import winsound

filename = 'StarWars60.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)
~~~
Príklad vykoná pípanie 1000 Hz tónu na 100 milisekúnd pomocou nasledujúceho kódu:
~~~
import winsound

winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
~~~
#### pydub

Keď sa na prácu so záznamom použije knižnica pydub musí byť nainštalovaný niektorý z týchto balíkov: Odporúčaný je predovšetkým simpleaudio ale pyaudio, ffplay, a avplay prichádzajú ako alternatívne možnosti.
~~~
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav('myfile.wav')
play(sound)
~~~
Ak chcete prehrávať iné typy zvuku, ako sú súbory MP3, je potrebné nainštalovať ffmpeg alebo libav. Ako to urobiť pre pydub nájdeme v [dokumentácii](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up).ffmpeg možno pomocou pip:
~~~
$ pip install ffmpeg-python
~~~
Po ffmpeg nainštalovaní vyžaduje prehrávanie súboru MP3 iba malú zmenu v našom predchádzajúcom kóde:
~~~
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('myfile.mp3')
play(sound)
~~~
Pomocou príkazu AudioSegment.from_file(filename, filetype) môžeme prehrávať akýkoľvek typ zvukového súboru, ktorý ffmpeg podporuje. Okrem prehrávania zvukových súborov a ukladania zvuku v rôznych formátoch pydub umožňuje rozdeľovať zvuk, vypočítať dĺžku zvukových súborov, zoslabovať alebo zoslabovať zvuk a aplikovať krížové zoslabovanie a pod.

### python-sounddevice

python-sounddevice poskytuje väzby na knižnicu [PortAudio](http://www.portaudio.com/) a niekoľko praktických funkcií na prehrávanie a nahrávanie polí NumPy obsahujúcich zvukové signály“. Ak chcete prehrávať súbory WAV numpy a soundfile je potrebné ich nainštalovať, otvárajte súbory WAV ako polia NumPy. S nainštalovanými sounddevice, numpy, a soundfile teraz môžete čítať súbor WAV ako pole NumPy a prehrávať ho:
~~~
import sounddevice as sd
import soundfile as sf

filename = 'myfile.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing
~~~

python-sounddevice umožňuje nahrávať zvuk z mikrofónu a ukladať ho ako pole NumPy. Ide o praktický dátový typ na spracovanie zvuku, ktorý je možné pomocou modulu previesť do formátu WAV na ukladanie scipy.io.wavfile. Uistite sa, že ste nainštalovali scipy modul pre nasledujúci príklad ( pip install scipy). Toto automaticky nainštaluje NumPy ako jednu zo svojich závislostí:
~~~
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 
~~~

### pyaudio

pyaudio poskytuje väzby na PortAudio čo je multiplatformová audio I/O knižnica. To znamená, že pyaudio môžete použiť  na prehrávanie/nahrávanie zvuku na rôznych platformách ako Windows, Linux a Mac. S pyaudio-m sa nahrávanie zvuku vykonáva zápisom do streamu:
~~~
import pyaudio
import wave

filename = 'myfile.wav'

# Set chunk size of 1024 samples per data frame
chunk = 1024  

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()
~~~

Nahrávanie zvuku je možné vykonať zápisom do streamu pomocou tohoto kódu:
~~~
import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
~~~

Práca s pyaudio je síce komplikovanejšia ale vám poskytuje viac kontroly, je možné získať a nastaviť parametre pre vaše vstupné a výstupné zariadenia alebo skontrolovať zaťaženie procesora a vstupnú alebo výstupnú latenciu.

## Ukladanie a konverzia zvuku
Už ste videli , že modul môžete použiť scipy.io.wavfile na ukladanie polí NumPy ako súbory WAV. Modul wavio vám podobne umožňuje konvertovať medzi súbormi WAV a poľami NumPy . Ak chcete uložiť svoj zvuk v inom formáte súboru prídete na to vhod **pydub** a **soundfile**, pretože vám umožňujú čítať a zapisovať celý rad populárnych formátov súborov (napríklad MP3, FLAC, WMA a FLV atď).

### wavio
Tento modul závisí od numpy a umožňuje vám čítať súbory WAV ako polia NumPy a ukladať polia NumPy ako súbory WAV.
Ak chcete uložiť pole NumPy ako súbor WAV, môžete použiť wavio.write():
~~~
import wavio

wavio.write("myfile.wav", my_np_array, fs, sampwidth=2)
~~~
V tomto príklade my_np_array je pole NumPy obsahujúce zvuk, fs je vzorkovacia frekvencia záznamu (zvyčajne 44100 alebo 44800 Hz) a sampwidth šírka vzorkovania zvuku (počet bajtov na vzorku, zvyčajne 1 alebo 2 bajty). Výstupný súbor si môžeme pozrieť aj pomocou [Hex editora](https://www.google.com/search?q=vscode+view+hexadecimal&sxsrf=AB5stBhIRGGu4FLWj7fVqsMG7JWwEnKCgA%3A1691046656747&source=hp&ei=AFPLZP-MK66Hxc8Ph4aawA0&iflsig=AD69kcEAAAAAZMthEDKnNtAC5s-jU7yZlcnNLGiaROZO&oq=vs-code+view+hexa&gs_lp=Egdnd3Mtd2l6IhF2cy1jb2RlIHZpZXcgaGV4YSoCCAAyBhAAGB4YDTIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSKqoAVDaC1i6UHABeACQAQCYAZgBoAGJDqoBBDUuMTK4AQHIAQD4AQGoAgrCAgcQIxjqAhgnwgIHEC4Y6gIYJ8ICBBAjGCfCAgwQIxiKBRgTGIAEGCfCAhEQLhiDARjHARixAxjRAxiABMICCxAAGIAEGLEDGIMBwgIREC4YgAQYsQMYgwEYxwEY0QPCAgUQABiABMICBxAAGIoFGEPCAg0QABiABBixAxiDARgKwgIHEAAYgAQYCsICBBAAGB7CAgYQABgeGA_CAgYQABgeGArCAggQABiABBjLAcICChAAGIAEGAoYywHCAgcQABgNGIAEwgIJEAAYDRgTGIAEwgIIEAAYFhgeGBPCAgoQABgIGB4YDRgT&sclient=gws-wiz#kpvalbx=_HVPLZN3NKryK9u8P66G2wAs_31) nainštalovaného ako extension.

Príklad audia pri vykreslovaní grafu najdeme [tu](https://www.geeksforgeeks.org/plotting-various-sounds-on-graphs-using-python-and-matplotlib/).