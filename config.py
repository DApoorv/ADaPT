# encoded in UTF-8
import datetime
from urllib.parse import quote
from flask import session


ENV = 'development'
DEBUG = True
TESTING = False
PROPAGATE_EXCEPTIONS = None
PRESERVE_CONTEXT_ON_EXCEPTION = None
# SECRET_KEY = 'MY_SECRET_KEY'
CLIENT_ID = 'ADAPT-Stage'
SECRET_KEY = '5IMzVQS7qc9gnT5Esg5Tx8qpEmDVLVSAlb6KH3V3KSl0v2LN'
REDIRECT_URL = 'https://ui-ara-adapt-iceberg.ara.decc.vmware.com/login'

#MinIO
# AWS-ec2
bucket_name = "adapttesting"
ip_address = '18.220.245.40:9000'
access_key = 'minioadmin'
secret_key = 'minioadmin'

# AWS-EKS-CLUSTER
# bucket_name = "adapttesting"
# ip_address = '192.168.29.107:9000'
# access_key = 'minio'
# secret_key = 'minio123'

mapping_sheet_path = "Unit Testing/Data Ingestion/Source-To-Target Column Mapping Sheet/"
log_path = "Unit Testing/Data Ingestion/logs/log.txt"

PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)
USE_X_SENDFILE = False
SERVER_NAME = None
APPLICATION_ROOT = '/'
SESSION_COOKIE_NAME = 'session'
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_PATH = None
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = None
SESSION_REFRESH_EACH_REQUEST = True
SESSION_PERMANENT = False
SESSION_TYPE = 'filesystem'
MAX_CONTENT_LENGTH = None
SEND_FILE_MAX_AGE_DEFAULT = None
TRAP_BAD_REQUEST_ERRORS = None
TRAP_HTTP_EXCEPTIONS = False
EXPLAIN_TEMPLATE_LOADING = False
PREFERRED_URL_SCHEME = 'http'
JSON_AS_ASCII = True
JSON_SORT_KEYS = True
JSONIFY_PRETTYPRINT_REGULAR = False
JSONIFY_MIMETYPE = 'application/json'
TEMPLATES_AUTO_RELOAD = None
MAX_COOKIE_SIZE = 4093
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Local
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:'+quote('1234')+'@localhost:5432/test_adapt_db'

# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:'+quote('adapt')+'@10.127.45.25:5432/adapt_db_ui'
# ARA DATABASE
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:'+quote('mysecretpassword')+'@10.168.3.214:5432/adapt_db_ui'
# LYRA DATABASE
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:'+quote('mysecretpassword')+'@10.182.224.124:5432/adapt_db_ui'
# AWS-ec2
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:'+quote('mysecretpassword')+'@192.168.49.2:30400/adapt_db_ui'
# AWS-EKS-CLUSTER
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:'+quote('postgres')+'@10.100.176.57:5432/adapt_db_ui'
SQLALCHEMY_ECHO = False
