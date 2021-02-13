import numpy as np

def Jaccard_Similarity(matrix, column_01, column_02):
    # Create sets from x and y by removing the nan values
    x = {i for i in matrix[:,column_01] if not np.isnan(i)}
    y = {i for i in matrix[:,column_02] if not np.isnan(i)}

    # Calculate Jaccard Similarity
    intersection = len(set(x) & set(y))
    union = len(set(x) | set(y))
    return intersection/float(union)

def Dice_Similarity(matrix, column_01, column_02):
    # Create sets from x and y by removing the nan values
    x = {i for i in matrix[:,column_01] if not np.isnan(i)}
    y = {i for i in matrix[:,column_02] if not np.isnan(i)}

    # Calculate Dice Similarity
    intersection = len(set(x) & set(y))
    return (2*intersection)/(len(x) + len(y))

def Cosine_Similarity(matrix,column_01, column_02):

    # Get the 2 columns from matrix
    x = matrix[:, column_01]
    y = matrix[:, column_02]

    # Calculate the dot product, ignoring nan values
    dot_product = np.nansum(x*y)

    # calculate the norm of the x and y columns, ignoring nan values
    x_norm = np.linalg.norm(x[~np.isnan(x)])
    y_norm = np.linalg.norm(y[~np.isnan(y)])

    # return the result
    return dot_product/(x_norm*y_norm)

def Adjusted_Cosine_Similarity(matrix,column_01, column_02):
    # Calculate the mean of each row, ignoring the nan values
    row_mean = np.nanmean(matrix,axis=1)

    # Get the 2 columns from matrix
    x = matrix[:,column_01]
    y = matrix[:,column_02]

    # substract each element of the 2 columns by their row average
    x_adjusted = x - row_mean
    y_adjusted = y - row_mean

    # create a copy of the initial scores matrix prediction and
    # set the new columns with the adjusted ones
    copy_matrix = np.array(matrix)
    copy_matrix[:,column_01] = x_adjusted
    copy_matrix[:,column_02] = y_adjusted

    # Calculate cosine similarity on the adjusted columns
    return Cosine_Similarity(copy_matrix, column_01, column_02)

if __name__ == '__main__':
    pass