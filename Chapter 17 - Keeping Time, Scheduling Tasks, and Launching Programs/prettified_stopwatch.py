# A stopwatch program that logs laps each time the ENTER key is pressed.
# Upon Keyboard Interruption (Ctrl + C), the overall results will get
# copied to the clipboard, and the program exits.

import time, pyperclip


def stopwatch():
    # Display the program's instructions.
    print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    input()  # press Enter to begin
    print('Started.')
    start_time = time.time()  # get the first lap's start time
    last_time = start_time
    lap_num = 1
    summary = []

    # Start tracking the lap times.
    try:
        while True:
            input()
            lap_num_str = str(lap_num).rjust(2)
            lap_time = str(round(time.time() - last_time, 2)).rjust(5)
            total_time = str(round(time.time() - start_time, 2)).rjust(5)
            lap_str = f'Lap #{lap_num_str}: {total_time} ({lap_time})'
            print(lap_str, end='')

            # Adding lap results to summary list
            summary.append(lap_str)

            lap_num += 1
            last_time = time.time()  # reset the last lap time
    except KeyboardInterrupt:
        # Handle the Ctrl-C exception to keep its error message from displaying, and copy summary to clipboard
        pyperclip.copy('\n'.join(summary))
        print('\nDone. The summary information has been copied to the clipboard.')


if __name__ == '__main__':
    stopwatch()
