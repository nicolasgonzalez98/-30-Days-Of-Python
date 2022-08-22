class Statics:
    def __init__(self, array):
        self.array = array
    
    def sum(self):
        suma = 0
        for n in self.array:
            suma += n
        
        return sum(self.array)
    def min(self):
        return min(self.array)
    def describe(self):
        return f'''Sum: {self.sum()}
Min: {self.min()}
        '''
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statics(ages)

print(data.describe())