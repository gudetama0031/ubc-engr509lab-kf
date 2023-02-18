import numpy as np
from tracking_1d import simulator_1d

class KalmanFilter:
    def __init__(self):
        self.v = 0.
        self.prev_t = 0.
        # Initial State Vector [[position], [velocity]]
        self.x = [0.]
        # Uncertainity Matrix
        self.SIGMA = [0.]
        self.R = [0.]
        # State Transition Matrix [[1., dt],
        #                          [0., 1.]]
        self.A = [0.]
        # Observation Matrix
        self.C = [0.]
        # Measurement Uncertainty
        self.Q = [0.]
        # Identity Matrix [[1., 0.],
        #                  [0., 1.]]
        self.I = [0.]

    def predict(self, t):
        dt = t - self.prev_t

        return

    def measure_and_update(self, measurements, t):

        return


# Simulator options.
options = {}
options['FIG_SIZE'] = [8, 8]
options['CONSTANT_SPEED'] = False
options["sensor_noise_variance"] = 0.3 

simulator_1d(options, KalmanFilter)
