workingDir = ["/"]
def path_sorter(path):
    #Helper function for most of the other functions.
    #Converts string path to list path.
    newPath = path.split("/")
    while newPath.count(""):
        newPath.remove("")
    if path[0] == "/":
        newPath = ["/"] + newPath
    return newPath

def usuablePath(FS, path):
    #Used on list paths.
    #Helper function for most of the other functions.
    #Checks if the path is valid.
    Path = []
    for i, x in enumerate(path):
        if x == ".":
            continue
        if x == "..":
            Path.pop()
            if not Path:
                return False
            continue
        Path.append(x)
        if not is_valid_exec(FS, Path) and i != len(path)-1 :
            return False
    return Path
        
def is_valid_mkdir(FS, path):
    #Checks if the path is valid.(mkdir function needed a specified is_valid function)
    if len(path) == 0:
        return False
    if len(path) == 1:
        return datum(FS)[0] == path[0]
    if is_leaf(FS):
        return False
    if datum(FS)[0] == path[0]:
        exists = False
        for child in children(FS):
            if datum(child)[1] in ["D", "d"]:
                exists = exists or is_valid_mkdir(child, path[1:])
            if exists:
                return True
    return False

def is_valid_mkdir2(FS, path, target):
    #An extre path checker for mkdir.
    folder = accsess(FS, path)
    for child in children(folder):
        if datum(child)[0] == target:
            return False 
    return True

def is_valid_copy(FS, path):
    #Path checker for the function copy. (Source)
    if len(path) == 0:
        return False
    if len(path) == 1:
        return datum(FS)[0] == path[0]
    if is_leaf(FS):
        return False
    if datum(FS)[0] == path[0]:
        exists = False
        for child in children(FS):
            exists = exists or is_valid_copy(child, path[1:])
            if exists:
                return True
    return False

def is_valid_copy2(FS, path):
    #Path checker for the function copy. (Target)
    if len(path) == 0:
        return False
    if len(path) == 1:
        return datum(FS)[0] == path[0]
    if is_leaf(FS):
        return False
    if datum(FS)[0] == path[0]:
        exists = False
        for child in children(FS):
            if datum(child)[1] in ["D", "d"]:
                exists = exists or is_valid_copy2(child, path[1:])
            if exists:
                return True
    return False

def is_valid_cd(FS, path):
    #Path checker for the function cd.
    if len(path) == 0:
        return False
    if len(path) == 1:
        return datum(FS)[0] == path[0]
    if is_leaf(FS):
        return False
    if datum(FS)[0] == path[0]:
        exists = False
        for child in children(FS):
            if datum(child)[1] in ["D", "d"]:
                exists = exists or is_valid_cd(child, path[1:])
            if exists:
                return True
    return False

def is_valid_rm(FS, path):
    #Path checker for the function rm.
    if len(path) == 0:
        return False
    if len(path) == 1:
        return datum(FS)[0] == path[0] and datum(FS)[1] in ["F", "f"]
    if is_leaf(FS):
        return False
    if datum(FS)[0] == path[0]:
        exists = False
        for child in children(FS):
            exists = exists or is_valid_rm(child, path[1:])
            if exists:
                return True
    return False

def is_valid_rmdir(FS, path):
    #Path checker for the function rmdir.
    if len(path) == 0:
        return False
    if len(path) == 1:
        return (datum(FS)[0] == path[0]) and is_leaf(FS)
    if is_leaf(FS):
        return False
    if datum(FS)[0] == path[0]:
        exists = False
        for child in children(FS):
            if datum(child)[1] in ["D", "d"]:
                exists = exists or is_valid_rmdir(child, path[1:])
            if exists:
                return True
    return False

def is_valid_rmdir2(path, workingDir):
    #An extra path checker for the function rmdir.
    if not workingDir:
        return len(path) > 0
    if not path:
        return False
    if workingDir[0] == path[0]:
        return is_valid_rmdir2(path[1:], workingDir[1:])
    else:
        return True

