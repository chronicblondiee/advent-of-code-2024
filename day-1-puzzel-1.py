# imports
import numpy as np

# main()
def main ():
    # load data
    input_list = np.loadtxt('inputs/day-1/day-1-input.txt')
    # extra number colums into arrays
    left_list = input_list[:, 0]
    right_list = input_list[:, 1]
    print("right list ", left_list)
    print("right list", right_list)


if __name__ == "__main__":
    main()