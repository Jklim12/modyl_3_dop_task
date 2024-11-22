def data_structure(n):
    total_sum = 0
    if isinstance(n,(int, float)):
        total_sum += n
    elif isinstance(n,str):
        total_sum += len(n)
    elif isinstance(n,(list, tuple, set)):
        for item in n:
            total_sum += data_structure(item)
    elif isinstance(n,dict):
        for key, value in n.items():
            total_sum += data_structure(key)
            total_sum += data_structure(value)

    return total_sum
data_structure_1= [

    [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]
print(data_structure(data_structure_1))

