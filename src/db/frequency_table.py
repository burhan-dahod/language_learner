# src/db/frequency_table.py
import sqlite3
import pandas as pd
from config import DB_PATH, FREQ_FILE

def create_frequency_table():
    """Load SUBTLEX-US Excel file and write it to SQLite."""
    conn = sqlite3.connect(DB_PATH)

    # Read Excel
    df = pd.read_excel(FREQ_FILE)
    df = df[["Word", "SUBTLWF", "Zipf", "Pos"]]
    df.columns = ["word", "freq", "zipf", "pos"]
    df["word"] = df["word"].str.lower()

    # Write to SQLite
    df.to_sql("frequency", conn, if_exists="replace", index=False)

    # Optional: create an index on 'word' for faster lookups
    conn.execute("CREATE INDEX IF NOT EXISTS idx_word ON frequency(word)")

    conn.commit()
    conn.close()
    print("Table 'frequency' created successfully.")
