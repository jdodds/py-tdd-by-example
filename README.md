# So what is this?

I've been re-reading
[Test Driven Development by Example](http://www.amazon.com/Test-Driven-Development-By-Example/dp/0321146530)
since it's been a few years since I last opened it, and decided to
write the examples given using Python. This repository reflects that.

In this repository, I'm trying to match the granularity of commits with the
"teeny" steps Kent describes in the book, giving a history of a
process that in any normal repository would happen in the space
between commits. This is not meant to be an example of what a commit
history for an application developed using TDD should look like.

After I'm finished going through the book, I'm looking forward to
creating some nice visualizations of the changes to the code over
time.

## Why Python?

Mostly because I like Python. That said, there are some points in the
book where taking the approach I am -- a mostly verbatim translation
-- produces code that isn't typical of what you'd do in Python. I'm
taking note of these spots as they arise, and if they're still present
after finishing the material, I'll be creating branches at the point
where they occur and refactoring them into "Pythonic" solutions using
the same style of commits as the rest of the repository.

## Why Public?

This is a type of thing that I find interesting, I'm sure others do as
well.

If you happen to be going through "TDD by example" and want to follow
along, there are tags for each chapter at the last commit made in that
chapter. They're named as follows:
`$part-$chapter-hyphenated-chapter-name`.
