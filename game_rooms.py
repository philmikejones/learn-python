all_rooms = {
    "outside" : {
      "label"  : "Outside",
      "locked" : None,
      "access" : ["mainhall",],  # need to force a list or python will iterate over the invididual letters
      "items"  : None,
      "desc"   : "It's too dangerous to go outside",
      "desc_special" : "You open the mansion door to see if you can make it to safety. One of the dogs that chased you leaps at you and you only just manage to slam the door shut in time. Going back outside is not an option.",
      "trigger_special" : True,
    },
    "mainhall" : {
      "label"  : "Main hall",
      "locked" : None,
      "access" : ["diningroom", "artroom", "outside"],
      "items"  : None,
      "desc"   : "The Main hall of this mysterious mansion. A grand staircase sweeps up to the first floor. It is too dangerous to go back outside."
    },
    "diningroom" : {
      "label"  : "Dining room",
      "locked" : None,
      "access" : ("mainhall", "westgroundcorridor"),
      "items"  : ["emblem", ],
      "desc"   : "An elaborate dining room with a ticking clock and a fireplace at the far end of the room. There is blood in front of the fireplace.",
      "trigger_special" : False,
    },
    "westgroundcorridor" : {
      "label"  : "West Ground Corridor",
      "locked" : None,
      "access" : ("diningroom", "musicroom"),
      "items"  : ["clip",],
      "desc"   : "A long corridor connecting the rooms of the west side of the house. The corpse of Kenneth from Bravo team is at the end of the hallway."
    },
    "musicroom" : {
      "label"  : "Music room",
      "locked" : "lockpick",
      "access" : ("westgroundcorridor",),
      "items"  : ["goldemblem", "musicsheet"],
      "desc  " : "A music room with grand piano, a drinks bar, a bookcase, and what looks like a gap in the wall..."
    },
    "artroom" : {
      "label"  : "Art room",
      "locked" : "Armour",
      "access" : ("mainhall", "eastgroundcorridor"),
      "items"  : None,
      "desc  " : "A room with a marble statue, various paintings, and art supplies tucked around the corner on shelves."
    },
    "eastgroundcorridor" : {
      "label"  : "East Ground Corridor",
      "locked" : None,
      "access" : ("artroom", "eastgroundrearcorridor"),
      "items"  : ["clip", ],
      "desc  " : "A long corridor with ornate silverware and crockery stored in sideboards. The corridor takes you to the back of the mansion."
    },
    "eastgroundrearcorridor" : {
      "label"  : "East Ground Rear Corridor",
      "locked" : None,
      "access" : ("eastgroundcorridor",),
      "items"  : None,
      "desc  " : "A winding corridor that takes you to the rear of the mansion. There is a bathroom, a study, and an outside store accessed from this corridor. Otherwise there is nothing of note."
    }
}
