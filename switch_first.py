rooms = {
    'room1_first_entry' : True,
    'room1_desc_first' : 'this is the first time you\'ve entered this room',
	'room1_desc' : 'this is every other time you enter this room'
}

def get_desc(room):
    global rooms
    room_first_entry = room + "_first_entry"
    if rooms[room_first_entry]:
        desc = room + "_desc_first"
        rooms.update({room_first_entry : False})
    else:
        desc = room + "_desc"
    
    desc = rooms[desc]
    return desc

desc = get_desc(room = 'room1')
print(desc)

desc = get_desc(room = 'room1')
print(desc)
