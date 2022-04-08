from typing import Dict

# (0, 0) is the bottom left, z increases upwards, x to the right
class PlayerState:
	'''
		Note the .enemy variable to identify the enemy
	'''
	def __init__(self, json_state : Dict, num = -1):
		self.player_num	= json_state["playerNumber"]
		self.moveSpeed 	= json_state["moveSpeed"]
		self.bombs 		= json_state["bombs"]
		self.bombRange 	= json_state["bombRange"]
		self.dead 		= json_state["dead"]
		self.x 			= json_state["position"]["x"]
		self.z 			= json_state["position"]["z"]
		self.enemy		= self.player_num != num


	def update_state(self, json_state : Dict):
		self.player_num	= json_state["playerNumber"]
		self.moveSpeed 	= json_state["moveSpeed"]
		self.bombs 		= json_state["bombs"]
		self.bombRange 	= json_state["bombRange"]
		self.dead 		= json_state["dead"]
		self.x 			= json_state["position"]["x"]
		self.z 			= json_state["position"]["z"]

	def __str__(self):
		indent = 5
		msg = ""
		msg += f"Player {self.player_num}, dead = {self.dead}\n"
		msg += f"{' ' * indent}[X, Z] = [{self.x}, {self.z}], speed {self.moveSpeed}\n"
		msg += f"{' ' * indent}bombs: {self.bombs}, range: {self.bombRange}\n"
		return msg
