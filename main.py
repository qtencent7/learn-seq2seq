chat_list = [
    {"question": "It’s time to get up", "answer": "Get up soon"},
    {"question": "I usually sleep late on Saturdays", "answer": "Hurry up"},
    {"question": "It’s still early", "answer": "Did the alarm go off"}
]
# to do continue

def generate_dict(corpus):
    dictionary = None
    dictSet = set()
    for dict in corpus:
        questionArr = dict['question'].split()
        answerArr = dict['answer'].split()
        for word in questionArr:
            dictSet.add(word)
        for word in answerArr:
            dictSet.add(word)
    dictionary = list(dictSet)
    return dictionary

STOP_WORDS = {
    "PAD": "<PAD>",
    "SOS": "<SOS>",
    "EOS": "<EOS>"
}
if __name__ == "__main__":
    dict = generate_dict(chat_list)
    for key in STOP_WORDS:
        dict.append(STOP_WORDS[key])
