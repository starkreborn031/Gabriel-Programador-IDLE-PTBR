import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title('Music Player')
        self.root.geometry('400x400')

        pygame.mixer.init()

        self.status = tk.StringVar()
        self.status.set('Escolha uma música')

        self.filename = None

        tk.Label(self.root, textvariable=self.status).pack(pady=10)
        tk.Button(self.root, text='Abrir', command=self.open_file).pack()
        tk.Button(self.root, text='Play', command=self.play_music).pack()
        tk.Button(self.root, text='Pause', command=self.pause_music).pack()
        tk.Button(self.root, text='Unpause', command=self.unpause_music).pack()
        tk.Button(self.root, text='Stop', command=self.stop_music).pack()

    def open_file(self):
        self.filename = filedialog.askopenfilename()
        self.status.set('Música selecionada: ' + self.filename.split('/')[-1])

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
