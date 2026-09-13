import os
from pxr import Usd, UsdGeom, Sdf


def main():
    layer = Sdf.Layer.CreateAnonymous()
    primSpec = Sdf.CreatePrimInLayer(layer, "/bike")
    primSpec.specifier = Sdf.SpecifierDef
    primSpec.assetInfo = {"identifer": Sdf.AssetPath("bike.usd")}
    primSpec.assetInfo["version"] = "v001"
    primSpec.customData = {"myData": "myValue"}

    print(primSpec.ListInfoKeys())
    print(primSpec.GetMetaDataInfoKeys())
    print(primSpec.assetInfo)


if __name__ == "__main__":
    main()
