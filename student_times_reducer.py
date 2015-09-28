#!/usr/bin/python
'''
Students and Posting Time on Forums

Find for each student what is the hour during which the student has posted the most posts.

Reducer input record format
(one record per post):

author_id   hour

Reducer output record format
(summary record per author_id with most frequent posting hour):

author_id   hour

If there are multiple hours during which a student has posted a maximum number of posts, the student-hour pairs are printed on separate lines.
'''

import sys

def reducer():

    last_author = None
    count_by_hour = [0]*24

    for line in sys.stdin:
        author_id, hour = line.strip().split("\t")
        try:
            author_id = int(author_id)
            hour = int(hour)
        except ValueError:
            continue

        if last_author and author_id != last_author:
            max_posts = max(count_by_hour)
            for h, count in enumerate(count_by_hour):
                if count == max_posts:
                    print "{0}\t{1}".format(last_author, h)
            count_by_hour = [0]*24

        last_author = author_id
        count_by_hour[hour] += 1

    if last_author != None:
        max_posts = max(count_by_hour)
        for h, count in enumerate(count_by_hour):
            if count == max_posts:
                print "{0}\t{1}".format(last_author, h)

if __name__ == "__main__":
    reducer()
