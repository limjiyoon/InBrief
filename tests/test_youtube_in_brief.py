from inbrief.types import Transcript
from inbrief.youtube_inbrief import YoutubeInBrief


class TestYoutubeInBrief:
    def test_fetch_youtube_transcript(self):
        # Given
        # Video: "당신에게 배달 시간이 전달되기까지: 불확실성을 다루는 예측 시스템 구축 과정" by 우아한테크
        video_url = "https://www.youtube.com/watch?v=SkliEsGRuSQ"

        # When
        youtube_inbrief = YoutubeInBrief()
        transcript = youtube_inbrief.fetch_transcript(video_url)

        # Then
        assert isinstance(transcript, Transcript)
