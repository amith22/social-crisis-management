from crisis.models import EventModel
from crisis.sentimentanalyzer import getCommentSentiment
from nltk.tokenize import word_tokenize

def isCrisisPost(comment):

    tokens = word_tokenize(comment)
    tokenlist = []

    for i in tokens:
        if len(i) >= 3 and i.isalpha():
            tokenlist.append(i)
    flag = 0

    for event in EventModel.objects.all():
        print("for 1")
        for token in tokenlist:
            print("for 2 :",token)
            for keyword in event.keywords.split(","):
                print("for 3 :", token,keyword)
                if token in keyword:
                    flag = 1

        print(event.subcategory,flag)

        if flag == 1:
            sentiment = getCommentSentiment(comment)
            print("sentiment ",sentiment , event.subcategory)
            if sentiment in "negative":
                print("final if")
                return [True, event.subcategory, sentiment]

    return [False,"",""]

