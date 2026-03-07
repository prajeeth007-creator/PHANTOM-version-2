from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from skills.math_skill import solve_math
from skills.unit_skill import convert_units


bot = ChatBot(
    "cooper",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "cooper does not compute!",
            "maximum_similarity_threshold": 0.90
        }
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


def get_response(message):

    message = message.lower()

    # try math skill
    math_result = solve_math(message)
    if math_result:
        return math_result

    # try unit skill
    unit_result = convert_units(message)
    if unit_result:
        return unit_result

    # fallback to chatbot
    return str(bot.get_response(message))