from music_player import play_song, stop_song, pause_song

def get_response(user_input):
    # 🛑 Handle empty input
    if not user_input:
        return "I didn't catch that."

    command = user_input.lower().strip()

    try:
        # 🎵 -------- MUSIC CONTROLS --------

        # ▶️ Play Song
        if "play" in command:
            # Extract song name properly
            song = command.split("play", 1)[-1]
            song = song.replace("song", "").strip()

            if song:
                play_song(song)
                return f"Playing {song} 🎧"
            else:
                return "Tell me the song name to play."

        # ⏸️ Pause
        elif "pause" in command:
            pause_song()
            return "Music paused ⏸️"

        # ⏹️ Stop
        elif "stop" in command:
            stop_song()
            return "Music stopped ⏹️"

        # 🧠 -------- BASIC RESPONSES --------

        elif command in ["hi", "hello"]:
            return "Hey! I'm Cooper 😎"

        elif "how are you" in command:
            return "I'm running perfectly. What about you?"

        elif "who are you" in command:
            return "I'm Cooper, your personal AI assistant 🤖"

        # ❓ Unknown
        else:
            return "I didn't understand that. Try saying play, pause, or stop."

    except Exception as e:
        print("Error:", e)
        return "Something went wrong while processing your request."