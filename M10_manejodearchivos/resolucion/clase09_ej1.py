import sys
if len(sys.argv) == 3:
    print(f"primer parametro{sys.argv[1]}")
    print(f"segundo parametro{sys.argv[2]}")
    print(f"tercer parametro{sys.argv[3]}")
else:
    print("ERROR debes dar un parametro")