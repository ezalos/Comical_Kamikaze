
class Solver():
	def __init__(self, DATA, puzzle=None):
		if puzzle:
			self.puzzle = puzzle
		else:
			self.puzzle = generate()
		self.original_puzzle = copy.deepcopy(self.puzzle)
		DATA.solution = generate_solution()
		DATA.index_map = get_index_map(DATA.solution)
		self.statistics = []
		# print(DATA.index_map)
		self.big_queue = []
		self.launch_Astar()

	@benchmark
	def launch_Astar(self):
		def tt_cost(x): return x.total_cost
		self.big_queue = []
		self.big_queue.append(NPuzzle(self.puzzle))

		state_studied = 0
		loop_nb = 0
		end = False
		while len(self.big_queue) and end == False:
			# for i in range(3):
			loop_nb += 1
			if True:
				print("\033[0;0H")
				print(self.big_queue[0])
			for dir in range(4):
				child = self.big_queue[0].do_move(dir)
				if child != None:
					state_studied += 1
					self.big_queue.append(child)
					if child.is_game_over():
						# print("GGGGGGGG")
						# print("Total states studied: ", state_studied)
						# print("Was originally: ", self.original_puzzle)
						# print(child)
						end = True
						break
			del self.big_queue[0]

			self.big_queue.sort(key=tt_cost)
		print("Queue of states:            {}".format(len(self.big_queue)))
		print("Total nb states generated:  {}".format(state_studied))
		print("A* cycle number:            {}".format(loop_nb))

	def __str__(self):
		m = (DATA.n ** 2) - 1
		m = len(str(m))
		if len(str(-1)):
			m = len(str(-1))
		board = ""
		for idx, val in enumerate(self.puzzle):
			i = self.puzzle[idx]
			if i == None:
				i = -1
				board += YELLOW
			elif i == 0:
				board += BLUE
			elif self.puzzle[idx] == DATA.solution[idx]:
				board += GREEN
			else:
				board += RED
			board += "{1:{0}d} ".format(m, i)
			if (idx % DATA.n) == DATA.n - 1:
				board += "\n"
		board += RESET
		return board
