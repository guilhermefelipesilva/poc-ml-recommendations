from dataset import user_reviews
from dataset_invert import movie_reviews

from math import sqrt

def euclidian (dataset, user1, user2):
    similar = {}

    for  item in dataset[user1]:
        if item in dataset[user2]: similar['item'] = 1

    if len(similar) == 0: return 0

    value = sum([pow(dataset[user1][item] - dataset[user2][item], 2) 
                    for item in dataset[user1] if item in dataset[user2]])

    return 1 / (1 + sqrt(value))


def get_similar(dataset, user):
    similar = [(euclidian(dataset, user, other), other) 
                for other in dataset if other != user]
    similar.sort()
    similar.reverse()
    return similar

def get_recommendations(dataset, user):
    totals = {}
    sumSimilar = {}

    for other in dataset:
        if other == user: continue
        similiar = euclidian(dataset, user, other)

        if similiar <= 0: continue
        
        for item in dataset[other]:
            if item not in dataset[user]:

                totals.setdefault(item, 0)
                totals[item] += dataset[other][item] * similiar

                sumSimilar.setdefault(item, 0)
                sumSimilar[item] += similiar

    rankings = [(total / sumSimilar[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()

    return rankings