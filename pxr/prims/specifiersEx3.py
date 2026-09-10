import os
from pxr import Sdf, Usd


def main():
    # High level
    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/car")

    prim = stage.DefinePrim(primPath, "Xform")
    prim.SetSpecifier(Sdf.SpecifierClass)
    prim = stage.CreateClassPrim(primPath)
    print(stage.GetRootLayer().ExportToString())

    # Low level
    layer = Sdf.Layer.CreateAnonymous()
    primPath = Sdf.Path("/bike")

    primSpec = Sdf.CreatePrimInLayer(layer, primPath)
    primSpec.specifier = Sdf.SpecifierClass


if __name__ == "__main__":
    main()
