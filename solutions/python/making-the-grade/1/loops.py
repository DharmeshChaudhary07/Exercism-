"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    # rounded = []
    # for marks in student_scores:
    #     marks = round(marks)
    #     rounded.append(marks)
    # return rounded
    return [round(marks) for marks in student_scores]
    


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    count = 0
    for marks in student_scores:
        if marks <= 40:
            count += 1
    return count

    # using list comprehension 

        

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """
    assholes = []
    for marks in student_scores:
        if marks >= threshold:
            assholes.append(marks)
    return assholes

    # using list comprehension 


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    list = []
    grade = (highest - 40) // 4
    for i in range(4):
        list.append(41 + grade * i)
    return list

    # using list comprehension 
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    list = []
    for i in range(len(student_scores)):
        list.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return list

    

    # using list comprehension 


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    for i in student_info:
        if i[1] == 100:
            return i
    return []

    # using list comprehension 
    