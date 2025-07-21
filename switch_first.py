rooms = {
    'room1' : {
        'first_entry' : True,
        'desc_first' : 'this is the first time you\'ve entered this room',
        'desc' : 'this is every other time you enter this room'
    }
}

def get_desc(room):
    global rooms
    if rooms.get(room).get('first_entry'):
        print('True')
        rooms.get(room).update({'first_entry' : False})
    elif not rooms.get(room).get('first_entry'):
        print('False')
    else:
        print('Error somewhere')

get_desc('room1')
get_desc('room1')
