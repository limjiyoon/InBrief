from inbrief.llm_factory import LlmFactory
from inbrief.youtube_inbrief import YoutubeInBrief


class Summarizer:
    """Summarize text using a language model."""

    def __init__(self, model_name: str):
        assert model_name in LlmFactory().available_models(), f"Model '{model_name}' is not available."
        self._model = LlmFactory().create(model_name)

    def summarize(self, text: str) -> str:
        return self._model.generate_content(["Summarize following contents", text]).text


if __name__ == "__main__":
    yt = YoutubeInBrief()
    video_url = "https://www.youtube.com/watch?v=loaTGpqfctI"
    transcript = yt.fetch_transcript(video_url)
    text = " ".join(chunk.text for chunk in transcript.chunks)
    summarizer = Summarizer("models/gemini-1.5-flash")
    summary = summarizer.summarize(text)
    print(summary)
