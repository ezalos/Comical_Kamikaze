from BaseAgent import BaseAgent
from random import Random
from Environment import Environnement
import defines


class FindAgent(BaseAgent):
	def __init__(self, player_num):
		super()
		self.player_num = player_num
		self.env		= Environnement(player_num)
		print("I Am a random agent, please help me get smarter than this !")


	def _direction_to_enemy(self, state):
		(s, pp, w) = state
		if pp[0].player_num == self.player_num:
			me, yu = pp[0], pp[1]
		else:
			me, yu = pp[1], pp[0]
		abs = lambda x: x if x >= 0 else -x
		diff_x = me.x - yu.x
		diff_z = me.z - yu.z
		if abs(diff_x) > abs(diff_z):
			if diff_x > 0:
				return defines.Down
			else:
				return defines.Up
		else:
			if diff_z > 0:
				return defines.Right
			else:
				return defines.Left


	def get_action(self, state):
		(s, pp, w) = state
		print(f"S is {s}")
		print(f"{pp[0]}")
		print(f"{pp[1]}")
		print(f"w is {w}")

		return (self._direction_to_enemy(state))


	
	


import sys
import time
if __name__ == "__main__":
	agent = FindAgent(int(sys.argv[1]))
	# agent.env.reset()
	state1 = agent.get_state()
	game_over = False


	while game_over == False:
		time.sleep(0.1)
		state = agent.do_action(agent.get_action(state1))
		_, _, w = state
		if (w is not None):
			game_over = True
