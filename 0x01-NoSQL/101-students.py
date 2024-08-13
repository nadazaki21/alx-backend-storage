# #!/usr/bin/env python3
# """ Task 14 """


# def top_students(mongo_collection):
#     """function that returns all students sorted by average score"""
#     for i in mongo_collection.find():
#         print(f"[{i['_id']}] {i['name']} - [{i['topics']}]")
#         sum_score = 0
#         for j in range(len(i["topics"])):
#             sum_score += i["topics"][j]["score"]
#         averageScore = sum_score / len(i["topics"])
#         # i.update_one({"_id" : i['_id']},{$set: {"averageScore": averageScore}})
#         mongo_collection.update_one(
#             {"_id": i["_id"]}, {"$set": {"averageScore": averageScore}}
#         )
#     return mongo_collection.find().sort("averageScore", -1)



#!/usr/bin/env python3
'''Task 14's module.
'''


def top_students(mongo_collection):
    '''Prints all students in a collection sorted by average score.
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students