import os
from pxr import Usd, UsdGeom, Sdf, Tf


def main():
    stage = Usd.Stage.CreateInMemory()
    primPath = Sdf.Path("/bikeA")
    prim = stage.DefinePrim(primPath, "Xform")
    prim.ApplyAPI("GeomModelAPI")
    primDef = prim.GetPrimDefinition()
    print(primDef.GetAppliedAPISchemas())
    print(primDef.GetPropertyNames())
    prim_type_info = prim.GetPrimTypeInfo()
    print(prim_type_info.GetSchemaTypeName())


if __name__ == "__main__":
    main()
