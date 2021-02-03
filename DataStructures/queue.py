class Queue:
    size = 0
    queue = []

    def __init__(self, max_size=100):
        self.max_size = max_size

    def enqueue(self, data):
        if self.size >= self.max_size:
            return False

        self.queue.append(data)
        self.size += 1

    def dequeue(self, amount = 1):
        if self.size == 0:
            return False
        elif amount > self.size:
            return False
        else:
            temp = []
            for i in range(amount):
                temp.append(self.queue.pop(0))
                self.size -= 1
            if temp.count() == 1:
                return temp[0]
            else:
                return temp

    def print_queue(self):
        for i in self.queue:
            print(i)