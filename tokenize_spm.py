import sentencepiece,os

# train.txtのファイルは著作権上公開できないので、ご自身で喘ぎ声を収集していただく必要があります。
def main(vocab_size):
    txt_for_training = "train.txt"
    if not os.path.exists("./model"):os.mkdir("./model")
    sentencepiece.SentencePieceTrainer.train(input=txt_for_training, model_prefix=f'./model/m{vocab_size}', vocab_size=vocab_size, user_defined_symbols=['<protag>', '<heroine>'])
    
if __name__ == '__main__':
    # main(2000)
    main(25000)
            