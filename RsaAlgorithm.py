import math
import random
import time

class Station:
    def __init__(self, name, security):
        self.name = name
        p, q = self.huge_prime_numbers(security)
        # print("p, q calculated", p, q)
        n = p*q
        self.n = n
        # print("n-> ", n)
        l = math.lcm((p-1), (q-1))  
        # print("l-> ", l)      
        e = self.rand_coprime(l)
        self.e = e
        # print("e->", e)
        d = self.calc_d(e, l)
        self._d = d
        # print("d->", d)

        self._public_key = [e, n]
        print(f'Public Key for Station {name} -> e: {e} | n: {n}')
        self._private_key = [d, n]
        print(f'Private Key for Station {name} -> d: {d} | n: {n}')
    

    def huge_prime_numbers(self, security):
        candidates = self.prime_eratosthenes(security)
        random.seed(time.time())
        return random.choice(candidates), random.choice(candidates)

    def prime_eratosthenes(self, n):
        composites = set()
        primes = []
        for i in range(2, n+1):
            if i not in composites:
                primes.append(i)
                for j in range(i*i, n+1, i):
                    composites.add(j)

        return primes

    def rand_coprime(self, l):
        candidates = []

        for j in range(2, l):
            if(math.gcd(j, l)==1):
                candidates.append(j)
        
        random.seed(time.time())
        return random.choice(candidates)

    def calc_d(self, e, l):
        i = 1
        while(True):
            if((e*i) % l == 1):
                return i
            else:
                i += 1

    def encrypt_msg(self, m, e, n):
        ans = 1

        for i in range(e):
            ans = (ans*m) % n

        return ans

    def decrypt_msg(self, c):
        ans = 1

        for i in range(self._d):
            ans = (ans*c) % self.n
        
        return ans


    @property
    def d(self):
        print("Access Prohibited")
    
    @d.setter
    def d(self, val):
        print("Setting Value Prohibited")

    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        print("Sorry, the public key cannot be changed by the user. It is assigned randomly and is read only")


    @property
    def private_key(self):
        print("Sorry, the private key cannot be read. Its a secret, But Good Luck Decoding it")
    
    @private_key.setter
    def private_key(self, value):
        print("Sorry, the private key cannot be set or assigned a value!!")


class Hacker(Station):
    def __init__(self, name):
        self.name = name
    

    def find_pq(self, n):
        candidates = super().prime_eratosthenes(n)

        for j in candidates:
            if n % j == 0:
                return j, int(n/j)

    def hack_public_key(self, arr):
        e = arr[0]
        n = arr[1]

        p, q = self.find_pq(n)
        l = math.lcm(p-1, q-1)
        d = super().calc_d(e, l)

        return [d, n]






sender = Station("sender", 5000)
receiver = Station("receiver", 5000)


msg = 222
print(receiver.decrypt_msg(sender.encrypt_msg(msg, receiver.e, receiver.n)))


print("\nStarting the Hacking Procedure")
hacker = Hacker("hacker")

print(f'The private key of {sender.name} is {hacker.hack_public_key(sender.public_key)}')
print(f'The private key of {receiver.name} is {hacker.hack_public_key(receiver.public_key)}')

























