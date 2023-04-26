import re

def solution(files):
    file = []
    for file_name in files:
        file.extend(re.findall(r'([a-zA-Z\-\n\s.]+)([0-9]{0,5})(.*)', file_name))
    file.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(i) for i in file]