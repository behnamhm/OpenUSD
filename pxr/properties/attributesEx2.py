import os
from pxr import Usd, UsdGeom, Sdf


def main():
    # High level
    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/bike")
    prim = stage.DefinePrim(primPath, "Xform")
    attr = prim.CreateAttribute("size", Sdf.ValueTypeNames.Float)
    for frame in range(1001, 1005):
        time_code = Usd.TimeCode(float(frame - 1001))
        attr.Set(frame, time_code)
    print(attr.Get(1005))
    print(stage.GetRootLayer().ExportToString())

    # Low level
    layer = Sdf.Layer.CreateAnonymous()
    primPath = Sdf.Path("/car")
    primSpec = Sdf.CreatePrimInLayer(layer, primPath)
    primSpec.specifier = Sdf.SpecifierDef
    primSpec.typeName = "Cube"
    attrSpec = Sdf.AttributeSpec(primSpec, "size", Sdf.ValueTypeNames.Double)
    for frame in range(1001, 1005):
        value = float(frame - 1001)
        layer.SetTimeSample(attrSpec.path, frame, value)
    print(layer.QueryTimeSample(attrSpec.path, 1004))


if __name__ == "__main__":
    main()
