from music_player import play_song, stop_song, pause_song

def get_response(user_input):
    if not user_input:
        return "I didn't catch that."

    command = user_input.lower().strip()

    try:
        # 🎵 -------- MUSIC CONTROLS --------
        if "play" in command:
            song = command.replace("play", "").replace("song", "").strip()

            if song:
                play_song(song)
                return f"Playing {song} 🎧"
            else:
                return "Which song should I play?"

        elif "pause" in command:
            pause_song()
            return "Music paused ⏸️"

        elif "stop" in command:
            stop_song()
            return "Music stopped ⏹️"

        # 🧠 -------- EXISTING LOGIC (KEEP YOUR OLD RESPONSES HERE) --------
        # Example:
        elif "hello" in command:
            return "Hey! I'm Cooper 😎"

        elif "how are you" in command:
            return "I'm running perfectly. What about you?"

        # 👉 IMPORTANT: Keep your previous conditions below this line
        # (paste your old code here if you had more responses)

        else:
            return "I didn't understand that."

    except Exception as e:
        print("Error:", e)
        return "Something went wrong while processing your request."