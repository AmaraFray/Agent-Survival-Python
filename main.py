from forestSample import ForestSample

f = ForestSample(size=25, initial_fire_pos={(0,0), (24,0)}, initial_monkey_pos=(24,24))


while f.isMonkeyAlive():
    step = f.bfs()
    f.renderFrame(step)
    input("Press Enter to continue...")
    print("\033[H\033[J")
    