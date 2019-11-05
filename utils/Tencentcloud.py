import hmac
import hashlib

sha1_http_string = hashlib.sha1('ExampleHttpString'.encode('utf-8')).hexdigest()

sign_key = hmac.new('YourSecretKey'.encode('utf-8'), 'ExampleKeyTime'.encode('utf-8'), hashlib.sha1).hexdigest()
print(sign_key, sha1_http_string)