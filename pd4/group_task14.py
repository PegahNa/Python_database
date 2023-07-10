"""
A&E Minimum Waiting Time Challenge -- SOLUTION

Please watch the demo video, which explains how to approach and solve
this challenge.

This is one of the multiple possible solutions (there might be many others)

This one is:
O(nlogn) time | O(1) space - where n is the number of patients
"""


def min_waiting_time(patients):
    """
    Calculate the minimum total waiting time for ALL patients
    :param patients: a list of ints where each int is a patient and
    the number represents the duration of their visit to a doctor
    :return: int  - total waiting time for all patients
    """
    patients.sort()  # sort the patients by waiting time in place
    total = 0

    for idx, time in enumerate(patients):
        patients_left = len(patients) - (idx + 1)
        total += time * patients_left
    print(total)
    return total

min_waiting_time([3,2,1,2,6])
