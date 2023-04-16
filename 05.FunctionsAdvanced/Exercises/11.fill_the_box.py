def fill_the_box(*args, **kwargs):
    global index
    if kwargs:
        for key in kwargs.keys():
            index = kwargs[key]
    else:
        index = 3
    height = args[0][0]
    length = args[1]
    width = args[2]
    box_volume = height * length * width - sum(args[3:index])

    if args[index] == "Finish":
        return f"There is free space in the box. You could put {box_volume} more cubes."
    box_volume -= args[index]
    if box_volume <= 0:
        return f"No more free space! You have {sum([x for x in args[index:] if type(x) == int]) - box_volume} " \
               f"more cubes."
    return fill_the_box(args, i=index+1)

    # cubes = deque(args)
    # current_cube = cubes.popleft()
    # while not current_cube == "Finish":
    #     box_volume -= current_cube
    #     if box_volume <= 0:
    #         return f"No more free space! You have {sum([x if type(x) == int else break for x in cubes]) -
    #         ox_volume} " \
    #                f"more cubes."
    #     current_cube = cubes.popleft()
    # return f"There is free space in the box. You could put {box_volume} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
