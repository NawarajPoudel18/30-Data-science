import modules #this is the module being called here
from modules import c_to_f #this is the specific function being called from modules
from modules import c_to_f as c #this is the specific function being called from modules and being inalized as c
import modules as m #this is the modules being called and being inilised as m

# print(modules.hello("nawaraj"))
# print(modules.add(1,9))
# print(modules.sub(1,9))
# print(modules.div(1,9))
# print(modules.mul(1,9))

print(modules.c_to_f(10)) # this is being called from "import modules"
print(c_to_f(10)) #this is being called from "from modules import c_to_f"
print(c(10)) #this is being called from "from modules import c_to_f as c"
print(m.c_to_f(10))  #this is being called from "import modules as m"



