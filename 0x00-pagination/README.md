# REST API Design - Pagination


## TASKS

[0-simple_helper_function.py](https://linktodocumentation)

Write a function named index_range that takes two integer arguments page and page_size

[1-simple_pagination.py](https://linktodocumentation)

implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10

[2-hypermedia_pagination.py](https://linktodocumentation)

eplicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

[3-hypermedia_del_pagination.py](https://linktodocumentation)

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.


Requirements/Behavior:

Use assert to verify that index is in a valid range.
If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
If they request the next index (10) with page_size 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.
