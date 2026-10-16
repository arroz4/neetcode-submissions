class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        # print(self.d)
        value = self.d.pop(key)
        self.d[key]=value
        return value

        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
            self.d[key] =value ## if key already exists push to newer location
            return 
        elif len(self.d)< self.capacity:
            self.d[key] =value ## If there is capacity left add new value
        else:
            oldest = next(k for k ,v in self.d.items()) ## Tuple uncpacking for getting oldest key
            self.d.pop(oldest) # remove oldest key value
            self.d[key] =value ## Add new key value