import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import time

global df

fig = plt.gcf()
fig.show()
fig.canvas.draw()


def refresh_df():
    file_name = 'acc_wh492789.csv'
    path = '/media/pi/DATA/Sensehat/data/'
    global df
    df = pd.read_csv(path+file_name, sep=',', header=None,
                     names=['t', 'acc_x', 'acc_y', 'acc_z', 'humidity',
                            'temp_from_hum', 'temp_from_pressure',
                            'pressure', 'compass_x', 'compass_y', 'compass_z',
                            'gyro_x', 'gyro_y', 'gyro_z'], decimal=".")


def create_plot_without_error(x, y, x_label, y_label):
    """
    Creates a plot of the data.
    Data must be in df['...'] format.
    :param x:
    :param y:
    :return:
    """
    plt.plot(x, y, '.', color="#ff0000", ms=1)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def multi_plot_live():
    dot_width = 1
    
    t = df['t']
    x1 = df['acc_x']
    x2 = df['acc_y']
    x3 = df['acc_z']
    x4 = df['gyro_x']
    x5 = df['gyro_y']
    x6 = df['gyro_z']

    plt.subplot(2, 3, 1)  # nrows, ncols, plot_number
    plt.plot(t, x1, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('acc_x')

    plt.subplot(2, 3, 2)  # nrows, ncols, plot_number
    plt.plot(t, x2, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('acc_y')

    plt.subplot(2, 3, 3)  # nrows, ncols, plot_number
    plt.plot(t, x3, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('acc_z')
    
    #Comp
    plt.subplot(2, 3, 4)  # nrows, ncols, plot_number
    plt.plot(t, x4, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('gyro_x')
    
    plt.subplot(2, 3, 5)  # nrows, ncols, plot_number
    plt.plot(t, x5, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('gyro_y')
    
    plt.subplot(2, 3, 6)  # nrows, ncols, plot_number
    plt.plot(t, x6, '.', color="#ff0000", ms=dot_width)
    plt.ylabel('gyro_z')


def plot_3d():
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['acc_x'], df['acc_y'], df['acc_z'], c='r', marker='o')


plot_history = -500 # mount of latest datapoints to plot in fig

# plt.clf() clears figure but keeps window open
while True:
    tstart = time.time()
    refresh_df()
    df = df.iloc[plot_history:]
    plt.clf()
    
    #multi_plot_live()
    create_plot_without_error(df['t'], df['pressure'], 'x', 'y')

    plt.tight_layout()
    fig.canvas.draw()
    print('FPS: ', (time.time()-tstart))
    




