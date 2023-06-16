import utilities
import Random.choose
print(utilities)
l = Random.choose.generate()
for i in range(2):
    print(l[i])
print(utilities.multiply(l[0], l[1]))
