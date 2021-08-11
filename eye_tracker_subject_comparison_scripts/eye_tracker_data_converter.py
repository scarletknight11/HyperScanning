# %% Calculate gaze direction in new column
# Formula to convert cartesian to degree
def gaze_direction_in_x_axis_degree(x, y):
    """Right hand rule coordinate"""
    try:
        degree = degrees(atan(y / x))  # Opposite / adjacent
    except ZeroDivisionError:
        degree = 0.0
    return round(degree, 2)

def gaze_direction_in_y_axis_degree(y, z):
    """Right hand rule coordinate"""
    try:
        degree = degrees(atan(z / y)) # Opposite / adjacent
    except ZeroDivisionError:
        degree = 0.0
    return round(degree, 2)

# Give mark 1 for GazeDirectionYDegree that falls under fovea are (30 degrees), otherwise 0
def check_degree_within_fovea(gaze_direction):
    """ In total 30 degrees where human can recognize an object. So we need to
    divide by 2. Half right and half left

    1 = within fovea
    0 = not wihtin fovea"""

    if (gaze_direction <= 15) & (gaze_direction >= 0):
        return 1
    elif (gaze_direction >= -15) & (gaze_direction <= 0):
        return 1
    else:
        return 0
