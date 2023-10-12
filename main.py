from forestSample import ForestSample

f = ForestSample(size=30)


while f.isMonkeyAlive():
    step = f.bfs()
    f.renderFrame(step)
    input("Press Enter to continue...")
    print("\033[H\033[J")
    