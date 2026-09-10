import os
from pxr import Sdf


def main():
    layer = Sdf.Layer.CreateAnonymous()
    primPath = Sdf.Path("/cube")
    primSpec = Sdf.CreatePrimInLayer(layer, primPath)

    primSpec.specifier = Sdf.SpecifierDef
    primSpec.typeName = "Cube"
    primSpec.active = True
    primSpec.kind = "group"
    primSpec.instanceable = False
    primSpec.hidden = False

    # can be done this way too
    primSpec.SetInfo(primSpec.SpecifierKey, Sdf.SpecifierDef)
    primSpec.SetInfo(primSpec.TypeNameKey, "Cube")
    primSpec.SetInfo(primSpec.ActiveKey, True)
    primSpec.SetInfo(primSpec.KindKey, "group")
    primSpec.SetInfo("instanceable", False)
    primSpec.SetInfo(primSpec.HiddenKey, False)


if __name__ == "__main__":
    main()
