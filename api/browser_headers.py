from fake_headers import Headers

def getBrowserHeaders(limit):
    headersList=[]
    header = Headers(
        # generate any browser & os headeers
        headers=False  # don`t generate misc headers
    )
    for i in range(limit):
        headersList.append(header.generate())
    return headersList



