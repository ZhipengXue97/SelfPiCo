# Extracted from https://stackoverflow.com/questions/3160699/python-progress-bar
import sys
import time

def ProgressBar(Total, Progress, BarLength=20, ProgressIcon="#", BarIcon="-"):
    try:
        # You can't have a progress bar with zero or negative length.
        if BarLength <1:
            BarLength = 20
        # Use status variable for going to the next line after progress completion.
        Status = ""
        # Calcuting progress between 0 and 1 for percentage.
        Progress = float(Progress) / float(Total)
        # Doing this conditions at final progressing.
        if Progress >= 1.:
            Progress = 1
            Status = "\r\n"    # Going to the next line
        # Calculating how many places should be filled
        Block = int(round(BarLength * Progress))
        # Show this
        Bar = "[{}] {:.0f}% {}".format(ProgressIcon * Block + BarIcon * (BarLength - Block), round(Progress * 100, 0), Status)
        return Bar
    except:
        return "ERROR"

def ShowBar(Bar):
    sys.stdout.write(Bar)
    sys.stdout.flush()

if __name__ == '__main__':
    print("This is a simple progress bar.\n")

    # Example #1:
    print('Example #1')
    Runs = 10
    for i in range(Runs + 1):
        progressBar = "\rProgress: " + ProgressBar(10, i, Runs)
        ShowBar(progressBar)
        time.sleep(1)

    # Example #2:
    print('\nExample #2')
    Runs = 10
    for i in range(Runs + 1):
        progressBar = "\rProgress: " + ProgressBar(10, i, 20, '|', '.')
        ShowBar(progressBar)
        time.sleep(1)

    print('\nDone.')

# Example #2:
Runs = 10
for i in range(Runs + 1):
    ProgressBar(10, i)
    time.sleep(1)

