#!/usr/bin/env python

import math

E_0 = 20.0
theta_degrees = 5.0
m_p = 0.938
E = 18.499
E_0_minus_E = E_0 - E
theta = math.radians(theta_degrees)
print(E_0, theta_degrees, m_p, E, E_0_minus_E, theta)
print(E_0_minus_E**2, 2*E_0_minus_E*m_p, E**2*math.sin(theta)**2, (E_0 - E*math.cos(theta))**2)
zero = E_0_minus_E**2 + 2*E_0_minus_E*m_p - E**2*math.sin(theta)**2 \
    - (E_0 - E*math.cos(theta))**2
print(zero)
exit
