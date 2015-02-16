from math import sqrt;

__author__ = 'user'

allusers = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
                      "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5,
                      "The Strokes": 2.5, "Vampire Weekend": 2.0},

         "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
                  "Deadmau5": 4.0, "Phoenix": 2.0,
                  "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},

         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
                  "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                  "Slightly Stoopid": 1.0},

         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
                 "Deadmau5": 4.5, "Phoenix": 3.0,
                 "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                 "Vampire Weekend": 2.0},

         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
                    "Norah Jones": 4.0, "The Strokes": 4.0,
                    "Vampire Weekend": 1.0},

         "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0,
                    "Norah Jones": 5.0, "Phoenix": 5.0,
                    "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                    "Vampire Weekend": 4.0},

         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
                 "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},

         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
                      "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                      "The Strokes": 3.0}
}



def look_users():
    print allusers["Veronica"]


def mahattan(userlist1, userlist2):
    """
    :param userlist1:
    :param userlist2:
    :return:
    """
    distance = 0
    for key1 in userlist1:
        if key1 in userlist2:
            distance += abs(userlist1[key1] - userlist2[key1])

    return distance

def getNearestNeighbor(username, users):
    """

    :param username:
    :param users:
    :return:
    """

    distances =[]

    for user in users:
        if user != username:
            distance = mahattan(allusers[user], allusers[username])
            distances.append((distance, user))
    distances.sort()

    return distances

def recommend(username, users):
    """

    :param username:
    :param users:
    :return:
    """
    nearest = getNearestNeighbor(username, users)[0][1]
    print nearest
    recommendations = []
    nearestrating = allusers[nearest]
    userrating = allusers[username]


    for item in nearestrating:
        if not item in userrating:
            #print "append"
            #print item
            recommendations.append((item, nearestrating[item]))
            #print recommendations

    recommendations.sort()

    return recommendations


if __name__ == '__main__':
    #look_users()
    #print mahattan(allusers["Sam"], allusers["Veronica"])
    #print getNearestNeighbor("Sam", allusers)

    print recommend("Hailey", allusers)