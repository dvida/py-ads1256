from __future__ import print_function, division

import ads1256
import time,random

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Initializes the ADC using py-ads1256 library function 
# First argument: GAIN. The second: SPS
# Possible settings:
# GAIN values:  1,  2,  4,  8,  16,  32,  64
# SPS values:   2d5,  5,  10,  15,  25,  30,  50,  60,  100,  
# SPS values:   500, 1000,  2000,  3750,  7500,  15000,  30000
ads1256.start("1","30000")

channel = 0
n_samples = 5000

# Performs the reading of ADC channel 0
time_prev = time.time()
first_time = time_prev

values = []
times = []
time_diffs = []

for i in range(n_samples):
		
		
    # For some reason 8 values are repeated, so take only one
        
    # Read the channel
    value = ads1256.read_channel(channel)
    
    time_ms = ((time.time()-time_prev)*1000)
    time_prev = time.time()
    time_diffs.append(time_ms)
    
    # Add the value read from the ADC
    values.append(value)
    
    # Add the UNIX timestamp
    times.append(time.time())
    

#print(zip(times, values))
print("SPS:", n_samples/(time.time() - first_time))

plt.plot(np.array(times) - first_time, values, marker='+')
plt.xlabel('UNIX timestamp (s)')
plt.ylabel('ADU')
plt.ylim(0, 2**23)
plt.show()



# Stop the ADC
ads1256.stop()
