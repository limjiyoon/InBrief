from inbrief.types import Transcript
from inbrief.youtube_inbrief import YoutubeInBrief


class TestYoutubeInBrief:
    def test_load_youtube_inbrief(self):
        # Given
        # Video: "당신에게 배달 시간이 전달되기까지: 불확실성을 다루는 예측 시스템 구축 과정" by 우아한테크
        video_id = "SkliEsGRuSQ"

        # When
        youtube_inbrief = YoutubeInBrief()
        transcript = youtube_inbrief.fetch_transcript(video_id)

        # Then
        assert isinstance(transcript, Transcript)
