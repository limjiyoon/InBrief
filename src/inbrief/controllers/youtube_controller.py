from fastapi import APIRouter
from loguru import logger

from inbrief.summarizer.logic_tree_summarizer import LogicTreeSummarizer
from inbrief.summarizer.simple_summarizer import SimpleSummarizer
from inbrief.youtube_inbrief import YoutubeInBrief


router = APIRouter(prefix="/youtube")


@router.get("/simple")
def generate_simple_summarize(url: str, model_name: str = "models/gemini-1.5-flash"):
    summarizer = SimpleSummarizer(model_name)
    yt = YoutubeInBrief(summarizer)
    logger.info("Fetch transcript")
    transcript = yt.fetch_transcript(url)
    logger.info("Create summarize...")
    summary = yt.summarize(transcript)
    logger.info("Complete summarize task")
    return summary

@router.get("/logictree")
def generate_logic_tree(url: str, max_depth: int = 1, model_name: str = "models/gemini-1.5-flash"):
    summarizer = LogicTreeSummarizer(model_name, max_depth)
    yt = YoutubeInBrief(summarizer)
    logger.info("Fetch transcript")
    transcript = yt.fetch_transcript(url)

    logger.info("Create summarize...")
    summary = yt.summarize(transcript)
    logger.info("Complete summarize task")
    return summary

    