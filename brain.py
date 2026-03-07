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
    text = user_text.lower().strip()

    # Math
    if any(op in text for op in ["+", "-", "*", "/", "sqrt", "sin", "cos", "tan"]):
        return solve_math(text)

    # GitHub
    if "github" in text:
        repo = text.replace("github", "").strip()
        if repo == "":
            return "Tell me what repository to search."
        results = search_github(repo)
        return "\n".join(results) if isinstance(results, list) else str(results)

    # Weather
    if "weather" in text:
        city = text.replace("weather", "").strip()
        if city == "":
            city = "chennai"
        return str(get_weather(city))

    # Robot
    if "move robot" in text:
        direction = text.replace("move robot", "").strip()
        if direction == "":
            return "Tell me which direction to move."
        return str(move_robot(direction))

    # File reader
    if "read file" in text:
        path = text.replace("read file", "").strip()
        if path == "":
            return "Tell me the file path."
        return str(read_file(path))

    # Default chatbot
    return str(bot.get_response(user_text))

