import sqlite3
import pandas as pd
from config import DB_PATH, FREQ_FILE

def setup_database():
    """Creates SQLite DB and populates frequency table from Excel."""
    
    # Connect (creates file if doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    
    # Read Excel file
    df = pd.read_excel(FREQ_FILE)
    
    # Select relevant columns (Word, SUBTLWF, Zipf, PoS)
    # Adjust column names based on your Excel file
    df = df[["Word", "SUBTLWF", "Zipf", "Pos"]]
    df.columns = ["word", "freq", "zipf", "pos"]
    
    # Lowercase words for easier lookup
    df["word"] = df["word"].str.lower()
    
    # Write to SQLite table (replace if exists)
    df.to_sql("frequency", conn, if_exists="replace", index=False)
    
    # Create an index on the word column for fast lookups
    conn.execute("CREATE INDEX IF NOT EXISTS idx_word ON frequency(word)")
    
    conn.commit()
    conn.close()
    print(f"Database created at {DB_PATH} with table 'frequency'.")

if __name__ == "__main__":
    setup_database()
