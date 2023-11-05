from fake_useragent  import UserAgent

def getUserAgent(limit):
    userList=[]
    ua = UserAgent()

    for i in range(limit):
        userList.append(ua.random)
    return userList
