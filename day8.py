import modules #this is the module being called here
from modules import c_to_f #this is the specific function being called from modules
import modules as m #this is the modules being called and being inilised as m

# print(modules.hello("nawaraj"))
# print(modules.add(1,9))
# print(modules.sub(1,9))
# print(modules.div(1,9))
# print(modules.mul(1,9))

print(modules.c_to_f(10))
print(c_to_f(10))
print(m.c_to_f(10))



