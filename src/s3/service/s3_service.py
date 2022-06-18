from src.s3.domain.s3 import s3
from src.s3.domain.s3_generate_presigned_url_req import S3GeneratePresignedUrlReq


def generate_presigned_url(req: S3GeneratePresignedUrlReq):
    return s3.generate_presigned_url(
        req.client_method,
        Params=req.to_json(),
        ExpiresIn=req.expiration
    )
