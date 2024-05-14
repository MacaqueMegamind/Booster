import os

from dotenv import load_dotenv

load_dotenv("data/token.env")

KEY_SIM_API = os.getenv("sim_api")
