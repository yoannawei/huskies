import random

tinyurl_list = []
captions = []
tinyurl_caption = {}

def open_text(filename):
    return open(filename)

def create_url_list(txt):
    #for line in txt:
    #    tinyurl_list.append(line.rstrip('\n'))
    url_map = map(lambda line: tinyurl_list.append(line.rstrip('\n')), txt)
    return list(url_map)

def print_tiny_url_list():
    # for tinyurl in tinyurl_list:
    #   print(tinyurl)
    return list(map(lambda x: print(x), tinyurl_list))

def select_random(my_list):
    return random.choice(my_list)

def add_caption(caption):
    captions.append(caption)

def create_dict(keys, values, tinyurl_caption):
    for i in range(len(keys)):
        tinyurl_caption[keys[i]] = values[i]
    return tinyurl_caption

def return_tinyurl_caption(key):
    return tinyurl_caption[key]

def print_captions():
    #for caption in captions:
        #print(caption)
    map(lambda caption: print(caption), captions)

def main():

    add_caption('husky puppy drives')
    add_caption('husky listens to banana phone')
    add_caption('chocolate husky puppy on floor')
    add_caption('siberian husky puppy in meadow')
    add_caption('a bunch of husky puppies')
    add_caption('white husky puppies in the snow')
    print_captions()

    create_url_list(open_text('shortened_url_list.txt'))

    create_dict(captions, tinyurl_list, tinyurl_caption)

    print(tinyurl_caption)

    print('random selection:', select_random(captions))

    #test run print(return_tinyurl_caption)
    #print(return_tinyurl_caption('husky listens to banana phone'))
    return

main()
