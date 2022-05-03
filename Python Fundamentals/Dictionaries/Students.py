studentsInfo = {}
courses = []
infoCheck = ''
newStudentsInfo = {}

while True:
    info = input()
    if ':' in info:
        info = info.split(':')
    elif '_' in info:
        info = info.split('_')
        infoCheck = info[0] + ' ' + info[1]
    elif '_' not in info:
        infoCheck = info

    if info in courses or infoCheck in courses:
        break

    ID = info[1]
    name = info[0]
    course = info[2]
    studentsInfo[ID] = {}
    studentsInfo[ID]['name'] = name
    studentsInfo[ID]['course'] = course
    courses.append(info[2])

for check in studentsInfo.keys():
    if infoCheck == studentsInfo[check]['course']:
        newStudentsInfo[check] = studentsInfo[check]['name']

for key in newStudentsInfo.keys():
    print(f"{newStudentsInfo[key]} - {key}")
