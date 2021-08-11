from scipy import signal
from math import atan, pi, degrees
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from icecream import ic
import glob
# %% Gaze direction averted
# use your path
path = r'/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_clean_new/'
averted_pre_files = glob.glob(path + "/*averted_pre*.csv")
pattern = re.compile(r"[S]+(\d+)\-")
averted_files_pre_odd = []
averted_files_pre_even = []

for file in averted_pre_files:
    if int(re.search(pattern, file).group(1)) % 2 != 0:
        averted_files_pre_odd.append(file)
    else:
        averted_files_pre_even.append(file)

li_averted_pre_odd = []
li_averted_pre_even = []

# ###############################################
# Combine all averted pre odd files
for filename in averted_files_pre_odd:
    df_averted_pre_odd = pd.read_csv(filename, index_col=None, header=0)
    li_averted_pre_odd.append(df_averted_pre_odd)
# Populate all dataframes into one dataframe
df_averted_pre_odd = pd.concat(li_averted_pre_odd, axis=0, ignore_index=True)
# Remove row where there is NaN value
df_averted_pre_odd = df_averted_pre_odd.dropna()
df_averted_pre_odd = df_averted_pre_odd.reset_index(drop=True)
# Remove space before column names
df_averted_pre_odd_new_columns = df_averted_pre_odd.columns.str.replace(
    ' ', '')
df_averted_pre_odd.columns = df_averted_pre_odd_new_columns
# df_averted_pre_odd.head()

# ###############################################
# Combine all averted pre even files
for filename in averted_files_pre_even:
    df_averted_pre_even = pd.read_csv(filename, index_col=None, header=0)
    li_averted_pre_even.append(df_averted_pre_even)

# Populate all dataframes into one dataframe
df_averted_pre_even = pd.concat(li_averted_pre_even, axis=0, ignore_index=True)

# Remove row where there is NaN value
df_averted_pre_even = df_averted_pre_even.dropna()
df_averted_pre_even = df_averted_pre_even.reset_index(drop=True)

# Remove space before column names
df_averted_pre_even_new_columns = df_averted_pre_even.columns.str.replace(
    ' ', '')
df_averted_pre_even.columns = df_averted_pre_even_new_columns
# df_averted_pre_even.head()

# %% Calculate GazeDirection for both eyes in Degree

# Gaze direction (right eye)
df_averted_pre_odd['GazeDirectionRight(X)Degree'] = df_averted_pre_odd.apply(lambda x: gaze_direction_in_x_axis_degree(x['GazeDirectionRight(X)'], x['GazeDirectionRight(Y)']), axis=1)
df_averted_pre_odd['GazeDirectionRight(Y)Degree'] = df_averted_pre_odd.apply(lambda x: gaze_direction_in_y_axis_degree(x['GazeDirectionRight(Y)'], x['GazeDirectionRight(Z)']), axis=1)

# Gaze direction (left eye)
df_averted_pre_odd['GazeDirectionLeft(X)Degree'] = df_averted_pre_odd.apply(lambda x: gaze_direction_in_x_axis_degree(x['GazeDirectionLeft(X)'], x['GazeDirectionLeft(Y)']), axis=1)
df_averted_pre_odd['GazeDirectionLeft(Y)Degree'] = df_averted_pre_odd.apply(lambda x: gaze_direction_in_y_axis_degree(x['GazeDirectionLeft(Y)'], x['GazeDirectionLeft(Z)']), axis=1)

# %% Give mark 1 for GazeDirection Y/X Degree that falls under fovea area (30 degrees), otherwise 0

df_averted_pre_odd['GazeDirectionRight(X)inFovea'] = df_averted_pre_odd.apply(lambda x: check_degree_within_fovea(x['GazeDirectionRight(X)Degree']), axis=1)
df_averted_pre_odd['GazeDirectionRight(Y)inFovea'] = df_averted_pre_odd.apply(lambda x: check_degree_within_fovea(x['GazeDirectionRight(Y)Degree']), axis=1)
df_averted_pre_odd['GazeDirectionLeft(X)inFovea'] = df_averted_pre_odd.apply(lambda x: check_degree_within_fovea(x['GazeDirectionLeft(X)Degree']), axis=1)
df_averted_pre_odd['GazeDirectionLeft(Y)inFovea'] = df_averted_pre_odd.apply(lambda x: check_degree_within_fovea(x['GazeDirectionLeft(Y)Degree']), axis=1)
