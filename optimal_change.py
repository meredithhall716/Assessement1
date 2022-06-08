from collections import Counter
import math

# write a function taking in two arguments: item_cost, amount_paid
# return a string describing the least amount of change possible
# convert item_cost and amount_paid to pennies
# create a remainder variable and get remainder of amount_paid-item_cost
# initialize empty answer
# loop through list and find the largest denominations smaller than remainder
# add found denominations to answer
# if remainder = 0, convert answer denominations into correct values

def optimal_change(item_cost, amount_paid):
    if item_cost <= 0:
        return 'No change!'
    if item_cost == amount_paid:
        return 'No change!'
    if item_cost > amount_paid:
        return 'No change!'
    else:
        change = []
        answer = []
        output = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is '

        amount_paid = amount_paid * 100
        item_cost = item_cost * 100
        remainder = amount_paid - item_cost
       
        pennies_list = [10000, 5000, 1000, 500, 100, 25, 10, 1]

        # get correct change
        for i in pennies_list:
            while remainder:
                if i <= remainder:
                    change.append(i)
                    remainder -= i
                else:
                    break
        
        # print(change) = something like [100, 100, 100, 10, 1, 1, 1, 1, 1, 1, 1, 1].
        
        
        pennies = {
            '$100 bill': 10000,
            '$50 bill': 5000,
            '$10 bill': 1000,
            '$5 bill': 500,
            '$1 bill': 100,
            'quarter': 25,
            'dime': 10,
            'penny': 1
        }

        # loop through the change list and the pennies dictionary to match the correct change with the correct string.
        for i in change:
            for key in pennies:
                if i == pennies[key]:
                    answer.append(key)
                    counts = {item:answer.count(item) for item in answer}
        
        # print(counts) = something like {'$1 bill': 3, 'dime': 1, 'penny': 8}.
        
        # loop through dictionary and put it into the output string
        for key, value in counts.items():
            if key != list(counts.keys())[-1] and value > 1:
                output = output + f'{value} {key}s, '
            elif key != list(counts.keys())[-1]:
                output = output + f'{value} {key}, '
            elif list(counts.keys()) and value > 1:
                output = output + f'and {value} {key}s.'
            else:
                output = output + f'and {value} {key}.'
    
    return(output)
        
# optimal_change(56.82, 60)
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = 0
        
        # for i in answer:
        #     if answer[0] == answer[1]:
        #         count = count + 1
        
       
       
        # for i in pennies_list: 
        #     if i in currency:
        #         print(str(currency[i]))
        #     else:
        #         return False
        

 # for key in change.keys():
    #     if math.floor(remainder/change[key]):
    #         remainder %= change[key]
    #         answer.update(change[key])
    #         # answer.append(change[key])

    #         print(answer)
    #         print(remainder)

    # for i in range(len(change)):
    #         if remainder > change[i]:
    #             remainder = change[i] - remainder

    # for values in pennies:
    #     while remainder > pennies[values]:
    #         if values in answer:
    #             answer[values] += 1
                
    #         else:
    #             answer[values] = 1
    #         remainder -= pennies[values]
       