'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph = {
    "@bongolpoc": {"first_name": "Joselito", "last_name": "Olpoc", "following": []},
    "@joaquin": {"first_name": "Joaquin", "last_name": "Gonzales", "following": ["@chums", "@jobenilagan"]},
    "@chums": {"first_name": "Matthew", "last_name": "Uy", "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]},
    "@jobenilagan": {"first_name": "Joben", "last_name": "Ilagan", "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]},
    "@joeilagan": {"first_name": "Joe", "last_name": "Ilagan", "following": ["@eeebeee", "@jobenilagan", "@chums"]},
    "@eeebeee": {"first_name": "Elizabeth", "last_name": "Ilagan", "following": ["@jobenilagan", "@joeilagan"]},
}):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
      
    from_following = social_graph.get(from_member, {}).get("following", [])
    to_following = social_graph.get(to_member, {}).get("following", [])

    if to_member in from_following and from_member in to_following:
        return "friends"
    elif to_member in from_following:
        return "follower"
    elif from_member in to_following:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board = [
        ['X', 'X', 'O'],
        ['O', 'X', 'O'],
        ['O', '', 'X']
    ]):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.    
    for row in board:
        if all(cell == row[0] and cell != '' for cell in row):
            return row[0]

    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(len(board))):
            return board[0][col]

    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(len(board))) or \
       all(board[i][len(board) - i - 1] == board[0][len(board) - 1] and board[i][len(board) - i - 1] != '' for i in range(len(board))):
        return board[0][0]

    return "NO WINNER"

#given the sample print(tic_tac_toe([['X', 'X', 'O'],['O', 'X', 'O'],['O', 'O', 'X']])) , the outcome should be X

def eta(first_stop="upd", second_stop="admu", route_map=None):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if route_map is None:
        route_map = {
            ("upd", "admu"): {"travel_time_mins": 10},
            ("admu", "dlsu"): {"travel_time_mins": 35},
            ("dlsu", "upd"): {"travel_time_mins": 55},
        }

    travel_time = 0
    current_stop = first_stop
    legs = list(route_map.keys())
    count = len(legs)

    if first_stop == second_stop:
        for leg in legs:
            travel_time += route_map[leg]["travel_time_mins"]
    else:
        while current_stop != second_stop:
            leg = [_ for _ in legs if _[0] == current_stop][0]
            travel_time += route_map[leg]["travel_time_mins"]
            current_stop = leg[1]

    print("ETA:", travel_time, "minutes")
    return travel_time

#you may use the following format to execute the code: result = eta(first_stop, second_stop)
#using the print function in this case will print the ETA twice