"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - the baking time already elapsed.
    :return: int - remaining bake time in minutes derived from EXPECTED_BAKE_TIME.

    Takes the actual minutes the lasagna has been in the oven and
    returns how many minutes it still needs to bake based on EXPECTED_BAKE_TIME.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining
    


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    
    """Calculate preparation time in minutes based on number of layers.

    :param number_of_layers: int - the number of layers in the cake.
    :return: int - preparation time in minutes.

    Each layer takes 2 minutes to prepare,
    so the total is number_of_layers multiplied by 2.
    """
    preparation_time_in_minutes = number_of_layers * 2
    return preparation_time_in_minutes



    
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the cake.
    :param elapsed_bake_time: int - the baking time already elapsed.
    :return: int - total elapsed time in minutes.

    Each layer takes 2 minutes to prepare, added to the
    elapsed bake time to give the total time elapsed.
    """
    total_time = (number_of_layers * 2) + elapsed_bake_time
    return total_time
    



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
