def player_status(health):
    if health == 0:
        print ("dead")
    elif health < 5:
        print ("critical")
    else:
        print ("healthy")