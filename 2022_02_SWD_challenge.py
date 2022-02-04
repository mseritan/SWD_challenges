#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:53:07 2022

@author: megankelley
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.patches as mplpatches

plt.style.use('plotstyle.mplstyle')

#%% Data

data = np.loadtxt('fossil_fuel_subsidies.txt')
years = data[:, 0]
oil = data[:, 1]
electricity = data[:, 2]
natural_gas = data[:, 3]
coal = data[:, 4]
total = data[:, 5]

oil_fraction = oil / total
electricity_fraction = electricity / total
natural_gas_fraction = natural_gas / total
coal_fraction = coal / total

sources = [oil, electricity, natural_gas, coal]
max_height = np.max(oil)

#%% Set up figure

fig_height = 6 # inches
fig_width = 11 # inches

plt.figure(figsize = (fig_width, fig_height))

margin = 1.0 # inches
panel1_width = fig_width - (2.0 * margin)
panel1_height =  fig_height - (2.0 * margin)

rel_panel1_width = panel1_width / fig_width
rel_panel1_height = panel1_height / fig_height

panel1 = plt.axes([margin / fig_width,
                  margin / fig_height,
                  rel_panel1_width,
                  rel_panel1_height],
                  frameon = True)
panel1.tick_params(bottom = True, labelbottom = True,
                   left = False, labelleft = False,
                   right = False, labelright = False,
                   top = False, labeltop = False)

panel1.set_xlim(years[0] - 0.5, years[-1] + 1)
# panel1.set_xticks([])
# panel1.set_xticklabels([])

panel1.set_ylim(0, 1.1 * max_height)
# panel1.set_yticks([])
# panel1.set_yticklabels([])

#%% Plot bars

oil_color = 'gold'
electricity_color = 'paleturquoise'
natural_gas_color = 'thistle'
coal_color = 'darkgray'
colors = [oil_color, electricity_color, natural_gas_color, coal_color]
rec_width = 0.15

for i in range(len(sources)):
    source_data = sources[i]
    for j in range(len(years)):
        year = years[j]
        rec_height = source_data[j]
        rectangle = mplpatches.Rectangle([year + (i * rec_width), 0],
                                  rec_width,
                                  rec_height,
                                  facecolor = colors[i],
                                  linewidth = 0)
        panel1.add_patch(rectangle)

#%% Save figure

plt.savefig('2022_02_SWD_challenge.png', dpi = 300)
plt.show()