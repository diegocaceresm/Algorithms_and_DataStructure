
###########################
#      LINKED LIST        #
###########################

"""
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
"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.node_next_index = None

    def append_new_node(self,data):
        current_head = self
        new_node = Node(data)
        while current_head.node_next_index is not None:
            current_head = current_head.node_next_index
        current_head.node_next_index = new_node

    def display(self):
        node_list = []
        display_node = self
        while display_node.node_next_index is not None:
            display_node = display_node.node_next_index
            node_list.append(display_node.data)
        print(node_list)


###############################
#      TIME COMPLEXITY        #
###############################

import matplotlib.pyplot as plt
import random
from time import perf_counter

ranges = [1000, 2000, 4000, 8000, 16000, 32000]
r_extime = [0, 0, 0, 0, 0, 0]


for ind in range(len(ranges)):
    list_a = [*range(1, ranges[ind], 1)]
    random.shuffle(list_a)

    start = perf_counter()
    for i in list_a:
        trial_list = Node()
        trial_list.append_new_node(i)
    end = perf_counter()
    r_extime[ind] = end - start

plt.clf()
plt.style.use('seaborn-darkgrid')
plt.plot(ranges,r_extime,label = 'Rand', marker ='o', markerfacecolor ='blue', color = 'skyblue')
plt.title("Time Complexity - Linear Function", loc='left', fontsize=12, fontweight=0, color='Black')
plt.xlabel("Data Ranges")
plt.ylabel("Seconds")
plt.legend()
plt.show()





