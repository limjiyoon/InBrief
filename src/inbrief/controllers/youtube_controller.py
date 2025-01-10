from fastapi import APIRouter

from inbrief.summarizer.simple_summarizer import SimpleSummarizer
from inbrief.youtube_inbrief import YoutubeInBrief


router = APIRouter(prefix="/youtube")


@router.get("/simple")
def generate_simple_summarize(url: str):
    model_name = "models/gemini-1.5-flash"
    summarizer = SimpleSummarizer(model_name)
    yt = YoutubeInBrief(summarizer)
    transcript = yt.fetch_transcript(url)
    summary = yt.summarize(transcript)
    return summary