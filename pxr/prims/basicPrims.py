import os
from pxr import Usd, Kind, Sdf


def main():

    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/cube")
    prim = stage.DefinePrim(primPath, "Xform")
    prim.SetSpecifier(Sdf.SpecifierOver)
    prim.SetTypeName("Cube")
    modelAPI = Usd.ModelAPI(prim)
    if not modelAPI.GetKind():
        modelAPI.SetKind(Kind.Tokens.group)

    print(stage.GetRootLayer().ExportToString())


if __name__ == "__main__":
    main()
