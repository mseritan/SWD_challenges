#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:53:07 2022

@author: megankelley
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('fossil_fuel_subsidies.txt')
years = data[:, 0]
oil = data[:, 1]
electricity = data[:, 2]
natural_gas = data[:, 3]
coal = data[:, 4]
total = data[:, 5]

plt.stackplot(years, electricity, natural_gas, coal, oil)
plt.show()