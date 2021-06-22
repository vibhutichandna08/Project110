import pandas as p
import statistics as s
import random
import plotly.figure_factory as pf

df = p.read_csv('Project110_data.csv')
data = df['reading_time'].tolist()
popMean = s.mean(data)


def randomsetofmean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data))
        value = data[randomIndex]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean


def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = randomsetofmean(30)
        mean_list.append(set_of_means)
    plot_graph(mean_list)


def plot_graph(meanlist):
    fig = pf.create_distplot([meanlist], ['reading_time'], show_hist=False)
    fig.show()


setup()
