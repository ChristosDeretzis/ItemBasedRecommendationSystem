from ItemBasedCollaborativeFiltering import item_to_item_collaborative_filtering
def chooseSimilarityMethod():
    print("Choose the similarity method")
    print("For Jaccard Similarity, press 1")
    print("For Dice Similarity, press 2")
    print("For Cosine Similarity, press 3")
    print("For Adjusted Cosine Similarity, press 4")
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        return "Jaccard"
    elif choice == 2:
        return "Dice"
    elif choice == 3:
        return "Cosine"
    elif choice == 4:
        return "Adjusted Cosine"
    return None

def chooseCalculationMethod():
    print("Choose the calculation method")
    print("For Simple Average, press 1")
    print("For Weighted Average, press 2")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        return "Simple Average"
    elif choice == 2:
        return "Weighted Average"
    return None

def choose_matrix_elements():
    n_rows = int(input("Enter the number of users(rows): "))
    n_columns = int(input("Enter the number of items(columns): "))
    percent = float(input("Enter the percent of the known elements of the matrix(between 0 and 100): ")) / 100.0
    number_of_iterations = int(input("Enter the number of iterations: "))
    k = int(input("Enter the number of k: "))

    return n_rows, n_columns, percent, number_of_iterations, k

if __name__ == '__main__':
    n_rows, n_columns, percent, iters, k = choose_matrix_elements()
    method_similarity = chooseSimilarityMethod()
    method_calculation = chooseCalculationMethod()
    item_to_item_collaborative_filtering(n_rows, n_columns, percent, method_similarity, method_calculation, k, iters)



