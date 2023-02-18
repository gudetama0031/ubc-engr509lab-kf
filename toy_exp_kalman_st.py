import numpy as np
from tracking_1d import simulator_1d

# Simulator options.
options = {}
options['FIG_SIZE'] = [8, 8]
options['CONSTANT_SPEED'] = False
options["sensor_noise_variance"] = 0.


class KalmanFilterToy:
    def __init__(self):
        self.v = 0.  # velocity estimate
        self.prev_pos = 0.
        self.prev_t = 0.

    def predict(self, t):
        """predict position"""
        predict_pos = 0.
        return predict_pos


    def measure_and_update(self, measure_pos, t):
        """estimate velocity"""
        return

simulator_1d(options, KalmanFilterToy)



