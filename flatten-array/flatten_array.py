def flatten(iterable):
    flat_list = []
    def flat(it):
        for i in it:
            if type(i) == list:
                flat(i)
            elif i != None:
                flat_list.append(i)
    flat(iterable)
    return flat_list 
