import os
import time
def play(song):
    print("Playing:-",song)
while True:
    os.system("clear")
    print("🎵My Music Player🎵")
    print("1.Play Song")
    print("2.Exit")

    choice=input("Enter your choice:-")

    if choice=="1":
        song_name=input("Enter the name of the song:-")
        play(song_name)
        input("Press Enter to continue...")
    elif choice=="2":
        print("Exit the program...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
        time.sleep(1)
        break