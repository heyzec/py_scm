import asyncio
import pygame

from py_scm.scene import Scene

class Director:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.scene:Scene = None
        self.quit_flag = False
        self.custom_events = []
    
    async def loop(self):
        self.scene.on_setup()
        context = {}
        while not self.quit_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                self.scene.on_event(event, context)

            for event in self.custom_events:
                self.scene.on_event(event, context)
            self.custom_events.clear()
                
            if self.scene is not None:
                self.scene.on_draw(self.screen)
            pygame.display.update()

            await asyncio.sleep(0.1)

    def event_from_outside(self, event):
        # assert isinstance(event, type(pygame.event.Event))
        self.custom_events.append(event)
        
    def set_scene(self, scene):
        self.scene = scene
    
    def quit(self):
        self.quit_flag = True
