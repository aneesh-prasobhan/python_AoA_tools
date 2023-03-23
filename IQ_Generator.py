import numpy as np
import pandas as pd

# Script to Generate IQ Data with moving angle (0 - 360 degrees)
antenna_dist = 0.035  # Enter the Antenna Distance %%
signal_freq1 = 250000  # Enter Antenna 1 Signal frequency after down conversion
signal_freq2 = 250000  # Enter Antenna 1 Signal frequency after down conversion
sampling_rate = 4000000  # Sampling Rate of ADC %% Other algorithm only supports 4 MHz
mag1 = 400  # Antenna 1 Signal Amplitude %%
mag2 = 400  # Antenna 2 Signal Amplitude %%

# Loop for Moving Angle Begins
j = 1
In = []
Qn = []
for main_angle in range(0, 181, 10):

    # Phase shift calculation
    ch = 17
    lambda_ = 0.1229  # Channel 17 (midpoint) with freq 2440 MHz; Lambda for Channel 0 is 0.1247
    phase_shift = ((np.cos(np.radians(main_angle)) * 360 * antenna_dist) / lambda_)  # angle is 0, phase is 102.5224 % angle is 180, phase is  -102.5224

    # Antenna 1 IQ Generation
    angle_step1 = (360 / (sampling_rate / signal_freq1))
    start_angle1 = -360
    steps = 624
    end_angle1 = start_angle1 + ((steps - 1) * -1 * angle_step1)  # -1 for the clockwise rotation of the phasor
    angle_steps1 = np.linspace(start_angle1, end_angle1, steps)  # start angle, end angle, steps. (-360,-10350,1000)...using formula an=a+(n-1)*d
    angle1 = np.remainder(angle_steps1, 360)
    I1_all = mag1 * np.cos(np.radians(angle1))  # Polar to cartesian conversion for I
    Q1_all = mag1 * np.sin(np.radians(angle1))  # Polar to cartesian conversion for Q

    # Antenna 2 IQ Generation
    angle_step2 = (360 / (sampling_rate / signal_freq2))
    start_angle2 = start_angle1 - phase_shift
    steps = 624
    end_angle2 = start_angle2 + ((steps - 1) * -1 * angle_step2)  # -1 for the clockwise rotation of the phasor
    angle_steps2 = np.linspace(start_angle2, end_angle2, steps)  # start angle, end angle, steps. using formula an=a+(n-1)*d
    angle2 = np.remainder(angle_steps2, 360)
    I2_all = mag2 * np.cos(np.radians(angle2))
    Q2_all = mag2 * np.sin(np.radians(angle2))

    # Arranging the IQ Data from both antennas into BLE 5.1 standard
    # First 32 samples are reference from Antenna 1 (TI bug, BLE says frm Ant 2)
    I = np.zeros(180)
    Q = np.zeros(180)

    I[:32] = I1_all[:32]
    Q[:32] = Q1_all[:32]

    # Antenna 1 Data from Switching Slots
    I[32::8] = I1_all[44::32]
    I[33::8] = I1_all[45::32]
    I[34::8] = I1_all[46::32]
    I[35::8] = I1_all[47::32]

    Q[32::8] = Q1_all[44::32]
    Q[33::8] = Q1_all[45::32]
    Q[34::8] = Q1_all[46::32]
    Q[35::8] = Q1_all[47::32]

    # Antenna 2 Data from Switching Slots
    I[36::8] = I2_all[60::32]
    I[37::8] = I2_all[61::32]
    I[38::8] = I2_all[62::32]
    I[39::8] = I2_all[63::32]

    Q[36::8] = Q2_all[60::32]
    Q[37::8] = Q2_all[61::32]
    Q[38::8] = Q2_all[62::32]
    Q[39::8] = Q2_all[63::32]

    In.extend(I)
    Qn.extend(Q)

    j += 180

In = np.array(In)
Qn = np.array(Qn)

num_elem = len(In)

# Creating channel array
channel = np.zeros(num_elem) + ch
null_columns = np.zeros(num_elem)

# CSV write
data = pd.DataFrame({'identifier': null_columns, 'pkt': null_columns, 'sample_idx': null_columns,
                     'rssi': null_columns, 'ant_array': null_columns, 'channel': channel,
                     'i': In, 'q': Qn})
data.to_csv('Python_Generated_IQ_Data_0_180.csv', index=False)
