    from scorer import score

def radar(sessions):

    ranked = [score(s) for s in sessions]

    ranked.sort(
        key=lambda x: x.action_score,
        reverse=True
    )

    return ranked