

'''Shamelessly copied from https://gist.github.com/jamiees2/5531924'''
def aStar(start, goal):
    def manhattan(src, dest):
        return src.id != dest.id

    #The open and closed sets
    openset = set()
    closedset = set()

    #Current point is the starting point
    current = start

    #Add the starting point to the open set
    openset.add(current)

    #While the open set is not empty
    while in openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o: o.G + o.H)

        #If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        #Remove the item from the open set
        openset.remove(current)

        #Add it to the closed set
        closedset.add(current)

        #Loop through the node's children/siblings
        for node in get_relatives(current.id):
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)

                #Set the parent to our current item
                node.parent = current

                #Add it to the set
                openset.add(node)

    #Throw an exception if there is no path
    raise ValueError('No Path Found')
