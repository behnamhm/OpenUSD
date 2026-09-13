import os
from pxr import Usd, UsdGeom, Sdf


def main():
    # High level
    stage = Usd.Stage.CreateInMemory()
    bikePrimPath = Sdf.Path("/bike")
    bikePrim = stage.DefinePrim(bikePrimPath, "Xform")
    bikePrim.SetAssetInfoByKey("identifier",
                               Sdf.AssetPath("bike.usd"))
    bikePrim.SetAssetInfoByKey("nested",
                               {"assetPath": Sdf.AssetPath("bike.usd"), "version": "1"})
    bikePrim.SetMetadataByDictKey("assetInfo",
                                  "nested:color", "blue")
    attr = bikePrim.CreateAttribute("tire:size",
                                    Sdf.ValueTypeNames.Float)
    attr.SetMetadata("customData", {"sizeUnit": "meter"})
    attr.SetCustomDataByKey("nested:shape", "round")

    print(bikePrim.HasAuthoredMetadata("assetInfo"))
    print(bikePrim.HasAuthoredMetadataDictKey("assetInfo", "identifier"))
    print(bikePrim.HasMetadata("assetInfo"))
    print(bikePrim.HasMetadataDictKey("assetInfo", "nested:color"))

    print(bikePrim.GetAssetInfo())
    print(bikePrim.GetAssetInfoByKey("nested:color"))

    for attr in bikePrim.GetAttributes():
        print(attr.GetName())


if __name__ == "__main__":
    main()
