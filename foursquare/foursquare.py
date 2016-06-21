# foursquare.py - Some attempts at collaborative filtering based on Foursquare data

'''
Command line arguments:
- Option 1: 1 argument
    - argument should be file to be parsed
    - k is set to 1 by default
- Option 1: 2 arguments
    - 1st argument is 'k' in kNN algorithm
    - 2nd argument is file to be parsed
File format:
Should be a tsv file
1st column is the user
2nd column is the location

Output:
Uses model-based collaborative filtering techniques
to calculate the "distance" between any two places.
Prints out a dictionary mapping each place with a
list of tuples in the from (cosine, neighbor) where
each list is "k" tuples long as specified by the user.
This output can be redirected into a text file to be
used in other programs.
'''



import sys
import codecs

class Recommender:

    def __init__(self, k, path):
        self.k = k
        self.data = {}
        f = codecs.open(path)
        for line in f:
            values = line.split('\t')
            place = values[1].strip()
            user = values[0].strip()
            if place not in self.data:
                self.data[place] = []
            self.data[place].append(user)


    def cosine(self, place1, place2):
        numerator = 0.0
        mag1 = len(self.data[place1])
        mag2 = len(self.data[place2])
        for user in self.data[place1]:
            if user in self.data[place2]:
                numerator += 1
        return numerator/(mag1 * mag2)

    def nearest_k(self, place):
        candidates = []
        for candidate in self.data:
            if candidate != place:
                candidates.append((self.cosine(place,candidate), candidate))
        candidates = sorted(candidates, reverse = True)
        return candidates[:self.k]

    def build_table(self):
        self.table = {}
        for place in self.data:
            self.table[place] = self.nearest_k(place)

def main():
    if len(sys.argv) == 3:
        r = Recommender(int(sys.argv[1]),sys.argv[2])
    if len(sys.argv) == 2:
        r = Recommender(1,sys.argv[1])
    r.build_table()
    print(r.table)

if __name__ == "__main__":
    main()