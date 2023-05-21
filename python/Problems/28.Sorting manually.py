data_list = [15,25,35,45,5,30,10,50,40,20]

def desc():
    desc_list = []
    while data_list:
        mini = data_list[0]
        for x in data_list:
            if x > mini:
                mini = x
        desc_list.append(mini)
        data_list.remove(mini)
    print('Descending order',desc_list)

    asc_list = desc_list[::-1]
    print('Ascending order',asc_list)

desc()

