import math
# write a function taking in two arguments: item_cost, amount_paid
# return a string describing the least amount of change possible
# convert item_cost and amount_paid to pennies
# create a remainder variable and get remainder of amount_paid-item_cost
# initialize empy answer
# find the largest denomination smaller than remainder
# add found denomination to answer
# if remainder = 0, convert answer denominations into correct values

def optimal_change(item_cost, amount_paid):
    if item_cost <= 0:
        return 'No change!'
    else:
        answer = []
        amount_paid = amount_paid * 100
        item_cost = item_cost * 100
        remainder = amount_paid - item_cost
        
        change = [1, 10, 25, 100, 500, 1000, 2000, 5000, 10000]
        print(remainder)
    
        i = len(change) - 1
        
        while i > 0:
            if remainder >= change[i]:
                remainder -= change[i]
                i.repeat(answer.append(change[i]))
            i -= 1
        
        print(remainder)
        print(answer)
        # for i in range(len(answer)):
            



optimal_change(1.50, 5)


 # for key in change.keys():
    #     if math.floor(remainder/change[key]):
    #         remainder %= change[key]
    #         answer.update(change[key])
    #         # answer.append(change[key])

    #         print(answer)
    #         print(remainder)