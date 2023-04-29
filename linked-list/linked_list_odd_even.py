# Given a linked list of size N, your task is to complete the function isLengthEvenOrOdd() which contains head of the linked list and check whether the length of linked list is even or odd.
# Input:
# The input line contains T, denoting the number of testcases. Each testcase contains two lines. the first line contains N(size of the linked list). the second line contains N elements of the linked list separated by space.
# Output:
# For each testcase in new line, print "even"(without quotes) if the length is even else "odd"(without quotes) if the length is odd.
# User Task:
# Since this is a functional problem you don't have to worry about input, you just have to  complete the function isLengthEvenOrOdd() which takes head of the linked list as input parameter and returns 0 if the length of the linked list is even otherwise returns 1.


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next  =  next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def get_head(self):
        return self.head

    def append(self, value):
        node = self.head
        while node.get_next():
            node = node.get_next()
        new_node = Node(value, None)
        node.set_next(new_node)	

    def delete(self, value):
        node = self.head
        prev = None
        while node:
            if node.get_value() == value:
                next_node = node.get_next()
                if prev:
                    prev.set_next(next_node)
                else:
                    self.head = next_node
            prev = node
            node = node.get_next()
    
    def display(self):
        node = self.head
        while node:
            print(node.get_value(), end = " ")
            node = node.get_next()

def count_linked_list_length(linked_list):
    head = linked_list.get_head()
    node =  head
    count = 0
    while node:
        count += 1
        node = node.get_next()
    return count

if __name__ == '__main__':
    
    node = Node(12, None)
    linked_list = LinkedList(node)
    linked_list.append(52)
    linked_list.append(10)
    linked_list.append(47)
    linked_list.append(95)
    linked_list.append(0)
    linked_list.display()
    print()

    count = count_linked_list_length(linked_list)
    if count % 2 == 0:
        print('even')
    else: 
        print('odd')		
	
				
		
			
	
