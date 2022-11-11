import os
import random

from dotenv import load_dotenv

load_dotenv()

MIN_VALUE = 0
MAX_VALUE = 100
TRYS_COUNT_DEFAULT = 3
RANDOM_SEED = os.getenv("RANDOM_SEED")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

random.seed(RANDOM_SEED)
RANDOM_VALUE = random.randint(MIN_VALUE, MAX_VALUE)
