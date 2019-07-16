import os

mysql_host = os.environ.get("DB_HOST", default="localhost")
mysql_user = os.environ.get("DB_USER", default="root")
mysql_password = os.environ.get("DB_PSW", default="root")
mysql_schema = os.environ.get("DB_SCHEMA", default="ac")

csrf_key = os.environ.get("CSRF_KEY", default="5xccudQfRA3Pc6Hx")

ssl_cn = os.environ.get("SSL_CN", default="ac-flask-demo.me")
host = os.environ.get("HTTPS_HOST", default="0.0.0.0")
port = os.environ.get("HTTPS_PORT", default=443)
debug = os.environ.get("IS_DEBUG", default=True)
ssl_context = (os.environ.get("SSL_PUB", default='cert.pem'), os.environ.get("SSL_PRIV", default='key.pem'))

token_expired = float(os.environ.get("TOKEN_EXPIRED", default=600))

storage_path = os.environ.get("STORAGE_PATH", default="storage/")

allowed_file_suffix_list = tuple(os.environ.get("ALLOWED_SUFFIX", default="'jpg', 'jpeg', 'png', 'bmp', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx'").replace("'", "").replace(" ", "").split(','))

nacl_sk_path = os.environ.get("NACL_SK_PATH", default="config/nacl_sk")
