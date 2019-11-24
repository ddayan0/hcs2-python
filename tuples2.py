# Dennis Dayan, Watson 3A
# tuples2.py

dissapointingAlbumsTuple = ('Raditude', 'MBDTF', 'Stoney', 'SongsAboutJane', 'EveryModernPopAlbum')

def printObj(obj):
    for i in obj:
        print(i)
def line():
    print('\n--------')

printObj(dissapointingAlbumsTuple)
line()


def tupleRemove(tup, item):
    mlist = []
    for i in tup:
        mlist.append(i)
    mlist.remove(item)
    newTuple = tuple(mlist)
    return newTuple


printObj(tupleRemove(dissapointingAlbumsTuple, 'Raditude'))
line()

