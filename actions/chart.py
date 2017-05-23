import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
import os
from st2common.content import utils
from st2common.runners.base_action import Action


class SentimentAction(Action):
    def __init__(self, config=None):
        super(SentimentAction, self).__init__(config=config)

    def run(self, top):
        path = os.path.join(utils.get_system_packs_base_path(), 'panic_room', 'actions', 'traffic_data.json')
        with open(path, 'r') as traffic_data:
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