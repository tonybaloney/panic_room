import matplotlib.pyplot as plt
import json

with open('traffic_data.json', 'r') as traffic_data:
    data = json.load(traffic_data)

data.sort(key=lambda x: x['sent'])
data = data[:10]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = [item['destination'] for item in data]
sizes = [item['sent'] for item in data]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()
plt.savefig('/opt/stackstorm/static/webui/img/output.png')