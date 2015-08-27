import matplotlib
import pylab
from pylab import *
from matplotlib import pyplot as plt
from mpltools import style
from mpltools import layout
from StringIO import StringIO
def log_scatter_2(list1, list2,list3, list4, log_x_min, log_x_max, bound):


    plt.close()
    temp = zip(list1,list2)
    temp2 = zip(list3,list4)
    temp_filter = filter(lambda a: a[0] > bound and a[1] > bound , temp)
    temp2_filter = filter(lambda a: a[0] > bound and a[1] > bound , temp2)
    plt.figure(figsize=(8*1.2,6*1.2), dpi=80)
    plt.gca().set_xscale('log')
    plt.gca().set_yscale('log')
    plt.scatter(*zip(*temp_filter), alpha = 0.5, s = 150)
    plt.scatter(*zip(*temp2_filter), alpha = 0.4, color = 'red', s = 150)
    xlim(10**(-5), 10**9)
    ylim(10**(-5), 1.0)
    plt.xlabel('duplicity', fontsize = 20)
    plt.ylabel('N_devices', fontsize = 20)
    plt.tick_params(which='both', width=2, length = 4)
    plt.show()

def log_hist(list,log_x_min,log_x_max, N_bins, N_bins_2):


    bins = np.logspace(log_x_min,log_x_max, N_bins)
    bins_2 = np.logspace(log_x_min,log_x_max, N_bins_2)

    xscale('log')
    yscale('log')

    hist(list, bins = bins, log = True, alpha = 0.25)

    plt.rc("font", size=20)
    plt.xlabel('invites', fontsize = 20)
    plt.ylabel('threads', fontsize = 22)






