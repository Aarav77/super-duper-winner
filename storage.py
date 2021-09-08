import csv

all_movies = []
data=[]
with open('final.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    #data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []