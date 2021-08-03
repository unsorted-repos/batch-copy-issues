import numpy as np

# from .helper import get_human_readable_schedule
# from .helper import write_list_to_file


def write_list_to_file(some_list, output_path):
    """TODO: move to helper

    :param some_list: param output_path:
    :param output_path: Relative path to a file that is outputted.

    """
    with open(output_path, "w") as f:
        for item in some_list:
            f.write("%s\n" % item)




def ask_two_factor_code():
    """USED"""
    two_fac_code = get_input(
        f"Please enter the two factor authentication you just received:"
    )
    return two_fac_code


def get_input(text):
    """

    :param text: 

    """
    return input(text)


def answer():
    """ """
    ans = get_input("enter yes or no")
    if ans == "yes":
        return "you entered yes"
    if ans == "no":
        return "you entered no"
