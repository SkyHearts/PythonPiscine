from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# height = [1.71, 1.65, 1.73, 1.95, 1.63, 123]
# weight = [65.3, 58.4, 63.4, 94.5, 72.9]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))

# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]
# $>
