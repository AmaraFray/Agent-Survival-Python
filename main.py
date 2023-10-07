from forestSample import ForestSample

f = ForestSample(size=10)


while f.isMonkeyAlive():
    step = f.bfs()
    f.renderFrame(step)