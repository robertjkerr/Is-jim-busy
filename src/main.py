##
## Main script for logging gym occupancy
##

from occupancy import get_occupancy, write_log

if __name__ == "__main__":
    file = "gym_log.csv"
    occupancy = get_occupancy()
    write_log(occupancy, file)
