import os
from pxr import Usd, UsdGeom, Gf


def main():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "HelloWorld.usda"
    )

    if os.path.exists(file_path):
        os.remove(file_path)

    stage = Usd.Stage.CreateNew(file_path)
    world = UsdGeom.Xform.Define(stage, "/World")
    sphere = UsdGeom.Sphere.Define(
        stage, world.GetPath().AppendPath("Sphere"))
    stage.Save()


if __name__ == "__main__":
    main()
