# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:29:15 2024

@author: q664377
"""
import os
from graphviz import Digraph

g = Digraph('Trailer')
g.node('k')
g.node('m')
g.node('y0', label='<y<sub>0</sub>>')
g.node('omega', label='<&omega;>')
g.node('v')
g.node('L')
g.node('X')
g.edge('v', 'omega')
g.edge('L', 'omega')
g.edge('y0', 'X')
g.edge('omega', 'X')
g.edge('k', 'X')
g.edge('m', 'X')
#g.render('trailer_g', format='png')