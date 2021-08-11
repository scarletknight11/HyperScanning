# cd /hpc/igum002/codes/frontiers_hyperscanning2/
import pandas as pd
from os.path import isfile, join
from os import listdir
import os
from extract_eye_tracker import extract_eye_data

# %% Extract data from raw eye data files (original recorded files)
listFiles = ["EyeTracker-S1.csv", "EyeTracker-S2.csv", "EyeTracker-S3.csv", "EyeTracker-S4.csv", "EyeTracker-S5.csv", "EyeTracker-S6.csv", "EyeTracker-S7.csv", "EyeTracker-S8.csv",
             "EyeTracker-S9.csv", "EyeTracker-S10.csv", "EyeTracker-S11.csv", "EyeTracker-S12.csv", "EyeTracker-S13.csv", "EyeTracker-S14.csv", "EyeTracker-S15.csv", "EyeTracker-S16.csv",
             "EyeTracker-S17.csv", "EyeTracker-S18.csv", "EyeTracker-S19.csv", "EyeTracker-S20.csv", "EyeTracker-S21.csv", "EyeTracker-S22.csv", "EyeTracker-S23.csv", "EyeTracker-S24.csv",
             "EyeTracker-S25.csv", "EyeTracker-S26.csv", "EyeTracker-S27.csv", "EyeTracker-S28.csv", "EyeTracker-S29.csv", "EyeTracker-S30.csv", "EyeTracker-S31.csv", "EyeTracker-S32.csv"]
listOrders = [1, 2, 1, 2, 1, 2, 1, 2,  3, 4,
              3, 4, 3, 4, 3, 4,  5, 6, 5, 6, 5, 6, 7, 8,
              7, 8, 7, 8, 9, 10, 9, 10]
path_eye_data_original = "/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_original/"

for idx, file in enumerate(listFiles):
    from_raw_eye_file = join(path_eye_data_original, file)
    extract_eye_data(from_raw_eye_file, listOrders[idx])

# # %%
# import os
# mypath = '/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_separated'
# for dirpath, dirnames, filenames in os.walk(mypath):
#     for filename in filenames:
#         if '_pre_' in filename or '_post_' in filename:
#             print(filename)

# %% Combine pre and post eye tracker data

path_eye_data_separated = '/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_separated'
path_eye_data_combined = '/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_combined'
onlyfiles = [f for f in listdir(path_eye_data_separated) if isfile(
    join(path_eye_data_separated, f))]

selected_averted_eye_files = []
selected_direct_eye_files = []
selected_natural_eye_files = []

for file in onlyfiles:
    if 'averted_pre_' in file or 'averted_post_' in file:
        selected_averted_eye_files.append(file)
    elif 'direct_pre_' in file or 'direct_post_' in file:
        selected_direct_eye_files.append(file)
    elif 'natural_pre_' in file or 'natural_post_' in file:
        selected_natural_eye_files.append(file)
# %% Combine csv files

for i in range(0, 4, 2):

    # Averted eye data
    df1_averted = pd.read_csv(os.path.join(
        path_eye_data_separated, selected_averted_eye_files[i]))
    df2_averted = pd.read_csv(os.path.join(
        path_eye_data_separated, selected_averted_eye_files[i + 1]))
    df_combined_averted = pd.concat([df1, df2], ignore_index=True)
    fname = selected_averted_eye_files[0]
    # Get subject no.
    start_idx = fname.find("S")
    end_idx = fname.index("-")
    sub_no = fname[start_idx:end_idx]
    fname_combined_averted = sub_no + "-averted_" + "left_right_combined" + ".csv"
    # save to csv file
    df_combined_averted.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_averted))

    # Direct eye data
    df1_direct = pd.read_csv(os.path.join(
        path_eye_data_separated, selected_direct_eye_files[i]))
    df2_direct = pd.read_csv(os.path.join(
        path_eye_data_separated, selected_direct_eye_files[i + 1]))
    df_combined_direct = pd.concat([df1_direct, df2_direct], ignore_index=True)
    fname_combined_direct = sub_no + "-direct_" + "left_right_combined" + ".csv"
    # save to csv file
    df_combined_direct.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_direct))

    # natural eye data
    df1_natural = pd.read_csv(os.path.join(
        path_eye_data_separated, selected_natural_eye_files[i]))
    df2_natural = pd.read_csv(os.path.join(
        path_eye_data_separated, selected_natural_eye_files[i + 1]))
    df_combined_natural = pd.concat(
        [df1_natural, df2_natural], ignore_index=True)
    fname_combined_natural = sub_no + "-natural_" + "left_right_combined" + ".csv"
    # save to csv file
    df_combined_natural.to_csv(os.path.join(
        path_eye_data_combined, fname_combined_natural))

print("Files have been combined and saved, man !")

# %% Direct
for file in onlyfiles:
    if 'direct_pre_' in file or 'direct_post_' in file:
        # print(file)
        selected_direct_eye_files.append(file)
        # Combine csv files
        for i in range(0, 4, 2):
            df1_direct = pd.read_csv(os.path.join(
                path_eye_data_separated, selected_direct_eye_files[i]))
            df2_direct = pd.read_csv(os.path.join(
                path_eye_data_separated, selected_direct_eye_files[i + 1]))
            df_combined_direct = pd.concat(
                [df1_direct, df2_direct], ignore_index=True)
# %% Natural
for file in onlyfiles:
    if 'natural_pre_' in file or 'natural_post_' in file:
    selected_natural_eye_files.append(file)
    # Combine csv files
    for i in range(0, 4, 2):
        df1_natural = pd.read_csv(os.path.join(
            path_eye_data_separated, selected_natural_eye_files[i]))
        df2_natural = pd.read_csv(os.path.join(
            path_eye_data_separated, selected_natural_eye_files[i + 1]))
        df_combined_natural = pd.concat(
            [df1_natural, df2_natural], ignore_index=True)

# %% test icecream

# import pandas as pd
# os.chdir("/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_combined/")
#
# df = pd.read_csv("/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_combined/S1-averted_post_right_left_combined.csv")
# %%
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split(r'(\d+)', text)]

def delete_epoch_eye_tracker(file_tag, indices):
    path = '/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_combined/'
    files = [file for file in os.listdir(path) if file_tag in file]
    ic(files)
    # files = files.sort(key=natural_keys)
    seconds  = 120
    for idx, file in enumerate(files):
        df = pd.read_csv(path + file)

        rate = (df.shape[0]-2) / seconds
        num_row_chunk = int(rate)
        end = 0
        chunks = []
        for second in range(seconds):
            start = end + 1
            dec = ((rate - num_row_chunk) * second) - int((rate - num_row_chunk) * second)
            end = start - 1 +  num_row_chunk + (1 if dec < (rate - num_row_chunk) else 0)
            chunks += [(start,end)]

        if idx < len(indices):
            for dlt in indices[idx]:
                df = df.drop([*range(chunks[dlt][0],chunks[dlt][1]+1,1)])
            path_save = '/hpc/igum002/codes/frontiers_hyperscanning2/eye_tracker_data_clean/'
            df.to_csv(path_save + file[:file.rfind('.')] + '_clean.csv')

# %%

delete_epoch_eye_tracker('averted_pre', [[1],[2],[3],[5,6],[1],[2],[3],[5,6],[1],[2],[3],[5,6],[1],[2],[3],[5,6],[1],[2],[3],[5,6],[1],[2],[3],[5,6],[1],[2],[3],[5,6],[1],[2],[3],[5,6]])

ic(round(df.shape[0] / seconds+0.5,0))
