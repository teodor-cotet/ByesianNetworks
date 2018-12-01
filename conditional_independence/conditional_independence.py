
# coditional ind implemented through d-separation

# X CI Y | Z if there is no active path between them given Z
# Xi+1 -> Xi -> Xi-1  

g = {}
g['A'] = [('C', 1)]
g['B'] = [('C', 1), ('D', 1)]
g['C'] = [('E', 1), ('D', 1)]
g['E'] = []
g['D'] = []

viz = set()
current = []
all_paths = []

def make_unorinted(g):
    gt = {}

    for x in g:
        for son in g[x[0]]:
            if son[0]  not in gt:
                gt[son[0]] = []
            gt[son[0]].append((x[0], 2))
    for x in g:
        for son in g[x[0]]:
            if x[0]  not in gt:
                gt[x[0]] = []
            gt[x[0]].append((son[0], 1))
    return gt

def get_all_desc(g, x):

    viz.add(x)
    res = [x]

    for son in g[x]:
        if son[0] not in viz:
            res += get_all_desc(g, son[0])
    return res

def get_all_paths(gc, x, y, dr):

    if x == y:
        all_paths.append(current + [(x, dr)])

    current.append((x, dr))
    viz.add(x)
    
    for son in gc[x]:
        sonn = son[0]
        if sonn not in viz:
            get_all_paths(gc, sonn, y, son[1])
    current.pop()
    viz.remove(x)
    
def is_path(x1, x2, x3, Z, g):
    if (x2[1] == 1 and x3[1] == 1):
        if x2[0] not in Z:
            return True
    elif (x2[1] == 2 and x3[1] == 2):
        if x2[0] not in Z:
            return True
    elif (x2[1] == 2 and x3[1] == 1):
        if x2[0] not in Z:
            return True
    elif (x2[1] == 1 and x3[1] == 2):
        viz = set()
        desc = get_all_desc(g, x2[0])
        for d in desc:
            if d in Z:
                return True
    return False


if __name__ == "__main__":
    gc = make_unorinted(g)
    # x CI y given Z
    x = 'A'
    y = 'B'
    Z = set('D')
    # all paths x -> y

    get_all_paths(gc, x, y, -1)
    dep = False

    # search for an active path
    for path in all_paths:
        ln = len(path)
        is_p = True
        # check each tuple(Xi-1, Xi, Xi+1) if is inactive
        for i in range(ln - 2):
            x1 = path[i]
            x2 = path[i + 1]
            x3 = path[i + 2]
            if is_path(x1, x2, x3, Z, g) == False:
                is_p = False
        if is_p == True:
            dep = True
        
    if dep == False:
        print("{} is conditionally independent wrt {}, given {}".format(x, y, Z))
    else:
        print("{} is NOT conditionally independent wrt {}, given {}".format(x, y, Z))


