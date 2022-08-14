# hvoice_generator

C100で発表した同人誌pythia R18の喘ぎ声生成用コードです。

pythonのバージョンは3.8.3です。

sentencepieceをインストール必要があります。

sentencepiece==0.1.91

で動作確認しました。

pip install sentencepiece==0.1.91

でインストールできます。

1. tokenize_spm.py

Tokenizer（分割器）の学習を行います。

2. train_markov.py

でマルコフモデルの学習を行います。

1と2に使うtrain.txtは著作権上公開が難しいので一部の例だけを載せています。

うまく加工できたら後ほど公開したいと思います。

3. generate_markov.py

学習したマルコフモデルから喘ぎ声を生成します。

喘ぎ声テキストで学習したモデルは./model/markov.modelにあるため、
生成するだけであれば、3.だけで実行することができます。