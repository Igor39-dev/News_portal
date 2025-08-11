from django import template

register = template.Library()

BAD_WORDS = ['редиска', 'дурак', 'дурень']

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError()

    def replace_bad_word(word):
        for bad_word in BAD_WORDS:
            if word.lower().startswith(bad_word.lower()):
                stars = '*' * (len(word) - 1)
                return word[0] + stars
        return word


    words = value.split()
    censored_words = [replace_bad_word(w) for w in words]
    return ' '.join(censored_words)