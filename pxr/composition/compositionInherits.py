import os
from pxr import Sdf, Usd


def main():
    stage = Usd.Stage.CreateInMemory()
    bikePrimPath = Sdf.Path("/bike")
    bikePrim = stage.DefinePrim(bikePrimPath)
    carPrimPath = Sdf.Path("/car")
    carPrim = stage.DefinePrim(carPrimPath)
    inheritAPI = bikePrim.GetInherits()
    inheritAPI.AddInherit(
        carPrimPath, position=Usd.ListPositionFrontOfAppendList)
    print(stage.GetRootLayer().ExportToString())


if __name__ == "__main__":
    main()
