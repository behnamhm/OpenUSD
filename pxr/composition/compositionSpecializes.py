import os
from pxr import Sdf, Usd


def main():
    stage = Usd.Stage.CreateInMemory()
    bikePrimPath = Sdf.Path("/bike")
    bikePrim = stage.DefinePrim(bikePrimPath)
    cubePrimPath = Sdf.Path("/cube")
    cubePrim = stage.DefinePrim(cubePrimPath, "Cube")
    specializes_api = bikePrim.GetSpecializes()
    specializes_api.AddSpecialize(
        cubePrimPath, position=Usd.ListPositionFrontOfAppendList)
    print(stage.GetRootLayer().ExportToString())


if __name__ == "__main__":
    main()
