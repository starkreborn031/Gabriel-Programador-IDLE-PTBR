import tkinter as tk
from tkinter import filedialog
import pygame
from mutagen.mp3 import EasyMP3
from PIL import Image, ImageTk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title('Music Player')
        self.root.geometry('400x300')

        pygame.mixer.init()

        self.status = tk.StringVar()
        self.status.set('Escolha uma música')

        self.filename = None
        self.photo = None

        self.label_image = tk.Label(self.root, text='Thumbnail aqui')
        self.label_image.pack(pady=10)

        tk.Label(self.root, textvariable=self.status).pack()

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        tk.Button(buttons_frame, text='Abrir', command=self.open_file).pack(side=tk.LEFT)
        tk.Button(buttons_frame, text='Play', command=self.play_music).pack(side=tk.LEFT)
        tk.Button(buttons_frame, text='Pause', command=self.pause_music).pack(side=tk.LEFT)
        tk.Button(buttons_frame, text='Unpause', command=self.unpause_music).pack(side=tk.LEFT)
        tk.Button(buttons_frame, text='Stop', command=self.stop_music).pack(side=tk.LEFT)

    def open_file(self):
        self.filename = filedialog.askopenfilename()
        audio = EasyMP3(self.filename)

        # Verifica se a tag 'title' existe
        if 'title' in audio:
            self.status.set('Música selecionada: ' + audio['title'][0])
        else:
            self.status.set('Música selecionada: Sem título disponível')

        # Carrega a thumbnail se disponível
        if 'APIC:' in audio.tags:
            artwork = audio.tags['APIC:'].data
            with open('temp_art.jpg', 'wb') as img:
                img.write(artwork)
                self.photo = ImageTk.PhotoImage(Image.open('temp_art.jpg'))
                self.label_image.config(image=self.photo)
        else:
            self.label_image.config(text='Thumbnail não disponível')

    def play_music(self):
        if self.filename:
            pygame.mixer.music.load(self.filename)
            pygame.mixer.music.play(loops=0)
            self.status.set('Música tocando...')

    def pause_music(self):
        pygame.mixer.music.pause()
        self.status.set('Música pausada...')

    def unpause_music(self):
        pygame.mixer.music.unpause()
        self.status.set('Música tocando...')

    def stop_music(self):
        pygame.mixer.music.stop()
        self.status.set('Música parada...')

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
