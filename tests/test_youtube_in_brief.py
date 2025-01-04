from inbrief.youtube_inbrief import YoutubeInBrief


class TestYoutubeInBrief:
    def test_load_youtube_inbrief(self):
        # Given
        video_id = "SkliEsGRuSQ"

        # When
        youtube_inbrief = YoutubeInBrief()
        transcript = youtube_inbrief.fetch_transcript(video_id)

        # Then
        assert transcript is not None
