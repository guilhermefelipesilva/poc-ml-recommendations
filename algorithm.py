from dataset import user_reviews

from math import sqrt

def euclidian (user1, user2):
    similar = {}

    for  item in user_reviews[user1]:
        if item in user_reviews[user2]: similar['item'] = 1

    if len(similar) == 0: return 0

    value = sum([pow(user_reviews[user1][item] - user_reviews[user2][item], 2) 
                    for item in user_reviews[user1] if item in user_reviews[user2]])

    return 1 / (1 + sqrt(value))


def get_similar(user):
    similar = [(euclidian(user, other), other) 
                for other in user_reviews if other != user]
    similar.sort()
    similar.reverse()
    return similar

def get_recommendations(user):
    totals = {}
    sumSimilar = {}

    for other in user_reviews:
        if other == user: continue
        similiar = euclidian(user, other)

        if similiar <= 0: continue
        
        for item in user_reviews[other]:
            if item not in user_reviews[user]:

                totals.setdefault(item, 0)
                totals[item] += user_reviews[other][item] * similiar

                sumSimilar.setdefault(item, 0)
                sumSimilar[item] += similiar

    rankings = [(total / sumSimilar[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()

    return rankings