import pandas as pd
from .config import FREQ_FILE


def load_frequency_data():
    """
    Loads a frequency dataset and prepares it for lookups.

    Returns:
        pd.DataFrame: DataFrame with lowercase words and frequencies.
    """
    df = pd.read_csv(FREQ_FILE, sep="\t", encoding="latin1")
    df = df[["Word", "SUBTLWF"]]
    df.columns = ["word", "freq"]
    df["word"] = df["word"].str.lower()
    return df


def find_rare_words(words, freq_df):
    """
    Matches each word to its frequency and sorts by rarity.

    Args:
        words (list[str]): Words from transcript.
        freq_df (pd.DataFrame): Frequency lookup.

    Returns:
        list[tuple[str, float]]: (word, frequency) sorted ascending.
    """
    def get_freq(word):
        row = freq_df.loc[freq_df["word"] == word]
        return float(row["freq"].values[0]) if not row.empty else 0.0

    word_freqs = [(w, get_freq(w)) for w in set(words)]
    return sorted(word_freqs, key=lambda x: x[1])
