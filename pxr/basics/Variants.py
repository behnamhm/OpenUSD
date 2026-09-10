import os
from pxr import Usd, UsdGeom, Gf


def main():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "HelloWorld.usda"
    )

    stage = Usd.Stage.Open(file_path)
    colorAttribute = UsdGeom.Gprim.Get(
        stage, '/World/Sphere').GetDisplayColorAttr()
    colorAttribute.Clear()

    rootPrim = stage.GetPrimAtPath('/World')
    vSet = rootPrim.GetVariantSets().AddVariantSet('shadingVariant')

    vSet.AddVariant('red')
    vSet.AddVariant('blue')
    vSet.AddVariant('green')

    vSet.SetVariantSelection('red')
    with vSet.GetVariantEditContext():
        colorAttribute.Set([(1, 0, 0)])
    vSet.SetVariantSelection('green')
    with vSet.GetVariantEditContext():
        colorAttribute.Set([(0, 1, 0)])
    vSet.SetVariantSelection('blue')
    with vSet.GetVariantEditContext():
        colorAttribute.Set([(0, 0, 1)])
    print(stage.GetRootLayer().ExportToString())

    file_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "HelloWorldWithVariants.usda"
    )
    stage.GetRootLayer().Export(file_path)


if __name__ == "__main__":
    main()
