import random

class SampleWithouReplacementModel:
   
   def __init__(self, elements, sample):
     self.n = len(sample)
     self.sample = sample
     self.mask = [0 for x in range(self.n)]
     self.nselected = [0 for x in range(elements)]
     self.maxs = [sample.count(x) for x in range(elements)]

   def next(self, element):
#     if self.nselected >= self.maxs: raise Exception
     
     rand = int(random.random()*(self.maxs[element] - self.nselected[element]))  
     count = 0
     for i in range(self.n):
       if self.sample[i] == element and self.mask[i] != 1:
         if rand == count:            
           self.mask[i] = 1
           self.nselected[element] = self.nselected[element] + 1
           return i
         else: count = count + 1



def main(argv):
  sampler = SampleWithouReplacementModel(2, [0,1,1,1,0,1,1])

  for i in range(2):
    print sampler.next(0)
    print sampler.next(1)


if __name__ == "__main__":
  main(sys.argv[1:])
