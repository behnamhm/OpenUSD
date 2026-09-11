import os
from pxr import Usd, UsdGeom, Sdf


def main():

    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/bike")
    prim = stage.DefinePrim(primPath, "Xform")
    attr = prim.CreateAttribute("tire:size", Sdf.ValueTypeNames.Float)
    attr.Set(10)
    attr.SetMetadata("interpolation", UsdGeom.Tokens.constant)
    print(stage.GetRootLayer().ExportToString())

    # Low level
    layer = Sdf.Layer.CreateAnonymous()
    primPath = Sdf.Path("/car")
    primSpec = Sdf.CreatePrimInLayer(layer, primPath)
    primSpec.specifier = Sdf.SpecifierDef
    primSpec.typeName = "Xform"
    attrSpec = Sdf.AttributeSpec(
        primSpec, "tire:size", Sdf.ValueTypeNames.Double)
    attrSpec.default = 10
    attrSpec.interpolation = UsdGeom.Tokens.constant
    attrSpec.SetInfo("interpolation", UsdGeom.Tokens.constant)
    print(attrSpec.GetAsText())


if __name__ == "__main__":
    main()
