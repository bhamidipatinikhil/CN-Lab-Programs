import random
import time

# THere is a single lock which is with d, 
# d is able to encrypt sender's message into the lock and 
# send it to receiver, and then 
# d is able to decrypt it
# d is the ultimate master
# Nobody can decrypt the message encrypted by d

# This is only an honest attempt to simulate the above rules


class DesSimulation():
    def __init__(self, security):
        p, q = self.huge_prime_numbers(security)
        self.n = p*q
        self._p = p
        self._q = q



    def encrypt_msg(self, msg):
        min_factor = min(self._p, self._q)
        max_factor = max(self._p, self._q)
        encr_msg = msg*self.n*max_factor + min_factor
        return encr_msg

    def decrypt_msg(self, msg):
        min_factor = min(self._p, self._q)
        max_factor = max(self._p, self._q)

        decr_msg = int((msg - min_factor)/(self.n*max_factor))
        return decr_msg


    @property
    def p(self):
        print("The p is a private variable, getters prohibited under the Nikhilian law!!")
    
    @p.setter
    def p(self, val):
        print("You are under arrest for trying to set the value of p")

    @property
    def q(self):
        print("The q is a private variable, getters prohibited under the Nikhilian law!!")

    @q.setter
    def q(self, val):
        print("You are under arrest for trying to set the value of q")


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



d = DesSimulation(security=5000)

msg = 22

encr_msg = d.encrypt_msg(msg)
decr_msg = d.decrypt_msg(encr_msg)

print(f'The value of n is publicly known:: {d.n}')
print(f'\nThe Encrypted msg is publicly known, but no one can decrypt it:: {encr_msg}')
print(f'The decrypted msg, which can only be decrypted by d is:: {decr_msg}')












