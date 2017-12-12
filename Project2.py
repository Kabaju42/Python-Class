"""
Schedule time in between breaks
Run it through your shift
Alarm: open browser and play favorite vid/music
"""

#need: time
# url
# sleep
# loop

from webbrowser import open as openw
import time

break_count = 0

url = "https://youtu.be/6P9xxJ4V7no"


def break_music(break_info = None):
    """
    Function to keep track of breaks
    :param break_info:  a dictionary with the following info
        t_break <int> default = 3
        url<string> default = TSO Mad Russian Christmas
        t_sleep <integer> integer in seconds, default = 1 hr
    :return: Nothing
    """
    global break_count
    if break_info is None:
        break_info = {}
    if "t_breaks" not in break_info:
        break_info["t_breaks"] = 3
    if "url" not in break_info:
        break_info["url"] = "https://youtu.be/6P9xxJ4V7no"
    if "t_sleep" not in break_info:
        break_info["t_sleep"] = 60*60
    while True:
        print("break " + str(break_count))
        openw(break_info["url"])
        break_count += 1
        if break_count >= break_info["t_breaks"]:
            break
        time.sleep(break_info["t_sleep"])


def main():
    my_info = {}
    break_music(my_info)


if __name__ == '__main__':
    main()
