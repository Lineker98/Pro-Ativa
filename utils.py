import re

def get_sentiment(arquivo: str) -> list:

    sentiment_rate = []
    with open(arquivo, 'r', encoding='utf-8') as arq:
        frases = arq.readlines()
        for i in range(len(frases)):
            frase = re.sub(r"\s+", "", frases[i])
            positive = int(frase[-3])
            negative = int(frase[-2::])
            sentiment_rate.append((positive, negative))
            
    return sentiment_rate

def make_corpus(text: list) -> list:

  for i in range(len(text)):

    if type(text[i]) is not str:
      text[i] = ""

    if type(text[i]) == str:
      text[i] = text[i].replace(" ", "").replace("/","").replace(";", " ").replace(".", "").replace("(","").replace(")","")
    
  return text
