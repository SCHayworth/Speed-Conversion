# Speed Conversion
# Shaun Hayworth
# CIS 2
# 12-03-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/Speed-Conversion

# This program generates a table of speeds in kilometers per hour and their
# equivalent speeds in miles per hour, starting with 40 kph and ending at 120
# in 10 kph increments.


# Define the main function
def main():
    '''This is the mainline program logic.'''
    # Initialize the first speed in kph.
    kph = 40

    # Print the table header, then loop through the kph_to_mph function
    # nine times, incrementing kph by 10 each time.
    print("""
          KPH         MPH
          ----------------
          """)
    for each in range(1,10):
        print(f'{kph}         {kph_to_mph(kph)}')
        kph += 10


# Define the kph_to_mph function.
def kph_to_mph(speed):
    '''Converts speed in kilometers-per-hour to miles-per-hour'''
    # Calculate the speed in mph and return the result.
    mph = speed * 0.6214
    return mph


# Call the main() function to execute the program.
main()
