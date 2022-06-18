
class XvideosDlCommands:

    # 동영상 다운로드
    @classmethod
    def download_video(cls, url: str) -> list[str]:
        return ['xvideos-dl', url]
