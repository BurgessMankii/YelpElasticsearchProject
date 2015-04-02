import os
import re


class Restaurant(object):
    # TODO:SEE WHAT ELSE SHOULD BE THE FIELDS
    def __init__(self, restaurant_name, reviews, location):
        self.restaurant_name = restaurant_name
        self.reviews = reviews


class Review(object):
    # TODO:SEE WHAT ELSE SHOULD BE THE FIELDS
    def __init__(self, restaurant_name, review_text, author):
        self.restaurant__name = restaurant_name
        self.review_text = review_text

def isTitleLine(line):
    return line.endswith('Yelp</title>')
def get_title_type_location(lines):
    info = []
    for line in lines:
        if isTitleLine(line):
            info = re.findall('\<title\>([^-]*) - ([^-]*) - ([^-]*MA)',line)
    return info


#Every page only contains 40 reviews, following

#get 40 reviews in the text
def get_review_text(text):
    #\<p itemprop\="description"
    rt = re.findall('\<p itemprop\="description" lang\="en"\>(.*)\<\/p\>',text)
    print len(rt)
    return rt


#get 40 dates in the text
def get_date(text):
    #\<p itemprop\="description"
    rt = re.findall('\<meta itemprop\="datePublished" content\=(.*)\>',text)
    print len(rt)
    return rt

def get_reviews(text):
    # get the part that contains all the reviews
    rt = re.findall('\<div class\="review\-list"\>(.*)\<div class\="review\-pager"\>',text,re.DOTALL)
    return rt[0]

def get_single_reviews(text):
    #return a list of raw text reviews
    # get the part that contains all the reviews
    # currently, for all 40 reviews, only able to get 38~39 of them. some loss here
    rt = re.findall('\<div class\="review review\-\-with\-sidebar"(.*?)\</li\>\s*\</ul\>\s*\</div\>\s*\</div\>\s*\</div\>\s*\</div\>\s*\</li\>\s*\<li\>',text,re.DOTALL)
    return rt

def get_author_name(single_review):
    rt = re.findall('\<meta itemprop\="author" content\="(.*)"\>', single_review)

    return rt



if __name__ == '__main__':
    for file in os.listdir(os.getcwd()):
        if file.endswith('html'):
            f = open(file,'r')
            text = f.read()
            lines = text.split('\n')
            review_text = get_reviews(text)
            reviews_list = get_single_reviews(review_text)
            for single_review in reviews_list:
                # TODO: MAIN EXTRACTION HERE, WRITE METHODS TO EXTRACT REVIREW_TEXT, AUTHOR_NAME(DONE), DATE, ETC
                print get_author_name(single_review)







