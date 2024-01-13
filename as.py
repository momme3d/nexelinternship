import pygame
import os


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def main():
    print("Simple Music Player")
    print("-------------------")

    # Assuming your music files are in the same directory as this script
    music_folder = os.path.dirname(os.path.abspath(__file__))

    # List all music files in the current directory
    music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    if not music_files:
        print("No music files found in the current directory.")
        return

    print("Available Music:")
    for i, music_file in enumerate(music_files, start=1):
        print(f"{i}. {music_file}")

    try:
        choice = int(input("Enter the number of the music file to play: "))
        if 1 <= choice <= len(music_files):
            selected_music = os.path.join(music_folder, music_files[choice - 1])
            play_music(selected_music)
            input("Press Enter to stop the music...")
            pygame.mixer.music.stop()
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
