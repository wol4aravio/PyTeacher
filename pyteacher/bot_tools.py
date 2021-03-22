def parse_register_message(message):
    url = None
    for word in message.split(" "):
        if "https://github.com" in word:
            url = word
            break
    return url
