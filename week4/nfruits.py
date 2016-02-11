def nfruits1 (fruit_basket, fruit_eat_pattern) : 
    '''
    Function to find out maximum fruits count in basket based on pattern of
    eating.
    
    After each fruit is consumed (except the last one which is consumed just on 
    reaching the campus), fruits are refilled of each type other than the last
    consumed fruit.
    
    Inputs :
    ========
    fruit_basket :: A non-empty dictionary containing type of fruit and 
                    its quantity initially with Python when he leaves home
                    (length < 10)

    fruit_eat_pattern :: A string pattern of the fruits eaten
    '''
    
    # Count of fruit pattern to ensure addition of fruit is not carried out 
    # in basket for last fruit consumed
    fruitseatencount = len(fruit_eat_pattern)
    
    # Iterate over all fruit in pattern
    for pythonfruit in fruit_eat_pattern :
        # Reduce count of fruit as it is consumed
        fruit_basket[pythonfruit] = max(fruit_basket[pythonfruit]-1 , 0)
        
        # Generate keylist of fruits for refill
        fruitlist = fruit_basket.keys();
        # Last consumed fruit is removed as no refil for it
        fruitlist.remove(pythonfruit)
        
        
        fruitseatencount -= 1
        # To check for the last fruit in pattern basket is not refilled
        if fruitseatencount != 0 :
            # Refill the basket for availble fruits in fruitlist
            for fruit in fruitlist:
                fruit_basket[fruit] +=1
    
    # Return the maximum count from fruits
    return max(fruit_basket.values())
    
    
def nfruits2 (fruit_basket, fruit_eat_pattern) : 
    '''
    Function to find out maximum fruits count in basket based on pattern of
    eating.
    
    After each fruit is consumed (except the last one which is consumed just on 
    reaching the campus), fruits are refilled of each type other than the last
    consumed fruit.
    
    Inputs :
    ========
    fruit_basket :: A non-empty dictionary containing type of fruit and 
                    its quantity initially with Python when he leaves home
                    (length < 10)
    
    fruit_eat_pattern :: A string pattern of the fruits eaten
    '''
    
    # Count of fruit pattern to ensure addition of fruit is not carried out 
    # in basket for last fruit consumed
    
    
    # Iterate over all fruit in pattern
    for pythonfruit in fruit_eat_pattern[:-1] :
        
        # Refill the basket for availble fruits in fruitlist
        for fruit in fruit_basket.keys():
            fruit_basket[fruit] +=1
        
        # Reduce count of fruit as it is consumed
        fruit_basket[pythonfruit] = max(fruit_basket[pythonfruit]-2 , 0)
    
    fruit_basket[fruit_eat_pattern[-1]] -=1 
    
    # Return the maximum count from fruits
    return max(fruit_basket.values())