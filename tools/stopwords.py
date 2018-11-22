from tools.preprocess import Token

class ListStopWords(object):

    def __init__(self, stop_word_file):
        stop_words_set = open(stop_word_file, "r", encoding="utf-8").read().split('\n')
        self.stop_words_set = set([x.strip() for x in stop_words_set if len(x.strip()) > 0])

    def get_judger(self, rules=None):
        def with_rules(token : Token):
            return token.word in self.stop_words_set or rules(token)

        if rules is None:
            return lambda t : t.word in self.stop_words_set
        else:
            return with_rules