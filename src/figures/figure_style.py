"""
Setting style for figures
"""
import matplotlib as mpl
import seaborn as sns

def set_style():
    sns.set_style('ticks')

    sns.set_context('poster')
    font = {
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial'],
         # 'text.usetex': False,
         'font.size': 30,
         'ytick.labelsize':15,
         'xtick.labelsize':15,
         # 'title.labelsize':20,
         'legend.fontsize':20,
         'axes.labelsize':30 
    }
    mpl.rcParams.update(font)
    # mpl.rc('font', **)
