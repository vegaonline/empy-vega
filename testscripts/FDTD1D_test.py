""" Testing FDTD 1D
"""
from __future__ import print_function
from __future__ import absolute_import

from builtins import zip
from builtins import str
from builtins import range
from builtins import object

import scipy
import matplotlib
import bases
from solvers.FDTD.FDTD1D import FDTD1D

__author__ = 'Abhijit Bhattacharyya'

ngridx = 400
ex = scipy.zeros(ngridx, dtype = float)
hy = scipy.zeros(ngridx, dtype = float)

centreProbSpace = 0.5 * ngridx
centrePulseInc = 40.0
pulseSpread = 12.0
numSteps = 1
plotOK = 1

FDTD1DObj = FDTD1D('FDTD1D', ex, hy, ngridx, centrePulseInc, pulseSpread, centreProbSpace, numSteps, plotOK)
FDTD1Dobj.computeFDTD1D()