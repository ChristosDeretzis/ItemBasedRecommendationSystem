import numpy as np
from Calculation_Score import Simple_Average, Weighted_Average, Hybrid_Prediction
from Scores_matrix import create_matrix, calculate_scores_for_prediction
from Similarities import Jaccard_Similarity, Dice_Similarity, Cosine_Similarity, Adjusted_Cosine_Similarity

# calculate the similarity of 2 columns based on a certain similarity method(e.g Dice, Cosine, ..)
def choose_comparision_method(name_of_method, matrix, index_column_01, index_column_02):
    if name_of_method == 'Jaccard':
        return Jaccard_Similarity(matrix, index_column_01, index_column_02)
    elif name_of_method == 'Dice':
        return Dice_Similarity(matrix, index_column_01, index_column_02)
    elif name_of_method == 'Cosine':
        return Cosine_Similarity(matrix, index_column_01, index_column_02)
    elif name_of_method == 'Adjusted Cosine':
        return Adjusted_Cosine_Similarity(matrix, index_column_01, index_column_02)

# this function predicts the score of a certain value in the scores matrix. It takes as argument the row and the column, where
# the score is located at the score matrix, the score matrix, the method prediction (such as simple average, weighted average or hybrid prediction),
# the method of prediction such as(cosine or adjusted cosine) and a certain value of k
def predict_score_in_place(n_row, n_col, score_matrix, method_prediction, method_calculation, k):
    # for each item(column) in the score matrix,except the column index where the predicted item is located
    # calculate the similarities between the column, where the item is located, and the other columns of
    # the score matrix
    similarities = []
    for j in range(len(score_matrix[n_row])):
        current_column = j
        if current_column == n_col:
            continue
        else:
            similarity = choose_comparision_method(method_prediction,score_matrix, current_column, n_col)
            similarities.append((similarity, current_column))
    if method_calculation == 'Simple Average':
        return Simple_Average(score_matrix, similarities, n_row, k)
    elif method_calculation == 'Weighted Average':
        return Weighted_Average(score_matrix, similarities, n_row, k)
    elif method_calculation == 'Hybrid Prediction':
        return Hybrid_Prediction(score_matrix, similarities, n_row, k)

# this function predicts the scores in the scores matrix filled with a certain percent of values, using a certain method
# of calculation (such as simple average, weighted average or hybrid prediction), a certain method of prediction
# such as(cosine or adjusted cosine) and a certain value of k
def predict_scores_in_matrix(scores_predict, scores_actual, method_prediction, method_calculation, k):
    absolute_error = 0
    number_of_nans = 0
    # loop through the 2d matrix
    for idx, x in np.ndenumerate(scores_predict):
        # if the value is not a number, then calculate the predicted value and find the absolute error of the predicted value
        if np.isnan(x):
            predicted_score = predict_score_in_place(idx[0], idx[1], scores_predict, method_prediction, method_calculation, k)
            actual_score = scores_actual[idx[0],idx[1]]
            absolute_error += np.absolute(predicted_score - actual_score)
            number_of_nans += 1
    # it returns the Mean Absolute Error of the predicted values
    return absolute_error/number_of_nans

# This fuction is the upper function of the item based collcaborative filtering. It takes as arguments the number of rows and
# columns of the matrix, the percentage of the known values in the score matrix, the method of prediction(like Cosine),
# the method of calculation(like Simple Average), the k value, and the iterations of the program
def item_to_item_collaborative_filtering(n_rows, n_cols, percent, method_prediction, method_calculation, k, n_iters):
    # Create a matrix based on the dimensions the user wants
    scores_matrix = create_matrix(n_rows, n_cols)

    sum = 0
    # for each iteration of the program, fill the matrix with certain values based on the percent the user wants, predict the
    # scores and calculate the mean absolute error of the predictions
    for i in range(n_iters):
        scores_to_predict = calculate_scores_for_prediction(scores_matrix, percent)
        mean_absolute_error = predict_scores_in_matrix(scores_to_predict, scores_matrix,method_prediction,method_calculation, k)
        print("For iteration ", i+1, " the mae is: ", mean_absolute_error)
        sum += mean_absolute_error

    # return the average of all mean absolute errors
    average = sum/n_iters
    print("Average MAE is: ", average)

if __name__ == '__main__':
    pass