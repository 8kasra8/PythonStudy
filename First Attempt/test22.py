import sys
from urllib.request import urlopen


def fetch_words(url):
    storyWords = []

    story = urlopen(url)

    for line in story:
        lineList = line.decode('utf8').split()
        for word in lineList:
            storyWords.append(word)
        
    story.close()
    return storyWords

def print_words(storyWords):
    for word in storyWords:
        print(word)

def main(url):
    words = fetch_words(url)
    print_words(words)

if __name__ == "__main__":
    main(sys.argv[1])    


    
