def player(prev_play, opponent_history=[], play_order={}):
    """
    Rock-Paper-Scissors player that predicts the opponent's next move
    from previously observed sequences and chooses the winning response.

    Args:
        prev_play (str): The opponent's previous move: "R", "P", "S",
                         or an empty string at the start of a match.

    Returns:
        str: Our move: "R", "P", or "S".
    """

    # Reset stored data at the beginning of a new match.
    if not prev_play:
        prev_play = "R"
        opponent_history.clear()
        play_order.clear()

    # Store the opponent's latest move.
    opponent_history.append(prev_play)

    # Default prediction until enough history is available.
    prediction = "P"

    # Count every observed sequence of five opponent moves.
    sequence_length = 5

    if len(opponent_history) > sequence_length:
        pattern = "".join(opponent_history[-sequence_length:])
        play_order[pattern] = play_order.get(pattern, 0) + 1

        # Use the latest four moves as the context for predicting
        # the opponent's next move.
        last_four = "".join(opponent_history[-(sequence_length - 1):])

        possible_sequences = [
            last_four + move for move in ("R", "P", "S")
        ]

        # Find the move that most often followed this four-move context.
        matching_sequences = {
            sequence: play_order[sequence]
            for sequence in possible_sequences
            if sequence in play_order
        }

        if matching_sequences:
            most_common_sequence = max(
                matching_sequences,
                key=matching_sequences.get
            )
            prediction = most_common_sequence[-1]

    # Choose the move that beats the predicted opponent move.
    winning_response = {
        "P": "S",
        "R": "P",
        "S": "R"
    }

    return winning_response[prediction]
