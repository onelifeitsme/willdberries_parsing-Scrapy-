def text_clear(text):
    text = text.replace('\u00a0', '').replace('\u20bd', '').strip()
    return text

