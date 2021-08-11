from scipy.stats import chisquare
import numpy as np
import statsmodels as sm
from collections import Counter
import scipy
import itertools
import os
import pickle
from icecream import ic
from scipy.stats import boschloo_exact, kendalltau
import datetime
# %% Read all list of eye conditions (averted, direct, and natural)
os.chdir("/hpc/igum002/codes/frontiers_hyperscanning2/eeg_all_connections/")

# Read averted pre list
with open('total_n_connections_all_pairs_averted_pre.pkl', 'rb') as handle:
    total_n_connections_all_pairs_averted_pre = pickle.load(handle)
    # print(len(total_n_connections_all_pairs_averted_pre))

# Read averted post list
with open('total_n_connections_all_pairs_averted_post.pkl', 'rb') as handle:
    total_n_connections_all_pairs_averted_post = pickle.load(handle)
    # print(len(total_n_connections_all_pairs_averted_post))

# Read direct pre list
with open('total_n_connections_all_pairs_direct_pre.pkl', 'rb') as handle:
    total_n_connections_all_pairs_direct_pre = pickle.load(handle)
    # print(len(total_n_connections_all_pairs_direct_pre))

# Read direct post list
with open('total_n_connections_all_pairs_direct_post.pkl', 'rb') as handle:
    total_n_connections_all_pairs_direct_post = pickle.load(handle)
    # print(len(total_n_connections_all_pairs_direct_post))

# Read natural pre list
with open('total_n_connections_all_pairs_natural_pre.pkl', 'rb') as handle:
    total_n_connections_all_pairs_natural_pre = pickle.load(handle)
    # print(len(total_n_connections_all_pairs_natural_pre))

# Read natural post list
with open('total_n_connections_all_pairs_natural_post.pkl', 'rb') as handle:
    total_n_connections_all_pairs_natural_post = pickle.load(handle)
    # print(len(total_n_connections_all_pairs_natural_post))

# Create function to count the most frequent pair
def most_frequent(List):
    return max(set(List), key=List.count)

# %%  Populate all connections of all bands of all eye conditions
# (averted_pre and post, direct_pre and post, natural_pre and post)
theta_averted_pre = []
alpha_averted_pre = []
beta_averted_pre = []
gamma_averted_pre = []
theta_averted_post = []
alpha_averted_post = []
beta_averted_post = []
gamma_averted_post = []

theta_direct_pre = []
alpha_direct_pre = []
beta_direct_pre = []
gamma_direct_pre = []
theta_direct_post = []
alpha_direct_post = []
beta_direct_post = []
gamma_direct_post = []

theta_natural_pre = []
alpha_natural_pre = []
beta_natural_pre = []
gamma_natural_pre = []
theta_natural_post = []
alpha_natural_post = []
beta_natural_post = []
gamma_natural_post = []

# Container for connections that are statisically significant before and after
alpha_averted_pre_labels = []
alpha_averted_post_labels = []
alpha_direct_pre_labels = []
alpha_direct_post_labels = []
alpha_natural_pre_labels = []
alpha_natural_post_labels = []


for i in range(len(total_n_connections_all_pairs_averted_pre)):

    # averted
    averted_pre_connections = total_n_connections_all_pairs_averted_pre[i]
    averted_post_connections = total_n_connections_all_pairs_averted_post[i]
    # direct
    direct_pre_connections = total_n_connections_all_pairs_direct_pre[i]
    direct_post_connections = total_n_connections_all_pairs_direct_post[i]
    # natural
    natural_pre_connections = total_n_connections_all_pairs_natural_pre[i]
    natural_post_connections = total_n_connections_all_pairs_natural_post[i]

    for j in range(len(averted_pre_connections)):
        if (j == 0):
            # averted
            theta_averted_pre.append(len(averted_pre_connections[j]))
            theta_averted_post.append(len(averted_post_connections[j]))

            # direct
            theta_direct_pre.append(len(direct_pre_connections[j]))
            theta_direct_post.append(len(direct_post_connections[j]))

            # natural
            theta_natural_pre.append(len(natural_pre_connections[j]))
            theta_natural_post.append(len(natural_post_connections[j]))

        elif (j == 1):
            # averted
            alpha_averted_pre.append(len(averted_pre_connections[j]))
            alpha_averted_post.append(len(averted_post_connections[j]))

            # significant averted pre labels (stat significant*)
            alpha_averted_pre_labels.append(averted_pre_connections[j])
            # significant averted post labels (stat significant*)
            alpha_averted_post_labels.append(averted_post_connections[j])

            # direct
            alpha_direct_pre.append(len(direct_pre_connections[j]))
            alpha_direct_post.append(len(direct_post_connections[j]))

            # significant direct pre labels (stat significant*)
            alpha_direct_pre_labels.append(direct_pre_connections[j])
            # significant direct post labels (stat significant*)
            alpha_direct_post_labels.append(direct_post_connections[j])

            # natural
            alpha_natural_pre.append(len(natural_pre_connections[j]))
            alpha_natural_post.append(len(natural_post_connections[j]))

            # significant natural pre labels (stat significant*)
            alpha_natural_pre_labels.append(natural_pre_connections[j])
            # significant natural post labels (stat significant*)
            alpha_natural_post_labels.append(natural_post_connections[j])

        elif (j == 2):
            # averted
            beta_averted_pre.append(len(averted_pre_connections[j]))
            beta_averted_post.append(len(averted_post_connections[j]))

            # direct
            beta_direct_pre.append(len(direct_pre_connections[j]))
            beta_direct_post.append(len(direct_post_connections[j]))
            # natural
            beta_natural_pre.append(len(natural_pre_connections[j]))
            beta_natural_post.append(len(natural_post_connections[j]))
        else:
            # averted
            gamma_averted_pre.append(len(averted_pre_connections[j]))
            gamma_averted_post.append(len(averted_post_connections[j]))
            # direct
            gamma_direct_pre.append(len(direct_pre_connections[j]))
            gamma_direct_post.append(len(direct_post_connections[j]))
            # natural
            gamma_natural_pre.append(len(natural_pre_connections[j]))
            gamma_natural_post.append(len(natural_post_connections[j]))

