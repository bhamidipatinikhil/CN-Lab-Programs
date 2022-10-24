
'''
CRC 12-> x^12 + x^11 + x^3 + x^2 + x^1 + x^0
1100000001111

CRC 3-> x^3 + x + 1
1011

'''


def btoi(str):
    return int(str, 2)

def itob(n):
    return bin(n)[2:]

def bdc(dd, ds):
    q, r = binary_division(bin(dd)[2:], bin(ds)[2:])
    return int(q, 2), int(r, 2)

def qr(dd, ds):
    return int(dd/ds), dd % ds

def binary_division(dividend, divisor):
    quot, rem = qr(btoi(dividend), btoi(divisor))
    return itob(quot), itob(rem)


class Station:
    def __init__(self, name, k):
        self.name = name
        self.k = k
    
    def send_msg(self, msg):
        qstr, rstr = binary_division(msg, self.k)
        to_send = itob(btoi(msg) + btoi(rstr))
        # to_send = msg + rstr
        return to_send

    def check_msg(self, rec_msg):
        q, r = binary_division(rec_msg, self.k)
        return btoi(r)==0




msg = "100100"
k = "1101"

sender = Station("sender", k)
receiver = Station("receiver", k)


msg_received_successfully = receiver.check_msg(sender.send_msg(msg))

print(msg_received_successfully)


# print(bdc(26, 7))












