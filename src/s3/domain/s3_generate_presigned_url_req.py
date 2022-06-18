# presigned url 생성 요청
class S3GeneratePresignedUrlReq:
    client_method: str = 'get_object'
    expiration: int = 36000
    bucket: str
    key: str

    def __init__(self, bucket: str, key: str):
        self.bucket = bucket
        self.key = key

    def to_json(self):
        return {
            "Bucket": self.bucket,
            "Key": self.key
        }
