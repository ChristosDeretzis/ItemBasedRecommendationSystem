import numpy as np
from numpy import random as rand

# Create a 2-dimensional n*m matrix filled with random numbers from the uniform distribution
def create_matrix(n_rows, n_columns):
    scores_array = np.around(rand.uniform(1,10,size=(n_rows, n_columns)), decimals = 2)
    return scores_array

# from the array filled with numbers from uniform distribution, choose only a percent of the matrix
# and the rest of the percent, fill it in with nan(not a number) values, in order to predict them
def calculate_scores_for_prediction(scores_array, percent):
    scores_for_prediction = scores_array.copy()
    number_of_nans = int(np.round((1-percent)*scores_array.shape[0]*scores_array.shape[1]))
    choices = np.random.choice(scores_array.size, number_of_nans, replace=False)
    scores_for_prediction.ravel()[choices] = np.nan

    return scores_for_prediction

if __name__ == '__main__':
    pass