
D = "~"



class Sender():
    def __init__(self):
        pass

    def char_stuff_it(self, stream, st_pt, end_pt):
        st_part = stream[0:st_pt]
        real_msg = self.char_stuffing_msg(stream[st_pt:end_pt])
        end_part = stream[end_pt:]

        return st_part + real_msg + end_part

    def char_stuffing_msg(self, M):
        ans_msg = ""
        
        ctr = 0
        tmp_str = D
        for ch in M:
            
            if ch==D:
                ctr += 1
            else:
                if(ctr != 0):
                    for j in range(ctr):
                        tmp_str = tmp_str + D
                    ans_msg = ans_msg + tmp_str + ch
                    tmp_str = D
                    ctr = 0
                else:
                    ans_msg = ans_msg + ch
                
        ans_msg = D + ans_msg + D
        return ans_msg




class Receiver():
    def __init__(self, ):
        pass

    def decode_msg(self, stream):
        ans = ""
        st_pt = 0
        end_pt = len(stream)
        first_d_got = False

        end_pt_reached=False
        ctr = 0
        tmp = ""
        for i, ch in enumerate(stream):
            if(not first_d_got):
                if(ch==D):
                    st_pt = i+1
                    first_d_got = True
            else:
                if(ch==D):
                    ctr += 1
                else:
                    if(ctr==1):
                        end_pt = i-2
                        end_pt_reached = True
                        break
                    elif(ctr > 1):
                        tmp = D * (ctr-1)
                        ans = ans + tmp + ch
                        tmp = ""
                        ctr = 0
                    else:
                        ans += ch


        return ans
        



        












r = Receiver()
s = Sender()

t = int(input("Enter the number of test cases:: "))

for i in range(t):
    D = input("Please enter a character to use as delimiter:: ")
    stream = input("Please enter the stream sentence on which to perform character stuffing:: ")
    print()
    st_pt = int(input("Please enter the starting pt index of your message in the stream:: "))
    end_pt = int(input("Please enter the ending pt index of your message in the stream:: "))

    char_stuffed_stream = s.char_stuff_it(stream, st_pt, end_pt)
    print()

    print("The stream being received by the Receiver is -> ", char_stuffed_stream)
    received_msg = r.decode_msg(char_stuffed_stream)
    print("The message decoded by the Receiver is -> ", received_msg)
    print()
    print()






























