def find_longest(string):
    dirs = []
    longest_length = 0
    for l in string.split("\n"):
        d = find_depth(l)
        name = l.strip()
        if len(dirs) <= d:
            dirs.append([name])
        else:
            dirs[d].append(name)
        if is_file(name):
            path = "/".join([ls[-1] for i, ls in enumerate(dirs) if i <= d])
            print path
            if len(path) > longest_length:
                longest_length = len(path)
    print dirs
    return longest_length

def is_file(name):
    return not name.find(".", 0) == -1

def find_depth(string):
    offset = 0
    cnt = 0
    while True:
        idx = string.find("\t", offset)
        if idx == -1:
            break
        else:
            cnt += 1
            offset = (idx + 1)
    return cnt

#string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\t\tthisisfile3.ext" 

print string
print find_longest(string)
