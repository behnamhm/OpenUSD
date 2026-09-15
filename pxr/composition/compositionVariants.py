import os
from pxr import Sdf, Usd


def main():
    stage = Usd.Stage.CreateInMemory()
    bikePrimPath = Sdf.Path("/bike")
    bikePrim = stage.DefinePrim(bikePrimPath)
    variantsSetsAPI = bikePrim.GetVariantSets()
    variantsSetsAPI = variantsSetsAPI.AddVariantSet("color",
                                                    position=Usd.ListPositionBackOfPrependList)
    variantsSetsAPI.AddVariant("colorA")
    variantsSetsAPI.SetVariantSelection("colorA")
    with variantsSetsAPI.GetVariantEditContext():
        carPrimPath = bikePrimPath.AppendChild("car")
        carPrim = stage.DefinePrim(carPrimPath)

    print(stage.GetRootLayer().ExportToString())


if __name__ == "__main__":
    main()
