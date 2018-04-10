###THIS IS THE INPUT DATA#######
# simulation settings
POP_SIZE=2000
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1       # years. Don't know if I'm supposed to change this????
PSA_ON = False      #dont think i need sens analysis here. 


# the transition probability matrix
Q3_TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # well
    [0.0,   0.0,    1.0,    0.0],   # stroke state
    [0.0,   0.25,   0.55,   0.2],   # PS
    [0.0,   0.0,    0.0,    1.00] #death
    ]

# New Matrix in the second state
ADJ_TRANS_MATRIX = [
    [0.75, 0.15, 0.0, 0.1],   # well
    [0.0,  0.0,  1.0, 0.0],   # stroke
    [0.0,  0.1625, 0.701, 0.1365],   # PS
    [0.0,  0.0,    0.0,   1.0] #death
    ]
