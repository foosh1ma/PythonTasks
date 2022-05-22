class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(arr):
    chars = ['R', 'P', 'S']
    p1_wins = [['R', 'S'], ['P', 'R'], ['S', 'P']]
    p1, p2, pc1, pc2 = arr[0][0], arr[1][0], arr[0][1], arr[1][1]
    if len(arr) != 2:
        raise WrongNumberOfPlayersError
    if pc1 not in chars or pc2 not in chars:
        raise NoSuchStrategyError
    if pc1 == pc2 or [pc1, pc2] in p1_wins:
        return f"{p1} {pc1}"
    else:
        return f"{p2} {pc2}"


# print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))    # => WrongNumberOfPlayersError
# print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))                      # => NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))                        # => 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))                        # => 'player1 P'
