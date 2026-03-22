from music_player import play_song, stop_song, pause_song
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from skills.github_search import search_github
from skills.math_skill import solve_math
from skills.robot_control import move_robot
from skills.weather import get_weather
from skills.file_reader import read_file

bot = ChatBot("cooper")

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


def get_response(user_text):
    if not user_text:
        return "I didn't catch that."

    text = user_text.lower().strip()

    try:
        # 🎵 -------- MUSIC CONTROLS --------
        if "play" in text:
            song = text.split("play", 1)[-1].replace("song", "").strip()

            if song:
                play_song(song)
                return f"Playing {song} 🎧"
            else:
                return "Tell me the song name."

        elif "pause" in text:
            pause_song()
            return "Music paused ⏸️"

        elif "stop" in text:
            stop_song()
            return "Music stopped ⏹️"

        # 🧮 -------- MATH --------
        elif any(op in text for op in ["+", "-", "*", "/", "sqrt", "sin", "cos", "tan"]):
            return str(solve_math(text))

        # 💻 -------- GITHUB --------
        elif "github" in text:
            repo = text.replace("github", "").strip()
            if repo == "":
                return "Tell me what repository to search."
            results = search_github(repo)
            return "\n".join(results) if isinstance(results, list) else str(results)

        # 🌦️ -------- WEATHER --------
        elif "weather" in text:
            city = text.replace("weather", "").strip()
            if city == "":
                city = "chennai"
            return str(get_weather(city))

        # 🤖 -------- ROBOT CONTROL --------
        elif "move robot" in text:
            direction = text.replace("move robot", "").strip()
            if direction == "":
                return "Tell me which direction to move."
            return str(move_robot(direction))

        # 📂 -------- FILE READER --------
        elif "read file" in text:
            path = text.replace("read file", "").strip()
            if path == "":
                return "Tell me the file path."
            return str(read_file(path))

        # 🧠 -------- DEFAULT CHATBOT --------
        else:
            return str(bot.get_response(user_text))

    except Exception as e:
        print("Error:", e)
        return "Something went wrong."

