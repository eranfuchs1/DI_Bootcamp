import operators

print(operators.addOperator(1,2))
print(operators.divideOperator(1,2))

from operators import addOperator, divideOperator

print(addOperator(1,2))
print(divideOperator(1,2))

from operators import addOperator as add, divideOperator as divide

print(add(1,2))
print(divide(1,2))
