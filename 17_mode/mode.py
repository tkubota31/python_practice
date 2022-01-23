def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    #loop through and count how many times each numbers shows up
    count = {}
    for num in nums:
        count[num] = count.get(num,0) + 1
#find which one appears most often
    max_val = max(count.values())

#loop through key value pair and see if it matches with max val
    for (key,val) in count.items():
        if val == max_val:
            return key
