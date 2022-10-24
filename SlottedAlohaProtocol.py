import random
import time




class Aloha:
    def __init__(self, freq, stations_num, slots_num):
        self.freq = freq
        self.stations_num = stations_num
        self.slots_num = slots_num

        self.slots = self.__provide_slots_to_all()
        # print(self.slots)

    def __provide_slots_to_a_station(self):
        random.seed(time.time_ns())
        print(time.time_ns())
        time.sleep(random.randint(0, 2))
        arr = [i for i in range(self.slots_num)]
        random.shuffle(arr)
        ans = arr[:3]
        return ans


    def __provide_slots_to_all(self):
        slots = {}
        for j in range(self.stations_num):
            # random.seed(time.time_ns())
            slots[j] = self.__provide_slots_to_a_station()
        return slots

    def show_allocated_slots(self):
        for j in range(self.slots_num+1):
            print(j, end='\t')
        
        for k, v in self.slots.items():
            v.sort()
            print()
            for val in v:

                for p in range(val):
                    print('\t', end = "    ")
                if(val==0):
                    print(end="    ")
                print(k)

        print()
        




freq = 3
stations_num = 3
slots_num = 10


a = Aloha(freq, stations_num, slots_num)

a.show_allocated_slots()

    


















