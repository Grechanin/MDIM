import datetime
AWS_ACCESS_KEY_ID = "AKIAJHWWMV5UM4OHOLNQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'arthouse.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'arthouse.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'md1m-bucket-us'
S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}