def do_stuff(num=0):
    if num:
        try:
            return int(num) + 5
        except ValueError as err:
            return err
    else:
        return 'Please enter valid num'
