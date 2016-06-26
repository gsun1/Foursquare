# analysis.py - Formats results of foursquare.py and ftest.py to be ready for analysis

'''
Input:
Should take exactly 2 arguments
    - 1st argument: The original data
    - 2nd argument: The corresponding output of fstest.py

Output:
First prints string 'Place,Times,Recommended'
The prints line by line data in the format
p,t,r
where
p = name of the place
t = number of times somebody checked in at the place
r = 0 if not Recommended, 1 otherwise
'''

import sys
import codecs

def main():
    if len(sys.argv) == 3:
        f = codecs.open(sys.argv[1])
        results = codecs.open(sys.argv[2])

        data = {}
        recd = []
        info = []



        for line in f:
            values = line.split('\t')
            place = values[1].strip()
            user = values[0].strip()
            if place not in data:
                data[place] = 1
            else:
                data[place] += 1

        count = 0.0
        for place in data:
            count += data[place]
        data_stats = count/len(data)

        for line in results:
            stripped = line.strip()
            info.append((data[stripped],stripped))
            recd.append(stripped)

        print('Place,Times,Recommended')

        for line in data:
            string = '%s,%d,%d'
            name = line
            times = data[line]
            if line in recd:
                recbool = 0
            else:
                recbool = 1
            print (string % (name,times,recbool))

    else:
        raise RuntimeError("Incorrect number of arguments")

if __name__ == "__main__":
    main()
