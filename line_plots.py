"""Helper functions for creating line plots"""

import matplotlib.pyplot as plt
import numpy as np

"""Set text sizes"""
SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

def line_plot_compare(x_mat, title_list, x_label_list, # total size must be the number of unique entries in subplot_list
                      overall_title,
                      y_mat, y_label_list, # all have the same length
                      subplot_list, # entries with the same number get plotted on the same subplot
                      subplot_shape, # total size must be the number of unique entries in subplot_list
                      save_path='fig.png',
                      add_legend=True,
                      linewidth=2,
                      subplot_height=5,
                      subplot_width=5,
                      ):
    plt.figure()
    plt.title(overall_title)
    fig, ax = plt.subplots(subplot_shape[0], subplot_shape[1], 
                   figsize = (subplot_width*subplot_shape[0], subplot_height*subplot_shape[1]))
    
    for plot in range(subplot_shape.size):
        
        ax[plot].axis('square')
        # ax[plot].set_xlim((-50, 50))
        # ax[plot].set_ylim((-50, 50))
        # ax[plot].set_xticks(range(20))
        # ax[plot].set_yticks(range(20))
        ax[plot].xlabel(x_label_list[plot])
        ax[plot].title(title_list[plot])
        
        # ax[plot].axis('off')
        ax[plot].tick_params(which='both',      # both major and minor ticks are affected
                             bottom=True,      # ticks along the bottom edge are off
                             top=False,         # ticks along the top edge are off
                             right=False,
                             left=True,
                             labelleft=False,
                             labelright=False,
                             labelbottom=False) # labels along the bottom edge are off  
        
        for line in np.nonzero(subplot_list==plot)[0]:

            ax[plot].subplot(x_mat[plot],y_mat[line], 
                             'r', 
                             label=y_label_list[line],
                             linewidth=linewidth,
                             linestyle='-',
                             title=title_list[line])
    
        if add_legend:
            ax[plot].legend()

    plt.savefig(save_path, bbox_inches='tight',dpi=600, pad_inches=0.0)
