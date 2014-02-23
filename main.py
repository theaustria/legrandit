import engine

def main():
    eng = engine.Engine()
    eng.loop()
    del eng

if __name__ == '__main__':
    main()