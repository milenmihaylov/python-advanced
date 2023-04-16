def check_valid_hit(r, c):
    if r in range(7) and c in range(7):
        return True
    return False


def score_hit(r, c):
    sector_hit = dartboard[r][c]
    if isinstance(sector_hit, int):
        return dartboard[r][c]
    elif sector_hit == 'D':  # possible Ds at the edges of the board!!!
        total = (dartboard[0][c] + dartboard[r][0] + dartboard[r][6] + dartboard[6][c]) * 2
        return total
    elif sector_hit == 'T':  # possible Ds at the edges of the board!!!
        total = (dartboard[0][c] + dartboard[r][0] + dartboard[r][6] + dartboard[6][c]) * 3
        return total


def bulls_eye(r,c):
    if r == 3 and c == 3:  # possible B not at the center of the board!!!
        return True


def won_game(player_name, player_score, turns):
    if player_score <= 0:
        print(f"{player_name} won the game with {turns} throws!")
        return True
    return False


first_player_name, second_player_name = input().split(', ')
first_player_score = 501
second_player_score = 501
dartboard = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(7)]
throws = 0

current, other = [first_player_name, first_player_score], [second_player_name, second_player_score]
while True:
    if current[0] == first_player_name:
        throws += 1
    hit = input().split(', ')
    row = int(hit[0][1:])
    col = int(hit[-1][:-1])
    if check_valid_hit(row, col):
        if bulls_eye(row, col):
            print(f"{current[0]} won the game with {throws} throws!")
            break
        score = score_hit(row, col)
        current[1] -= score
        if won_game(current[0], current[1], throws):
            break

    current, other = other, current
