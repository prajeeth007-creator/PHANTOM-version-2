import pygame
import os

pygame.mixer.init()

MUSIC_FOLDER = "music"

def play_song(song_name):
    for file in os.listdir(MUSIC_FOLDER):
        if song_name.lower() in file.lower():
            pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, file))
            pygame.mixer.music.play()
            print(f"Playing {file}")
            return
    print("Song not found")

def stop_song():
    pygame.mixer.music.stop()

def pause_song():
    pygame.mixer.music.pause()