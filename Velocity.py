import numpy as np 
import matplotlib.pylab as plt

t = np.arange(0, 20.25, 0.25) 

#  y0_Velocity  
y0 = [
         1.0000,         0.5898,        -0.3447,        -1.1247,        -1.1693,
        -0.4085,         0.6628,         1.3280,         1.1492,         0.2715,
        -0.6814,        -1.0471,        -0.5903,         0.3349,         1.0376,
         0.9823,         0.1705,        -0.8555,        -1.3908,        -1.0623,
        -0.0910,         0.8625,         1.1602,         0.6320,        -0.3095,
        -0.9645,        -0.8435,        -0.0154,         0.9387,         1.3350,
         0.8696,        -0.1642,        -1.0783,        -1.2693,        -0.6386,
         0.3426,         0.9685,         0.7977,        -0.0360,        -0.9193,
        -1.1948,        -0.6283,         0.4215,         1.2503,         1.3002,
         0.5491,        -0.4749,        -1.0658,        -0.8347,         0.0194,
         0.8546,         1.0428,         0.4172,        -0.6060,        -1.3179,
        -1.2143,        -0.3516,         0.6911,         1.2163,         0.8949,
        -0.0074,        -0.8218,        -0.9516,        -0.2954,         0.6804,
         1.2704,         1.0294,         0.0896,        -0.9279,        -1.3455,
        -0.9014,         0.0699,         0.8758,         0.9549,         0.2709,
        -0.6637,        -1.1524,        -0.8102,         0.1602,         1.1069,
         1.3833,
] 
#   y1_Velocity
y1 = [
        -1.0000,        -0.7640,        -0.2078,         0.3182,         0.5067,
         0.3021,        -0.0698,        -0.2711,        -0.0989,         0.3638,
         0.8024,         0.8903,         0.5215,        -0.1095,        -0.6364,
        -0.7697,        -0.4903,        -0.0538,         0.1970,         0.0776,
        -0.3072,        -0.6394,        -0.6180,        -0.1789,         0.4498,
         0.8988,         0.9083,         0.5040,        -0.0247,        -0.3294,
        -0.2452,         0.0998,         0.3827,         0.3235,        -0.1081,
        -0.6621,        -0.9777,        -0.8340,        -0.3049,         0.2889,
         0.5999,         0.4896,         0.1160,        -0.1876,        -0.1558,
         0.2153,         0.6623,         0.8401,         0.5690,        -0.0324,
        -0.6215,        -0.8631,        -0.6556,        -0.1939,         0.1735,
         0.1933,        -0.1153,        -0.4779,        -0.5654,        -0.2348,
         0.3599,         0.8665,         0.9745,         0.6278,         0.0620,
        -0.3608,        -0.4019,        -0.1077,         0.2332,         0.3027,
        -0.0129,        -0.5347,        -0.9120,        -0.8673,        -0.3928,
         0.2389,         0.6591,         0.6536,         0.3032,        -0.0827,
        -0.1917,
] 

plt.figure(figsize = (8, 4))
plt.subplots_adjust(bottom = 0.2, left = 0.2) 

plt.plot(t, y0, 'r-', label = r'$Point_0$', lw = 2)
plt.plot(t, y1, 'b--', label = r'$Point_1$', lw = 3) 

plt.xlabel(r'$Time(Sec)$').set_fontsize(16) 
plt.ylabel(r'$Amplitude$').set_fontsize(16)
plt.title("$***Time*and*Velocity***$").set_fontsize(16) 

plt.grid(axis = 'both') 
plt.legend(loc = 'best') 

plt.show(); 