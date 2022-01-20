import random


class FakeChatAI:
    sentences = []
    lookup = []
    level = 50

    def __init__(self, sentences, level=100):
        for s in sentences:
            lookup_value = 0
            for c in s[0]:
                lookup_value += ord(c)
            self.lookup.append(lookup_value)
            self.sentences.append(s[1])
        self.level = 50

    def add(self, sentences):
        for s in sentences:
            lookup_value = 0
            for c in s[0]:
                lookup_value += ord(c)
            self.lookup.append(lookup_value)
            self.sentences.append(s[1])

    def get(self):
        return self.sentences

    def reset(self):
        self.lookup = []
        self.sentences = []

    def chat(self, input):
        if not self.sentences:
            return
        lookup_value = 0
        for c in input:
            lookup_value += ord(c)
        output = []
        for (i, j) in zip(self.lookup, self.sentences):
            if abs(i-lookup_value) <= self.level:
                if type(j) in (list, tuple):
                    for k in j:
                        output.append(k)
                else:
                    output.append(j)
        if output != []:
            return random.choice(output)
        else:
            a = [abs(lookup_value-i) for i in self.lookup]
            r = self.sentences[a.index(min(a))]
            if type(r) == str:
                return r
            else:
                return random.choice(r)

fake_chat_ai = FakeChatAI([
    ('Hello', ('Hello!', 'Hi~')),
    ('What\'s you name?', ('Fake', 'My name is Fake.')),
    ('F*ck', ('be civilized, please.', 'F*ck')),
    ('What\'s the weather like today?', 'It\'s Ok.')
])

def be_civilied(sentence, civilized_words=None, level=0.5):
    if civilized_words == None:
        civilized_words = ['f*ck', 'b*tch', 'd*mmit']
    words = {}
    for cw in civilized_words:
        l = len(cw)
        if not words.get(l, None):
            words[l] = [cw]
        else:
            words[l].append(cw)
    wordlist = sentence.split(' ')
    r = []
    for w in wordlist:
        if words.get(len(w), None):
            if random.random() <= level:
                r.append(random.choice(words[len(w)]))
                continue
        r.append(w)
    return ' '.join(r)
