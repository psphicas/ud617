# ud617
Intro to Hadoop and MapReduce

## Final Project

Given a set of forum posts, use map-reduce to solve the following problems:

1. Student Times

For each student, find the hour during which the student has posted the most posts.

[mapper](student_times_mapper.py)
[reducer](student_times_reducer.py)

2. Post and Answer Length

For each question, find the length of the post and the average answer length.

[mapper](average_length_mapper.py)
[reducer](average_length_reducer.py)

3. Top Tags

Find the Top 10 tags, ordered by the number of questions they appear in.

[mapper](popular_tags_mapper.py)
[reducer](popular_tags_reducer.py)

4. Study Groups

For each forum thread (that is a question node with all it's answers and comments),
list the students that have posted there.

[mapper](study_groups_mapper.py)
[reducer](study_groups_reducer.py)

## Validation

Validation instructions are provided here:

https://www.udacity.com/wiki/ud617/local-testing-instructions

## Datasets

Udacity provides two datasets compatible with the scripts:

- [small dataset](https://s3.amazonaws.com/udacity-hosted-downloads/student_test_posts.csv)
- [full dataset](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz)

