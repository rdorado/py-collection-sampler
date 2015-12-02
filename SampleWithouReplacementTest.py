

def main(argv):
  sampler = SampleWithouReplacementModel(2, [0,1,1,1,0,1,1])

  for i in range(2):
    print sampler.next(0)
    print sampler.next(1)


if __name__ == "__main__":
  main(sys.argv[1:])
