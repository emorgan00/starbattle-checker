def check(grid):
	global row, count

	size = len(grid)

	if size == 0 or size != len(grid[0]):
		print("Error: grid is not square.")
		return

	region = {}
	for r in grid:
		for x in r:
			region[x] = 0

	row = -1
	count = 0
	stars = [[0 for _ in range(size)] for _ in range(size)]
	cols = [0 for _ in range(size)]

	def valid(i):
		return (row == 0 \
			or not (i > 0 and stars[row-1][i-1] or stars[row-1][i] or i < size-1 and stars[row-1][i+1])) \
			and region[grid[row][i]] < 2 \
			and cols[i] < 2

	def step():
		global row, count

		row += 1

		if row == size:
			for r in stars:
				print('\t'.join('O' if x else ' ' for x in r))
			print("\n" + "-\t"*size + "\n")
			row -= 1
			count += 1
			if count > 10:
				print("many solutions were found. exiting early...")
			return

		for i in range(size):
			if valid(i):
				region[grid[row][i]] += 1

				for j in range(i-1):
					if valid(j):
						stars[row][i] = 1
						stars[row][j] = 1
						cols[i] += 1
						cols[j] += 1
						region[grid[row][j]] += 1

						step()
						if count > 10:
							return

						stars[row][i] = 0
						stars[row][j] = 0
						cols[i] -= 1
						cols[j] -= 1
						region[grid[row][j]] -= 1

				region[grid[row][i]] -= 1
		row -= 1

	step()
	if count == 1:
		print("Success. The puzzle had only one solution.")