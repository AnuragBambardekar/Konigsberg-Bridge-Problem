BRIDGES = [
    "AaB",
    "AbB",
    "AcC",
    "AdC",
    "AeD",
    "BfD",
    "CgD",
]

def get_walks_starting_from(area, bridges=BRIDGES):
    walks = []
    # print(area)

    def make_walks(area, walked=None, bridges_crossed=None):
        print("area: ", area)
        walked = walked or area
        bridges_crossed = bridges_crossed or ()

        print("walked: ", walked)
        print("bridges crossed: ", bridges_crossed)

        available_bridges = [
            bridge
            for bridge in bridges
            if area in bridge and bridge not in bridges_crossed
        ]

        print("available bridges: ",available_bridges)

        # determine if walk has ended
        if not available_bridges:
            walks.append(walked)

        # walk the bridge to the adjacent area and recurse
        for bridge in available_bridges:
            print("bridge: ",bridge[0])
            crossing = bridge[1:] if bridge[0] == area else bridge[1::-1] # AaB or BaA
            print("crossing: ", crossing)
            make_walks(
                area=crossing[-1],
                walked=walked + crossing,
                bridges_crossed=(bridge, *bridges_crossed), # creates a new tuple that starts with the current bridge and is followed by all the elements from the original bridges_crossed tuple
            )
            break
    make_walks(area)
    return walks

walks_starting_from = {area: get_walks_starting_from(area) for area in "A"}