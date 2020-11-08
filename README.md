# Algorithms_and_DataStructure

Class Asignment

Adding an element to an array is a time-consuming task, while accessing a random element has a constant time complexity.
For the majority of use cases, that makes total sense; however, there are also use cases where elements are only
accessed through iteration with no necessity of randomly accessing an element. A linked list would be a great container
for such cases. Your (individual) assignment is the development of a linked list. Using object-oriented programming,
define a class Node that will hold the data as well as a reference to the next element. The class Node also needs a
method insert that inserts a new element right after itself and before the previously next element. (18 points)

This insert method is always doing the same amount of operations and hence should have a constant time complexity.
Your second task is verifying this by creating differently sized lists and adding a new element somewhere (note that
finding the element is not part of calculating the time complexity; hence you could always enter an element after the
first position). (6 points)

Please create a repository on GitLab or GitHub and invite me as a collaborator. My GitLab user is vandonians,
and my GitHub user is vaheandonians. I am happy to look at the code and answer questions that you might have using
GitLab or GitHub, however, the full code needs to be posted as a .py file to this assignment. Please do not post and
Notebooks, but only directly executable .py files. (6 points)
