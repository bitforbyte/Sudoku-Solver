#!/usr/bin/env python3
import json
from SudoSolver import SudoSolver
from pprint import pprint

def main():
    with open('Example.json') as f:
        data = json.load(f)
    
    sSolve = SudoSolver(data["Problem"])
    sSolve.solve()

    pprint(sSolve.solution)
    print(data["Solution"] == sSolve.solution)

if __name__ == "__main__":
    main()