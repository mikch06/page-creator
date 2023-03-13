from csv import DictReader
import random
from datetime import datetime

filename = 'wine_content.csv'

with open(filename, 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for col in csv_dict_reader:
        #print(col['created'], col['title'], col['introtext'], col['catid'])
        dstamp = datetime.strptime(col['created'], '%Y-%m-%d %H:%M:%S')
        #tstamp = dstamp.strftime("%Y.%m.%d")
        tstamp = dstamp.strftime("%Y-%m-%d")

        # Random number attach to filename
        rnmbr = random.randint(1, 99)
        file = tstamp + '-' + str(rnmbr) + ".md"
        print("Filename: ", file)

        print("Content:")
        print("")
        print("---")
        print("winename:", col['title'])
        print("date:", tstamp)
        print("category:", col['catid'])
        print("tags:")
        print("---")
        print(col['introtext'])
        #tstamp )

        print("")

        f = open(file, "w")
        f.write("---\n")
        f.write("winename: " + col['title'] + "\n")
        f.write("date: " + tstamp + "\n")
        f.write("category: " + col['catid'] + "\n")
        f.write("tags:\n")
        f.write("image: " + col['introtext'] + "\n")
        f.write("---\n")
        f.close()


