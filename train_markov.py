import sys,codecs
import zenhan,json
import sentencepiece
import markovify

def to_json(text_model):
    def chain_to_json(chain):
        """
        Dump the model as a JSON object, for loading later.
        """
        return json.dumps(list(chain.model.items()),ensure_ascii=False)
    return {
        "state_size": text_model.state_size,
        "chain": chain_to_json(text_model.chain),
        "parsed_sentences": text_model.parsed_sentences if text_model.retain_original else None,
    }


def train_markovify(fr,sp,n_vocab):
    import json
    del_letter = lambda s:s.replace("、","")
    text = "\n".join([" ".join([word for word in sp.encode(del_letter(line).strip(),out_type=str)]) for line in fr.readlines()])
    text_model = markovify.NewlineText(text, state_size=2,well_formed=False,retain_original=False)

    model_json = to_json(text_model)
    jsonw = codecs.open("./model/markov.model","w",encoding="utf-8")
    jsonw.write(json.dumps(model_json,ensure_ascii=False))
    jsonw.close()


# train.txtのファイルは著作権上公開できないので、ご自身で喘ぎ声を収集していただく必要があります。
def main(vocab_size):
    txt_for_training = "train.txt"
    sp = sentencepiece.SentencePieceProcessor(model_file=f'./model/m{vocab_size}.model')
    fr = codecs.open(txt_for_training)
    train_markovify(fr,sp,vocab_size)

if __name__ == '__main__':
    # main(2000)
    main(25000)
            