import thulac
import re

class Token(object):

    def __init__(self,
        word,
        part_of_speech=None,
        **kwargs):
        self.word = word
        self.part_of_speech = part_of_speech

    def __str__(self):
        return self.word + "/" + self.part_of_speech

    def __eq__(self, other):
        return self.word == other.word

    def __hash__(self):
        return self.word.__hash__()

class Preprocess(object):

    def __init__(self, **kwargs):
        self._tokenizer = thulac.thulac(**kwargs)

    def tokenize(self, document : str) -> list:
        document = self.clean(document)
        tokenizer_result = self._tokenizer.cut(document, False)
        tokens = []
        for token_info in tokenizer_result:
            token = Token(token_info[0],
                          part_of_speech=token_info[1])
            # token_info: [word, part_of_speech]
            tokens.append(token)

        return tokens

    def clean(self, document : str) -> str:
        document = re.sub(r"\s+", "；", document)

        return document