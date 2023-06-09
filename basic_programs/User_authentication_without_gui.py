user = {
    'name': 'maverick',
    'valid': 'True'}


def auth(func):
    def wrapfunc(*args, **kwargs):
        if user['valid'] == 'True':
            func(*args, **kwargs)
        else:
            print('message not sent ')
    return wrapfunc


@auth
def validtrue():
    print('message sent')


validtrue()
