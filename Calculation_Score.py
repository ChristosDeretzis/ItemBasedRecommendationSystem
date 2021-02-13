import numpy as np

def Simple_Average(score_predict, similarity_matrix, row, k):
    # similarity matrix is an array with tuple elements of the form: (similarity_value, column_index)
    #Sort the similarity matrix based on the similarity value of item
    similarity_matrix.sort(key=lambda x:x[0], reverse=True)

    # Calculate the simple average with the k values that
    # have the highest score prediction value. If k < number_of_not_nan_values,
    # then calculate the simple average of the number_of_not_nan_values
    sum_scores = 0

    # i is for counting all the loops inside while loop
    i = 0

    # j is for counting the loops, where score is not nan
    j = 0

    # for the k values that are not nan with the highest prediction score,
    # calculate the simple average
    while j < k:
        column = similarity_matrix[i][1]
        score = score_predict[row][column]

        # check if a score is not nan,
        # then add score to the variable sum_scores
        if not np.isnan(score):
            sum_scores += score
            j += 1;
        i += 1

        # if i is higher or equal than the number of columns of scores matrix, break out of the loop
        if i >= score_predict.shape[1] - 1:
            break
    return sum_scores/j


def Weighted_Average(score_predict, similarity_matrix, row, k):
    # similarity matrix is an array with tuple elements of the form: (similarity_value, column_index)
    #Sort the similarity matrix based on the similarity value of item
    similarity_matrix.sort(key=lambda x:x[0], reverse=True)

    # Calculate the weighted average with the k values that
    # have the highest score prediction value and use the score prediction
    # values as weights for the weighted average calculation. If k < number_of_not_nan_values,
    # then calculate the weighted average of the number_of_not_nan_values
    sum_scores = 0
    sum_weights = 0

    # i is for counting all the loops inside while loop
    i = 0

    # j is for counting the loops, where score is not nan
    j = 0

    # for the k values that are not nan with the highest prediction score,
    # calculate the weighted average
    while j < k:
        column = similarity_matrix[i][1]
        weight = similarity_matrix[i][0]
        score = score_predict[row][column]

        # check if a score is not equal to nan,
        # then add weighted_score and weight to their variables sums
        if not np.isnan(score):
            weighted_score = weight*score
            sum_scores += weighted_score
            sum_weights += weight
            j += 1
        i += 1

        # if i is higher or equal than the number of columns of scores matrix, break out of the loop
        if i>=score_predict.shape[1] - 1:
            break

    score = sum_scores/sum_weights
    if score > 0:
        return score
    else:
        return 10 - score


# This method is an extra prediction function for calculating the score in a matrix. It calculates the average value between
# Simple and Weighted Average
def Hybrid_Prediction(score_predict, similarity_matrix, row, k):
    simple_average = Simple_Average(score_predict, similarity_matrix, row, k);
    weighted_average = Weighted_Average(score_predict, similarity_matrix, row, k)
    return (simple_average + weighted_average)/2

if __name__ == '__main__':
    pass