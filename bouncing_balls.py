def bouncing_ball(h, bounce, window):
    if h <= 0 or not 0 < bounce < 1 or window > h:
        return -1
    count = -1
    while h > window:
        count += 2
        h *= bounce

    return count
