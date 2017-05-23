from st2common.runners.base_action import Action

from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAction(Action):
    def __init__(self, config=None):
        super(SentimentAction, self).__init__(config=config)
        
    def run(self, sentence):
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)
        return ss['compound']
