import asyncio
import pygame
import pyxel as p
from player import Player
from road import Road
import os
import websockets

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

class Game:
    def __init__(self, websocket):
        self.websocket = websocket
        self.player = Player(self.websocket)
        self.players = []
        self.road = Road() 

    def update(self):

        self.player.update()

    def draw(self):
        p.cls(p.COLOR_LIME)
        self.road.draw_road()
        self.player.car.draw_car()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.start_pyxel)

    def start_pyxel(self):
        joystick_count = pygame.joystick.get_count()
        if joystick_count > 0:
            self.player.joystick = pygame.joystick.Joystick(0)
            self.player.joystick.init()
        p.init(288, 224, fps=60, title="Mario Kart 8.5")
        p.load("images.pyxres")
        p.mouse(True)
        p.run(self.update, self.draw)

    async def receive_message(self):
        try:
            async for message in self.websocket:
                print(f"Received from server: {message}")
                await self.player.handle_message(message)
                await self.handle_message(message)
        except websockets.ConnectionClosed:
            print("Disconnected from server.")


    async def handle_message(self, message):
        if message.startswith("create_player"):
            self.create_player(message)
        elif message == "run":
            self.run()
        elif message == "this room is full error":
            print("This room is full.")
            await self.websocket.close()


    def create_player(self, message):
        player_id = message.split("-")[0].split("/")[1]
        if not any(player["id"] == player_id for player in self.players):
            self.players.append({
                "id": player_id,
                "color": message.split("-")[1].split("/")[1]
            })
        print(self.players)
    
    async def send_id_request(self):
        await self.websocket.send("load")
    
