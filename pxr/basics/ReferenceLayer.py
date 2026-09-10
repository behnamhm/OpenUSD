import os
from pxr import Usd, UsdGeom, Gf


def main():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "HelloWorld.usda"
    )

    stage = Usd.Stage.Open(file_path)
    world = stage.GetPrimAtPath('/World')
    stage.SetDefaultPrim(world)
    UsdGeom.XformCommonAPI(world).SetTranslate((4, 5, 6))
    print(stage.GetRootLayer().ExportToString())
    stage.GetRootLayer().Save()


if __name__ == "__main__":
    main()
