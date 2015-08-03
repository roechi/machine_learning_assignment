def print_scores(text, scores):
    return (str(text) + ' {0:.8f} (+/-{1:.5f})').format(scores.mean(), scores.std())
    