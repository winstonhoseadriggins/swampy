from math import *
from unum.units import *
from unum import Unum

import unum.units
print dir(unum.units)

# Example 1-3 on page 11 of Wolfson and Pasachoff

Me = 5.97e24 * KG
T = 8.64e4 * S
Re = 6.37e6 * M
G = 6.67e-11 * N*M**2/KG**2

rad = G * Me * T**2 / 4 / pi**2

alt = pow(rad.asNumber(M**3), 1.0/3.0) * M - Re
print alt

# Example 2-2 on page 24 of Wolfson and Pasachoff

KM   = Unum.unit('km' , 1000 * M )
dx = 1000 * KM
dt = 4 * H

dxdt = dx/dt
print dxdt
print dxdt.as(M/S)

# Example 2-5 on page 24 of Wolfson and Pasachoff

v0 = 270 * KM / H
a = 4.5 * M / S**2

x = -v0**2 / 2 / a
print x




