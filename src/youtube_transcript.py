from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import re


"""
Extracts a YouTube video ID from a given URL (watch, shorts, or youtu.be) 
or returns it directly if it's already an ID.

Args:
    url_or_id (str): YouTube URL or raw video ID.

Returns:
    str: Extracted video ID.
"""
def extract_video_id(url_or_id: str) -> str:
    # Direct video ID
    if len(url_or_id) == 11 and re.match(r"^[a-zA-Z0-9_-]{11}$", url_or_id):
        return url_or_id

    parsed = urlparse(url_or_id)
    query = parse_qs(parsed.query)

    # Standard watch URL (e.g., youtube.com/watch?v=...)
    if "v" in query:
        return query["v"][0]

    # Short URL (youtu.be/<id>)
    if parsed.netloc in ["youtu.be", "www.youtu.be"]:
        return parsed.path.strip("/")

    # Shorts URL (youtube.com/shorts/<id>)
    if "shorts" in parsed.path:
        match = re.search(r"/shorts/([a-zA-Z0-9_-]{11})", parsed.path)
        if match:
            return match.group(1)

    # Embedded video (youtube.com/embed/<id>)
    if "embed" in parsed.path:
        match = re.search(r"/embed/([a-zA-Z0-9_-]{11})", parsed.path)
        if match:
            return match.group(1)

    raise ValueError(f"❌ Invalid YouTube URL or ID: {url_or_id}")



"""
Fetches transcript text from a YouTube video or Shorts link and cleans it.

Args:
    url_or_id (str): YouTube URL or video ID.

Returns:
    str: Cleaned lowercase transcript text.
"""
def fetch_transcript(url_or_id: str) -> set[str]:
    video_id = extract_video_id(url_or_id)

    # Fetch transcript
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)

    # Combine all transcript segments into a single string
    all_text = " ".join([t.text for t in fetched_transcript])

    # Remove non-alphabetic characters and convert to lowercase
    clean_text = re.sub(r"[^a-zA-Z\s]", "", all_text).lower()
    words = clean_text.split()
    unique_words = set(words)

    return unique_words

