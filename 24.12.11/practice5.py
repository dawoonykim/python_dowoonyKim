import bbb.cm2 as bc
import bbb.cm2
import ccc
from modules.mylib.food import name, cook, eat
from modules.mylib import food
print("from modules.mylib import food")
print(food.name)
food.cook()
food.eat()

print("from modules.mylib.food import name, cook, eat")
print(name)
cook()
eat()

ccc.abc()
ccc.add(1, 2)

bbb.cm2.print_bbb()

bc.print_bbb()
