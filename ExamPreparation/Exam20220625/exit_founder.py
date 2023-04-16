def take_matrix():
    matrix = []
    for _ in range(6):
        matrix.append(input().split())

    return matrix


def unpack_coordinates():
    z = input().split(', ')
    x = int(z[0][1])
    y = int(z[1][0])
    return x, y


def main(player_one, player_two, matrix):
    player_one_hit_wall = False
    player_two_hit_wall = False
    while True:
        if not player_one_hit_wall:
            i, j = unpack_coordinates()
            position = matrix[i][j]

            # Check win
            if position == 'E':
                print(f"{player_one} found the Exit and wins the game!")
                break

            # Check trap
            if position == 'T':
                print(f"{player_one} is out of the game! The winner is {player_two}.")
                break

            # Check wall
            if position == 'W':
                print(f"{player_one} hits a wall and needs to rest.")
                player_one_hit_wall = True
        else:
            player_one_hit_wall = False

        if not player_two_hit_wall:
            i, j = unpack_coordinates()
            position = matrix[i][j]

            # Check win
            if position == 'E':
                print(f"{player_two} found the Exit and wins the game!")
                break

            # Check trap
            if position == 'T':
                print(f"{player_two} is out of the game! The winner is {player_one}.")
                break

            # Check wall
            if position == 'W':
                print(f"{player_two} hits a wall and needs to rest.")
                player_two_hit_wall = True
        else:
            player_two_hit_wall = False


if __name__ == '__main__':
    player_one, player_two = input().split(', ')
    maze_board = take_matrix()
    main(player_one, player_two, maze_board)
