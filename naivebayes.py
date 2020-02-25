from math import log2


N_TRAIN = 5000
N_TEST = 1000

def f(x,y,image,eps):
    count = 0
    for i in range(x,len(image)):
        for j in range(y,len(image)):
            if image[i][j] != ' ':
                count += 1
    size = len(image)*len(image)
    if count >= int(eps * size):
        return 1
    else:
        return 0


def f_raw_count(x,y,image):
    count = 0
    for i in range(x,len(image)):
        for j in range(y,len(image)):
            if image[i][j] != ' ':
                count += 1

    return count


#parser for the training image data
def read_image_data(filename):
    data = list()
    digit = list()
    with open(filename, "r") as file:
        images = file.readlines()

    found_digitstart = False
    found_digitend = False
    found_char = False
    for line in images:
        for i in range(0, 29):
            #check the line to see if it has text
            if line[i] == '#' or line[i] == '+':
                found_char = True
                found_digitend = False
                found_digitstart = True
        if found_digitstart == True and found_char == False:
            found_digitend = True
            data.append(digit)
            digit = list()
            found_digitstart = False
        if found_char:
            found_char = False
            if found_digitstart == False:
                found_digitstart = True
            else:
                digit.append(line)
    return data



#parser for training label data
def read_label_data(filename):
    labels = list()
    with open(filename, "r") as file:
        labels = file.readlines()

    labels = [item.replace('\n', '') for item in labels]
    return labels


#for debugging
def print_image(image):
    for line in image:
        print(line)

def get_image(image):
    return [line for line in image]

def count_training_instances(image_vectors,label):
    count = 0
    for image in image_vectors:
        if image[3] == label:
            count += 1
    return count

def create_feature_vectors(image_data,label_data,N):
    i = 0
    image_vectors = []
    for image in image_data[0:N]:
        image_vectors.append([symbol_per_line('#', image),
                              symbol_per_line('+', image),
                              symbol_per_line(' ', image),
                              label_data[i]])
        i += 1
    return image_vectors


def count(data,predicate):
    return sum([1 for item in data if predicate(item)])
#these functions generate specific features
def symbol_per_line(symbol,mystrs):
    sum = int()
    for line in mystrs:
        sum += line.count(symbol)

    return int(sum / len(mystrs))


def get_training_instances(image_vectors,label):
    return [item for item in image_vectors if item[3] == label]

def avg(items):
    return sum(items) / len(items)



# calculate the probabilities for the features
def calculate_prob_dist(image_vectors,y):

    prob = list()
    for label in y:
        num = count_training_instances(image_vectors, label)
        denom = (count_training_instances(image_vectors, label) / 5000) + (
                (5000 - count_training_instances(image_vectors, label)) / 5000)
        prob.append(num / denom)

    return prob


'''
def predict(image_vectors):
    # these are the labels
    y = [str(num) for num in range(0, 10)]

    # these are the predicted labels
    yp = [count_training_instances(image_vectors, str(label)) / 5000 for label in range(0, 10)]
    return yp
'''


''''

def liklihood(pa, pb, pc, pd, data):

    if pa != None:
        num = len([[a, b, c, d] for [a, b, c, d] in data
               if  a == pa and d == pd])
    elif pb != None:
        num = len([[a, b, c, d] for [a, b, c, d] in data
               if b == pb and d == pd])
    elif pc != None:
        num = len([[a, b, c, d] for [a, b, c, d] in data
               if c == pc and d == pd])

    else:
        print("Error: must specify exactly one event.")
        exit(-1)

    denom = len([[a, b, c, d] for [a, b, c, d] in data
                 if d == pd])

    return num/denom
'''


def prior(label,data):
    num = len([[a, b, c, d,e] for [a, b, c, d,e] in data
               if e == label])

    denom = len(data)

    return num/denom


def prob(num):
    print(f"{round(num*100.0,2)}%")
#print("number of images: " + str(len(image_data)))
#print("number of labels: " + str(len(label_data)))
#print("number of image vectors: " + str(len(image_vectors)))
#lst = [[item[0], item[1], item[2], int(item[3])] for item in get_training_instances(image_vectors,'3')[0:3000]]

#print([item[1] for item in lst])
#print("sanity check (does the distribution sum to 1?): " + str(sum(yp)))

#print(image_vectors)
#print("size: " + str(len(image_vectors)))

#print(image_vectors)
'''
for image in image_data:
    for item in image:
        print(item)
'''

def getByFeature(f,data):
    if f == 1:
        return [a for [a, b, c, d, e] in data]
    elif f == 2:
        return [b for [a, b, c, d, e] in data]
    elif f == 3:
        return [c for [a, b, c, d, e] in data]
    elif f == 4:
        return [d for [a, b, c, d, e] in data]



def getByLabel(label,data):
    return [[a, b, c, d, label] for [a, b, c, d, e] in data]








def feature_prob(data,feature=None):
    count = 0
    for item in data:
        if item[feature] == 1:
            count += 1
    return count / len(data)

def make_feature_vector(image_data,label_data,n_items,eps=None):
    vectors = list()
    for i in range(0,n_items):
        image = image_data[i]
        label = label_data[i]
        n = int(len(image)/2)
        if eps == None:
            vectors.append([f_raw_count(0, 0, image), f_raw_count(0, int(n / 2), image), f_raw_count(int(n / 2), 0, image),
                            f_raw_count(int(n / 2), int(n / 2), image), label])
        else:
            vectors.append([f(0,0,image,eps),f(0,int(n/2),image,eps),f(int(n/2),0,image,eps),f(int(n/2),int(n/2),image,eps), label])
    return vectors

