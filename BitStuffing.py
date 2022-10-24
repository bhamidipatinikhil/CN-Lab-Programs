


D = "01111110"

L=8

M=5

T = "~"


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, stream):
        self.root = Node(stream[0])
        curr = self.root
        n = len(stream)
        for i in range(1, n):
            tmp = Node(stream[i])
            curr.next = tmp
            curr = curr.next
    
    def print_list(self):
        curr = self.root

        while(curr!=None):
            print(f'{curr.val}->', end="")
            curr = curr.next
        print()


class Sender():
    def __init__(self):
        pass

    def bit_stream_it(self, stream):
        ll = LinkedList(stream)
        # ll.print_list()
        
        curr = ll.root
        tmp_ctr=0
        while(curr!=None):
            if(curr.val=='1'):
                tmp_ctr += 1
                if(tmp_ctr == 5):
                    nexter = curr.next
                    buffer_node = Node('0')
                    curr.next = buffer_node
                    buffer_node.next = nexter
                    tmp_ctr = 0
                    curr = buffer_node
                    continue
            else:
                tmp_ctr = 0
            curr = curr.next
        

        # ll.print_list()
        curr = ll.root
        ans_stream = ""
        while(curr!=None):
            ans_stream += curr.val
            curr = curr.next
        
        return ans_stream


s = Sender()

stream = "0111111000000000000000000"

bit_stuffed_stream = s.bit_stream_it(stream)

print(bit_stuffed_stream)






