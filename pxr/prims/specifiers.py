import os
from pxr import Sdf, Usd


def main():
    stage = Usd.Stage.CreateInMemory()

    stage.DefinePrim("/definedCube", "Cube").SetSpecifier(Sdf.SpecifierDef)
    stage.DefinePrim("/overCube", "Cube").SetSpecifier(Sdf.SpecifierOver)
    stage.DefinePrim("/classCube", "Cube").SetSpecifier(Sdf.SpecifierClass)

    for prim in stage.Traverse():
        print(prim)  # Usd.Prim(</definedCube>)

    for prim in stage.TraverseAll():
        print(prim)  # Usd.Prim(</definedCube>)
        # Usd.Prim(</overCube>)
        # Usd.Prim(</classCube>)

    for prim in stage.Traverse(Usd.PrimIsAbstract):
        print(prim)  # Usd.Prim(</classCube>)

    for prim in stage.Traverse(~Usd.PrimIsDefined):
        print(prim)  # Usd.Prim(</overCube>)


if __name__ == "__main__":
    main()
