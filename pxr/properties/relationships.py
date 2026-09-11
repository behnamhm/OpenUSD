import os
from pxr import Usd, UsdGeom, Sdf


def main():
    # High level
    stage = Usd.Stage.CreateInMemory()
    bikePrimPath = Sdf.Path("/bikePrim/bike")
    carPrimPath = Sdf.Path("/carPrim/car")
    bikePrim = stage.DefinePrim(bikePrimPath, "Cube")
    carPrim = stage.DefinePrim(carPrimPath, "Sphere")
    favoriteCarRel = bikePrim.CreateRelationship("favoriteCar")
    favoriteCarRel.AddTarget(carPrim.GetPath())
    print(favoriteCarRel.GetForwardedTargets())
    print(stage.GetRootLayer().ExportToString())

    # Low level
    layer = Sdf.Layer.CreateAnonymous()
    cubePrimSpec = Sdf.CreatePrimInLayer(layer, Sdf.Path("/cube_prim"))
    cubePrimSpec.specifier = Sdf.SpecifierDef
    cubePrimSpec.typeName = "Cube"
    spherePrimSpec = Sdf.CreatePrimInLayer(layer, Sdf.Path("/sphere_prim"))
    spherePrimSpec.specifier = Sdf.SpecifierDef
    spherePrimSpec.typeName = "Cube"
    relSpec = Sdf.RelationshipSpec(cubePrimSpec, "proxyPrim")
    relSpec.targetPathList.Append(spherePrimSpec.path)
    print(relSpec.GetAsText())


if __name__ == "__main__":
    main()
