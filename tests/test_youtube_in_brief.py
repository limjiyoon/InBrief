from inbrief.summarizer.echo_summarizer import EchoSummarizer
from inbrief.types import Transcript
from inbrief.youtube_inbrief import YoutubeInBrief


class TestYoutubeInBrief:
    def test_fetch_youtube_transcript(self) -> None:
        # Given
        # Video: "당신에게 배달 시간이 전달되기까지: 불확실성을 다루는 예측 시스템 구축 과정" by 우아한테크
        video_url = "https://www.youtube.com/watch?v=SkliEsGRuSQ"
        summarizer = EchoSummarizer()

        # When
        youtube_inbrief = YoutubeInBrief(summarizer=summarizer)
        transcript = youtube_inbrief.fetch_transcript(video_url)

        # Then
        assert isinstance(transcript, Transcript)
