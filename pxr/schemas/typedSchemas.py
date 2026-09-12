import os
from pxr import Usd, UsdGeom, Sdf


def main():
    # High level
    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/bikeA")
    cubePrim = stage.DefinePrim(primPath, "Cube")
    # define prim via typedSchema
    primPath = Sdf.Path("/bikeB")
    primTypedSchema = UsdGeom.Cube.Define(stage, primPath)
    prim = primTypedSchema.GetPrim()
    print(prim.IsA(UsdGeom.Cube))
    print(prim.IsA(UsdGeom.Boundable))
    print(primTypedSchema.GetSizeAttr().Get())

    # Low level
    layer = Sdf.Layer.CreateAnonymous()
    primPath = Sdf.Path("/bikeC")
    prim_spec = Sdf.CreatePrimInLayer(layer, primPath)
    prim_spec.typeName = "Cube"


if __name__ == "__main__":
    main()