def is_valid_exec(FS, path):
    #Path checker for the function exec.
    if len(path) == 0:
        return False
    if len(path) == 1:
        return datum(FS)[0] == path[0]
    if is_leaf(FS):
        return False
    if datum(FS)[0] == path[0]:
        exists = False
        for child in children(FS):
            exists = exists or is_valid_exec(child, path[1:])
            if exists:
                return True
    return False

def datum(tree):
    #Returns the datum of the given tree.
    return tree[0: 2]
def children(tree):
    #Return the children of the given tree.
    return tree[2:]
def is_leaf(tree):
    #Checks if the given tree is a leaf.
    return tree[2:] == []

def accsess(FS, path):
    #Return the file of the given path.
    if len(path) == 1:
        return FS
    for child in children(FS):
        if datum(child)[0] == path[1]:
            return accsess(child, path[1:])

def rmdir(FS, RM):
    #Remove the directory of the given path.
    #Return True if path is valid and the directoru has been removed succesfully. Return False otherwise.
    path = RM.split(" ")
    while path.count(""):
        path.remove("")
    if len(path) != 2:
        return False
    path = path[1]
    path = path_sorter(path)
    if path[0] != "/":
        path = workingDir + path
    path = usuablePath(FS, path)
    if path == False:
        return False
    if not is_valid_rmdir(FS, path):
        return False
    if not is_valid_rmdir2(path, workingDir):
        return False
    parent = accsess(FS, path[:-1])
    for child in children(parent):
        if datum(child)[0] == path[-1]:
            parent.remove(child) 
    return True

def rm(FS, RM):
    #Remove the file of the given path.
    path = RM.split(" ")
    while path.count(""):
        path.remove("")
    if len(path) != 2:
        return False
    path = path[1]
    path = path_sorter(path)
    if path[0] != "/":
        path = workingDir + path
    path = usuablePath(FS, path)
    if path == False:
        return False
    if not is_valid_rm(FS, path):
        return False
    parent = accsess(FS, path[:-1])
    for child in children(parent):
        if datum(child)[0] == path[-1]:
            parent.remove(child)
    return True

def mkdir(FS, MD):
    #Create a directory with the given path.
    #Return True if the path is valid and directory has been created succesfully. Return False otherwise.
    path = MD.split(" ")
    while path.count(""):
        path.remove("")
    if len(path) != 2:
        return False
    path = path[1]
    path = path_sorter(path)
    if path[0] != "/":
        path = workingDir + path
    path = usuablePath(FS, path)
    if path == False:
        return False
    target = path[-1]
    path = path[:-1]
    if not is_valid_mkdir(FS, path):
        return False
    if not is_valid_mkdir2(FS, path, target):
        return False
    parent = accsess(FS, path)
    parent.append([target, "D"])
    return True

def execute(FS, EX):
    #Execute the file of the given path.
    #Return True if the path is valid and the file has been executed succesfully. Return False otherwise.
    path = EX.split(" ")
    while path.count(""):
        path.remove("")
    if len(path) != 2:
        return False
    path = path[1]
    path = path_sorter(path)
    if path[0] != "/":
        path = workingDir + path
    path = usuablePath(FS, path)
    if path == False:
        return False
    if not is_valid_exec(FS, path):
        return False
    target = accsess(FS, path)
    if datum(target)[1] not in ["F", "f"]:
        return False
    return True

