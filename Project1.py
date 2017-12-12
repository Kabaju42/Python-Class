"""
This is my first project -- documentation goes here
"""

# open a file from the web
# itterate over the file
# create a list of workds from the file
# iterate over new list

from urllib.request import urlopen
import sys


def fetch_words(f):
    """
    Fetches words from a file
    :param f: url address of an encoded file
    :return: Zilch
    """

    # """ creates the documentation
    # print("open the webpage")
    #f = "https://icarus.cs.weber.edu/~hvalle/hafb/wasteland.txt"
    #f = "http://kabaju.net/helena.html"

    story_words = []

    with urlopen(f) as story:
        for line in story:
            # print (line.decode('utf-8'))
            line_rec = line.decode('utf-8').split()
            # line_rec = line.split()
            # print(line_rec)

            for word in line_rec:
                story_words.append(word)
    print("This file has: ", len(story_words), " words")

def main(f):
    fetch_words(f)

if __name__ == "__main__":
    # test the code
    # print list of words
    f = "https://icarus.cs.weber.edu/~hvalle/hafb/wasteland.txt"
    #f = "http://kabaju.net/helena.html"

#    url = sys.argv[1]
    main(f)
    print(f)

#    print(story_words)




