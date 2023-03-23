def lambda_calculation(channel_data):
    # Channel vs Frequency lookup table
    channel_frequency = [2404, 2406, 2408, 2410, 2412, 2414, 2416, 2418,
                          2420, 2422, 2424, 2428, 2430, 2432, 2434, 2436,
                            2438, 2440, 2442, 2444, 2446, 2448, 2450, 2452,
                              2454, 2456, 2458, 2460, 2462, 2464, 2466, 2468,
                                2470, 2472, 2474, 2476, 2478, 2402, 2426, 2480]

    wavelength = 299792458 / ((channel_frequency[channel_data])*1000000) # speed of light / frequency
    print("Channel = %d", channel_data)
    print("Wavelength in m = %f", wavelength)
    return wavelength


def lambda_calculation_optimized(channel_data):
    # Precomputed wavelength dictionary
    channel_wavelength = {
        0: 0.12470568136439268,
        1: 0.12460201911886949,
        2: 0.12449852906976744,
        3: 0.12439521078838174,
        4: 0.12429206384742952,
        5: 0.12418908782104392,
        6: 0.12408628228476822,
        7: 0.12398364681555005,
        8: 0.12388118099173553,
        9: 0.12377888439306359,
        10: 0.12367675660066006,
        11: 0.1234730057660626,
        12: 0.12337138189300412,
        13: 0.12326992516447369,
        14: 0.123168635168447,
        15: 0.12306751149425288,
        16: 0.12296655373256768,
        17: 0.12286576147540984,
        18: 0.12276513431613431,
        19: 0.12266467184942717,
        20: 0.12256437367130008,
        21: 0.12246423937908497,
        22: 0.12236426857142857,
        23: 0.12226446084828711,
        24: 0.12216481581092095,
        25: 0.12206533306188926,
        26: 0.12196601220504476,
        27: 0.12186685284552845,
        28: 0.12176785458976441,
        29: 0.12166901704545455,
        30: 0.12157033982157339,
        31: 0.12147182252836304,
        32: 0.12137346477732794,
        33: 0.12127526618122977,
        34: 0.12117722635408246,
        35: 0.12107934491114701,
        36: 0.12098162146892655,
        37: 0.1248095162364696,
        38: 0.12357479719703215,
        39: 0.12088405564516129
    }

    # Get the precomputed wavelength for the given channel
    wavelength = channel_wavelength[channel_data]
    print("Channel = %d", channel_data)
    print("Wavelength in m = %f", wavelength)
    return wavelength


# Loop through the channels and calculate the wavelength
for i in range(0, 40):
    pp = lambda_calculation(i)
    ff = lambda_calculation_optimized(i)
    if pp == ff:
        print("Wavelengths are equal")
    else:
        print("NOOOOOOOOOOOOOOOOOOOOO")