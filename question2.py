# TIME TAKEN: 30 MIN

class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data,None)
        else:
            currentNode = Node(data,None)
            currentPosition = self.head
            while currentPosition.next:
                currentPosition = currentPosition.next
            currentPosition.next = currentNode
                
        
    def print(self):
        if self.head is None:
            print('Singly Linked List is empty')
        
        ssl = self.head
        sslstr =''
        print('\nSingly Linked List:')
        while ssl:
            sslstr += str(ssl.data) 
            if ssl.next:
                sslstr += ' ---> '
            ssl = ssl.next
        print(f'{sslstr}\n')
        
    def getMiddleNode(self):
        if self.head is None:  
            print('Singly Linked List is empty')
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(f'The middle node is {slow.data}\n')
        
    
def insert_into_array():
    while True:
        try:
            array = input("Enter numbers separated by spaces (each between 1 and 100): ").split()
            if not array:
                print("Input cannot be empty! Please enter at least one number.")
                continue
            array = [int(x) for x in array]
                
            if all(1 <= x <= 100 for x in array):
                return array  # Return the valid array
            else:
                print("All numbers must be between 1 and 100. Please try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        
if __name__ == "__main__":
    ssl = SinglyLinkedList()
    array = insert_into_array()
    if array:
        for num in array:
            ssl.insert(num)
        
        ssl.print()
        ssl.getMiddleNode()