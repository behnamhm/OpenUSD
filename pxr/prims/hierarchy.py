import os
from pxr import Sdf, Usd


def main():
    # High level
    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/set/car")
    prim = stage.DefinePrim(primPath, "Xform")
    primParent = prim.GetParent()
    print(prim.GetPath())
    print(prim.GetParent())
    print(primParent.GetChildren())
    print(primParent.GetChildrenNames())

    # Low level
    layer = Sdf.Layer.CreateAnonymous()
    primPath = Sdf.Path("/set/bike")
    primSpec = Sdf.CreatePrimInLayer(layer, primPath)
    print(primSpec.path)
    print(primSpec.name)
    primSpec.name = 'electricBike'
    print(primSpec.nameParent)
    print(primSpec.nameParent.nameChildren)
    print(primSpec.layer)


if __name__ == "__main__":
    main()
