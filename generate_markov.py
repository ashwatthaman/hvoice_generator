import markovify
import json,codecs

def load_markov():
    jdict = json.load(codecs.open("./model/markov.model",encoding="utf-8"))    
    model = markovify.NewlineText.from_dict(jdict)
    return model

def generate_markov():
    text_model = load_markov()
    
    for _ in range(10):
        output1 = text_model.make_sentence_with_start(beginning="▁「 じゅるっ",strict=False)
        print(output1.replace(" ","").replace("▁",""))
    for _ in range(10):
        output2 = text_model.make_sentence_with_start(beginning="▁「 ちゅぱ",strict=False)
        print(output2.replace(" ","").replace("▁",""))
    for _ in range(10):
        output3 = text_model.make_sentence_with_start(beginning="▁「 ちゅぱっ",strict=False)
        print(output3.replace(" ","").replace("▁",""))



if __name__=="__main__":
    generate_markov()