# %% compare all eye conditions (post-training, all freqs)
# theta all eyes post-training
all_eyes_theta_post = np.array([theta_averted_post, theta_direct_post, theta_natural_post])
theta_post_all_cond = chisquare(all_eyes_theta_post.T, axis=None)
print("Theta all eyes post : ", theta_post_all_cond)
# alpha all eyes post-training
all_eyes_alpha_post = np.array([alpha_averted_post, alpha_direct_post, alpha_natural_post])
alpha_post_all_cond = chisquare(all_eyes_alpha_post.T, axis=None)
# print(alpha_post_all_cond)
# beta all eyes post-training
all_eyes_beta_post = np.array([beta_averted_post, beta_direct_post, beta_natural_post])
beta_post_all_cond = chisquare(all_eyes_beta_post.T, axis=None)
print("beta all eyes post : ", beta_post_all_cond)
# gamma all eyes post-training
all_eyes_gamma_post = np.array([gamma_averted_post, gamma_direct_post, gamma_natural_post])
gamma_post_all_cond = chisquare(all_eyes_gamma_post.T, axis=None)
# print(gamma_post_all_cond)
# %% total number of brain connections (based on the above stat significant connections)

# theta
print("############ Theta #######################")
print("theta averted before : ", sum(theta_averted_pre))
print("theta averted after : ", sum(theta_averted_post))
print("")

print("theta direct before : ", sum(theta_direct_pre))
print("theta direct after : ", sum(theta_direct_post))
print("")

print("theta natural before : ", sum(theta_natural_pre))
print("theta natural after : ", sum(theta_natural_post))
print("")
print("############ Beta #######################")
# beta
print("beta averted before : ", sum(beta_averted_pre))
print("beta averted after : ", sum(beta_averted_post))
print("")

print("beta direct before : ", sum(beta_direct_pre))
print("beta direct after : ", sum(beta_direct_post))
print("")

print("beta natural before : ", sum(beta_natural_pre))
print("beta natural after : ", sum(beta_natural_post))
print("")

# %% Number of connections for each pair each eye condition
# theta
print("############ Theta #######################")
print("theta_averted_pre : ", theta_averted_pre)
print("theta_averted_post : ", theta_averted_post)
print("")

print("theta_direct_pre : ", theta_direct_pre)
print("theta_direct_post : ", theta_direct_post)
print("")

print("theta_natural_pre : ", theta_natural_pre)
print("theta_natural_post : ", theta_natural_post)
print("")

print("############ Beta #######################")
# beta
print("beta_averted_pre : ", beta_averted_pre)
print("beta_averted_post : ", beta_averted_post)
print("")

print("beta_direct_pre : ", beta_direct_pre)
print("beta_direct_post : ", beta_direct_post)
print("")

print("beta_natural_pre : ", beta_natural_pre)
print("beta_natural_post : ", beta_natural_post)
print("")
# %% ideas
# Contigency table
# 1. Apakah ada korelasi antara eye gaze directions (averted / direct) dengan brain synchronization ?
# Chi-square
# 2. Jumlah brain synchronization pada saat direct eye gaze itu sama aja (null hypothesis)
# In other words, direct eye gaze itu memberikan brain synchronization yang berbeda (alternative hypothesis)
