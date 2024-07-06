import re

def replace_token(blob):
    # Регулярное выражение для поиска строки с токеном
    token_pattern = re.compile(rb'bot = Bot\(token="[^"]+"\)')
    # Замена строки с токеном на пустую строку
    return token_pattern.sub(b'bot = Bot(token="REMOVED")', blob)

FILTERS = {
    'blob_callback': replace_token,
}