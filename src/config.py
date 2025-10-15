from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).resolve().parent  # Points to src/
DATA_DIR = BASE_DIR.parent / "data"        # Points to the ../data/ folder

# Paths to important files
FREQ_FILE = DATA_DIR / "SUBTLEX_US.xlsx"       # Excel frequency list
DB_PATH = DATA_DIR / "language_learner.db"     # SQLite DB
SLANG_DICT_PATH = DATA_DIR / "slang_dict.json" # Slang dictionary JSON