def copy(FS, CP):
    #Copies the file of the given path to required position.
    #Returns True if the paths are valid and the file has been copeid succesfully. Returns False otherwise.
    path = CP.split(" ")
    while path.count(""):
        path.remove("")
    print path
    if len(path) != 3:
        return False
    path1 = path[1]
    path2 = path[2]
    print path1
    print path2
    def get_path(workingDir, path):
        path = path_sorter(path)
        if path[0] != "/":
            path = workingDir + path
        path = usuablePath(FS, path)
        return path
    path1 = get_path(workingDir, path1)
    path2 = get_path(workingDir, path2)
    if path1 == False or path2 == False:
        return False
    if not is_valid_copy(FS, path1):
        return False
    source = accsess(FS, path1)
    if source[1] in ["F", "f"]:
        if not is_valid_copy(FS ,path2) and is_valid_copy2(FS, path2[:-1]):
            parent = accsess(FS, path2[:-1])
            parent.append([path2[-1]]+[source[1]])
            return True
        if is_valid_copy(FS, path2):
            target = accsess(FS, path2)
            if target[1] in ["F", "f"]:
                return False
            if target[1] in ["D", "d"]:
                if not can_copy(target, source):
                    return False
                target.append(source)
                return True
        return False
    if source[1] in ["D", "d"]:
        if not is_valid_copy(FS, path2) and is_valid_copy2(FS,path2[:-1]):
            parent = accsess(FS, path2[:-1])
            parent.append([path2[-1]]+deepcopy(source[1:]))
            return True
        if is_valid_copy(FS, path2):
            target = accsess(FS, path2)
            if target[1] in ["F", "f"]:
                return False
            if target[1] in ["D", "d"]:
                if not can_copy(target, source):
                    return False
                target.append(deepcopy(source[:]))
                return True
        else:
            return False
    return True

def can_copy(parent, target):
    #A helper function for copy.
    for child in children(parent):
        if datum(child)[0] == target[0]:
            return False
    return True
    
def cd(FS, CD):
    #Does the same operation as the "cd" command in Linux. (Updates the working directory)
    #Returns true if the operation is succesfull. Return false otherwise.
    global workingDir
    path = CD.split(" ")
    while path.count(""):
        path.remove("")
    if len(path) > 2:
        return False
    if len(path) == 1:
        workingDir = ["/"]
        return True
    path = path[1]
    path = path_sorter(path)
    if path[0] != "/": #If it is not an absolute path
        path = workingDir + path
    path = usuablePath(FS, path)
    if path == False:
        return False
    if is_valid_cd(FS, path):
        workingDir = path
        return True
    else:
        return False

#FS = ["/", "d", ["home", "D", ["the4", "D", ["the4", "D"], ["the.py", "F"]]], ["etc", "d"], ["tmp", "D", ["tmp.sh", "F"], ["del.txt", "F"]]]
def check_commands(FS, C):
    #Think this as the main function. 
    #The parameter C should be in list tpye, such as; ["cd home", "cd .."]
    global workingDir
    workingDir = ["/"]
    commands = []
    while len(C) > 0:
        commands.append(C.pop(0))
    for x in commands:
        lst = x.split(" ")
        while lst.count(""):
            lst.remove("")
        if lst[0] not in ["cd", "cp", "mkdir", "rmdir", "rm", "exec"]:
            return "ERROR", x, get_dir(workingDir)
        elif lst[0] == "cd":
             if not cd(FS, x):
                 return "ERROR", x, get_dir(workingDir)
        elif lst[0] == "cp":
            if not copy(FS, x):
                return "ERROR", x, get_dir(workingDir)
        elif lst[0] == "mkdir":
            if not mkdir(FS, x):
                return "ERROR", x, get_dir(workingDir)
        elif lst[0] == "rmdir":
            if not rmdir(FS, x):
                return "ERROR", x, get_dir(workingDir)
        elif lst[0] == "rm":
            if not rm(FS, x):
                return "ERROR", x, get_dir(workingDir)
        elif lst[0] == "exec":
            if not execute(FS, x):
                return "ERROR", x, get_dir(workingDir)
    return "SUCCESS", FS, get_dir(workingDir)

def get_dir(workingDir = workingDir):
    #Returns the working directory. (the global variable workingDir should be given as an input)
    workingDir = "/".join(workingDir)
    if len(workingDir) > 1 and (workingDir[0] == "/") and (workingDir[1] == "/"):
        workingDir = workingDir[1:]
    return workingDir

def deepcopy(lst):
    #Deepcopy function for lists. 
    #Used as a helper function of the function copy.
    ret = []
    if type(lst) != list:
        ret = lst
    if type(lst) == list:
        for x in lst:
            ret.append(deepcopy(x))
    return ret
