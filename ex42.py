#Gothons From Planet Percal#25

class Scene(object):

    def enter(self):
        print ("You have been entered into %s" %self.name)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        print ("The room is full of %s" %self.scene_map)
        Map()
    
class Death(Scene):

    def enter(self):
        print ("You died. Game over!")

class CentralCorridor(Scene):

    def enter(self):
        print ("There is a Gothon already standing here that you have to default.")

class LaserWeaponArmory(Scene):
    
    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass
    
class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play