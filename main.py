from src.youtube_transcript import fetch_transcript
from src.text_processing import normalize_text

def main(video_id: str):
    print("🎥 Fetching transcript...")
    text = fetch_transcript(video_id)

    print("🧹 Normalizing text...")
    processed_words = normalize_text(text)

    return processed_words


if __name__ == "__main__":
    # Example YouTube video ID
    a = main("kPa7bsKwL-c")
    print(a)
