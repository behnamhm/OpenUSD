import os
from pxr import Sdf, Usd


def main():
    # High level
    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/car")

    prim = stage.DefinePrim(primPath, "Xform")
    prim.SetSpecifier(Sdf.SpecifierDef)
    print(stage.GetRootLayer().ExportToString())

    # Low level
    layer = Sdf.Layer.CreateAnonymous()
    primPath = Sdf.Path("/bike")

    primSpec = Sdf.CreatePrimInLayer(layer, primPath)
    primSpec.specifier = Sdf.SpecifierDef


if __name__ == "__main__":
    main()
