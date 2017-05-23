import matplotlib.pyplot as plt
import json

from st2common.runners.base_action import Action

from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAction(Action):
    def __init__(self, config=None):
        super(SentimentAction, self).__init__(config=config)

    def run(self, top):
        with open('traffic_data.json', 'r') as traffic_data:
            data = json.load(traffic_data)

        data.sort(key=lambda x: x['sent'])
        data = data[:top]

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = [item['destination'] for item in data]
        sizes = [item['sent'] for item in data]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # plt.show()
        plt.savefig('/opt/stackstorm/static/webui/img/output.png')