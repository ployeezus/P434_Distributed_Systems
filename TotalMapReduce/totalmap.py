mapperV = 0
reducerV = 0
reading_file = ""
out_file = ""


total_line = ""
total_dict = {}
# {the:}

def startMapper(user_input):
    ''' '[x, y, txt, txt]' --> split them and store them into the mapper'''
    global mapperV
    global reducerV
    global reading_file
    global out_file
    global total_line
    a = user_input
    print('a:', a)
    for element in user_input:
        a += str(element) + " "
    a = a.split() # turns into an array
    print('a:',a)
    mapperV = int(a[0])
    reducerV = int(a[1])
    reading_file = a[2]
    out_file = a[3]


def readingFile(user_input):
    try:
        print(user_input)
        startMapper(user_input)
        # print(reading_file)
        try:
            with open('book2.txt', 'r') as fileRead:
                line = fileRead.readlines()
                total_line = line
        except:
            print('Book Doesn;t exist')
        print(total_line)
        # remove uncessary lines
        newSentence = []
        for sentence in total_line:
            sentence = sentence.strip('\n')
            sentence = sentence.replace(".", "").replace("?","") # add more unn...
            newSentence.append(sentence)
        total_line = newSentence
        mapper()
        # print(newSentence)
    except:
        print('Something went wrong in the ReadingFile')


def mapper():
    """
        1. We have the array of sentences
        2. We need to loop through the specific line, split it, loop through it until the end line
        3. Write that dicitonary to mapper
        4. empty the dicitoary
    """
    global total_dict
    current_dict = {}
    current_mapper = 1
    for sentence in total_line:
        modf = sentence.split()  # = [This,is,cool]
        for index in modf:
            if index in current_dict:
                current_dict[index] += 1
            else:
                current_dict[index] = 1
            # total dict looper
        # Write it to a file, using curren_mapper
        with open("mapper_Index_{}.txt".format(current_mapper), "a+") as file:
            file.write(str(current_dict) + '\n')
        # total dict looper: {I:[5,1,1]}
        for index in current_dict.keys():
            if index not in total_dict:
                total_dict[index] = []
                total_dict[index].append(current_dict[index])
            else:
                # current_dict = {'This: 1, is:1, cool:1}
                # total_dict = {'This:[1], is:[1], }
                # total_dict = {this:[1], is:[], cool:[]}
                total_dict[index].append(current_dict[index])
        current_dict = {}
        current_mapper += 1 # 1, 2, 3--> 1
        if current_mapper > mapperV:
            current_mapper = 1
    reducer()
    

def reducer():
    """
        * have index counter for which reducer your on
        * have dict to indicate which file the first character will go to.
        example:
        reducer_counter = 1, we have n = 2
        reducer_dict = {}
            - This': [1, 1, 1]
            - is': [1, 1]
            - Earth: [1]
            - The: [1]
        * Example:
            1. reducer_dict = {'t':1}, then we increment the reducer_counter and check it too
            2. reducer_dict = {'t':1, i:2}, then ew incremnt and check
            3. reducer_dict = {'t':1, i:2, e:1}
    """

    reducer_dict = {}
    reducer_index = 1
    for key in total_dict.keys():
        character = key[0]
        if character not in reducer_dict:
            reducer_dict[character] = reducer_index
            # We write the current key abd value to the reducer_index which is where the reducer is going to be written in
            with open('reduce_{}.txt'.format(reducer_index), 'a+') as file:
                # get the key, get the value, then write it to a file
                where = key
                what =  total_dict[key]
                file.write(str({'{}:{}'.format(where, what)}) + '\n')
            reducer_index += 1
            if reducer_index > reducerV:
                reducer_index = 1
            
        else:
            # We access the value of the first character by doing this:
            # a = reducer_dict[character]
            # Then we write it to the specific file
            with open('reduce_{}.txt'.format(reducer_dict[character])) as file:
                where = key
                what =  total_dict[key]
                file.write(str({'{}:{}'.format(where, what)}) + '\n')
    output()
                



def output():
    with open(out_file, 'a+') as file:
        for key in total_dict.keys():
            whereKey = key
            whatValue = (total_dict[key])
            file.write(str({'{}:{}'.format(whereKey, sum(whatValue))}) + '\n')
            

a = [2,2,'book1.txt', 'total_out.txt']
# # print(str(a)
readingFile(a)
# # print(mapperV)
# # print(reducerV)
# # print(reading_file)
# # print(out_file)
# # print(total_line)
# print(total_line)
# print(total_dict)
