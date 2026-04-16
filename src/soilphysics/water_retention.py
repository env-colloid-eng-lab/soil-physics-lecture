from __future__ import division

import numpy as np

CAMPBELL = 1
VAN_GENUCHTEN = 2
RESTRICTED_VG = 3
IPPISCH_VG = 4
CAMPBELL_IPPISCH_VG = 5


def Campbell(v, psi, theta):
    thetaS = v[0]
    he = v[1]
    Campbell_b = v[2]
    for i in range(len(psi)):
        if psi[i] <= he:
            theta[i] = thetaS
        else:
            se = (psi[i] / he) ** (-1.0 / Campbell_b)
            theta[i] = se * thetaS


def VanGenuchten(v, psi, theta):
    thetaS = v[0]
    VG_thetaR = v[1]
    VG_alpha = v[2]
    VG_n = v[3]
    VG_m = v[4]
    for i in range(len(psi)):
        se = 1.0 / pow(1.0 + pow(VG_alpha * psi[i], VG_n), VG_m)
        theta[i] = se * (thetaS - VG_thetaR) + VG_thetaR


def VanGenuchtenRestricted(v, psi, theta):
    thetaS = v[0]
    VG_thetaR = v[1]
    VG_alpha = v[2]
    VG_n = v[3]
    VG_m = 1.0 - (1.0 / VG_n)
    for i in range(len(psi)):
        if psi[i] <= 0:
            se = 0
        else:
            se = (1.0 + (VG_alpha * abs(psi[i])) ** VG_n) ** (-VG_m)
        theta[i] = se * (thetaS - VG_thetaR) + VG_thetaR


def IppischVanGenuchten(v, psi, theta):
    thetaS = v[0]
    VG_thetaR = v[1]
    he = v[2]
    VG_alpha = v[3]
    VG_n = v[4]
    VG_m = 1.0 - (1.0 / VG_n)
    VG_Sc = (1.0 + (VG_alpha * he) ** VG_n) ** VG_m
    for i in range(len(psi)):
        if psi[i] <= he:
            se = 1.0
        else:
            se = VG_Sc * (1.0 + (VG_alpha * abs(psi[i])) ** VG_n) ** (-VG_m)
        theta[i] = se * (thetaS - VG_thetaR) + VG_thetaR


def CampbellIppischVanGenuchten(v, psi, theta):
    thetaS = v[0]
    VG_thetaR = v[1]
    he = v[2]
    VG_alpha = v[3]
    VG_n = v[4]
    VG_m = 1.0 - (1.0 / VG_n)
    VG_Sc = (1.0 + (VG_alpha * he) ** VG_n) ** VG_m
    for i in range(len(psi)):
        if psi[i] <= he:
            se = 1.0
        else:
            se = VG_Sc * (1.0 + (VG_alpha * abs(psi[i])) ** VG_n) ** (-VG_m)
        residual = VG_thetaR * (1 - ((np.log(VG_alpha * psi[i] + 1.0) / np.log(VG_alpha * (10**6) + 1.0))))
        theta[i] = max(0.0, se * (thetaS - residual) + residual)
