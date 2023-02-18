import numpy as np
from tracking_2d import simulator_2d

# Simulator options.
options = {}
options['FIG_SIZE'] = [8, 8]

options['DRIVE_IN_CIRCLE'] = False
# If False, measurements will be pos_x,pos_y.
# If True, measurements will be pos_x, pos_y, and current angle of the car.

# Required if driving in circle.
options['MEASURE_ANGLE'] = False
options['CONTROL_INPUTS'] = False


class KalmanFilter:
    def __init__(self):
        self.prev_t = 0
        # Initial State Vector [[pos_x], [pos_y], [velocity_x], [velocity_y]]
        self.x = [0.]
        # Uncertainty Matrix
        self.SIGMA = [0.]
        self. R = [0.]
        # State Transition Matrix
        self.A = [0.]

        # Observation Matrix
        self.C = [0.]

        # Measurement Uncertainty
        self.Q = [0.]

        # Identity Matrix
        self.I = np.eye(4,)

    def predict(self, t):
        # Calculate dt.
        # Put dt into the state transition matrix.
        dt = t - self.prev_t
        return

    def update(self, measurements, t):
        self.x = [0.]
        return [self.x[0], self.x[1]]

    # Required if driving in circle.
    def control_inputs(self, u_steer, u_pedal):
        return


simulator_2d(options, KalmanFilter)
