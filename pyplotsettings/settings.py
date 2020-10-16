import matplotlib

font = {'family' : 'Times New Roman',
        'weight' : 'light',
        'size'   : 18}	
matplotlib.rc('font', **font)
params = {'legend.fontsize': 20,
        'figure.figsize': (9, 6),
        'axes.labelsize': 20,
        'axes.titlesize': 20,
        'xtick.labelsize': 18,
        'ytick.labelsize': 18}
matplotlib.rcParams.update(params)
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Times New Roman'
matplotlib.rcParams['axes.formatter.useoffset'] = False
matplotlib.rcParams['lines.linewidth'] = 3