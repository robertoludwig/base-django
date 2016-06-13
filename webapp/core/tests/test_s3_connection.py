import unittest
import boto
from webapp import settings


class TestS3Connection(unittest.TestCase):
    def setUp(self):
        self.s3 = boto.connect_s3(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            calling_format=boto.s3.connection.OrdinaryCallingFormat(),
        )

        self.bucket = self.s3.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)

    def tearDown(self):
        pass

    def test_connection(self):
        assert self.s3 is not None

        # must be a better way to ensure connection works
        bucket = boto.s3.bucket.Bucket(connection=self.s3, name=settings.AWS_STORAGE_BUCKET_NAME)
        all_keys = bucket.get_all_keys()
        assert len(all_keys) == 1