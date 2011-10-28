from pyrobot.brain import Brain

class WB(Brain):
    def setup(self):
        self.counter = 0
        self.inverse = {}
        self.inverse['right'] = 'left'
        self.inverse['down'] = 'up'
        self.inverse['left'] = 'right'
        self.inverse['up'] = 'down'
        d = 'down'
        r = 'right'
        u = 'up'
        l = 'left'
        self.actions = ['right','right','up','up','left','left','up','up','left','up','up','right','up','up','up','right','right',d,d,r,r,r,r,u,u,l,l]

    def step(self):
        if not (self.robot.getItem('win')):
            if self.robot.getItem('golds')>0:
                pos = self.robot.move(self.actions[self.counter])
                self.counter += 1
                if pos == 'gold':
                    self.robot.move('grab')
            else:
                if self.counter > 0:
                    self.counter -= 1
                pos = self.robot.move(self.inverse[self.actions[self.counter]])

def INIT(engine):
    return WB('WB', engine)
