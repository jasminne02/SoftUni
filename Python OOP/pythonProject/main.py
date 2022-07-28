def getTopUserAgent(browsers: list):
    browsers_dict = {}

    for browser in browsers:
        if browser in browsers_dict:
            browsers_dict[browser] += 1
        else:
            browsers_dict[browser] = 1

    sorted_browsers_dict = sorted(
        browsers_dict.items(),
        key=lambda x: (-x[1], x[0]),
    )

    return sorted_browsers_dict[0]


def getTopNUserAgents(browsers: list, number: int):
    browsers_dict = {}

    for browser in browsers:
        browser = browser.split("/")
        browser = browser[0]
        if browser in browsers_dict:
            browsers_dict[browser] += 1
        else:
            browsers_dict[browser] = 1

    sorted_browsers_dict = sorted(
        browsers_dict.items(),
        key=lambda x: -x[1],
    )

    result = []

    for idx in range(number):
        result.append(sorted_browsers_dict[idx][0])

    result.sort()

    return ", ".join(result)


print(getTopUserAgent(["Chrome", "Chrome", "Mozilla", "Safari", "Mozilla", "Chrome"]))
print(getTopUserAgent(["Safari", "Mozilla", "Mozilla", "Safari"]))
print(getTopNUserAgents(["Chrome", "Chrome", "Mozilla", "Safari", "Mozilla", "Chrome"], 2))
print(getTopNUserAgents(["Edge", "Safari", "Internet Explorer"], 3))
print(getTopNUserAgents(["Mozilla/5.15.0", "Chrome/60.0.3112.3", "Mozilla/5.0", "Safari/537.36", "Mozilla/4.59", "Chrome/60.0.3112.3"], 2))
print(getTopNUserAgents(["Mozilla", "Chrome/60.0.3112.3", "Mozilla/5.0"], 1))
