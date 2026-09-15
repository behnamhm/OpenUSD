import os
from pxr import Sdf, Usd


def main():
    stage = Usd.Stage.CreateInMemory()
    layerA = Sdf.Layer.CreateAnonymous()
    layerB = Sdf.Layer.CreateAnonymous()
    rootLayer = stage.GetRootLayer()
    rootLayer.subLayerPaths.append(layerA.identifier)
    rootLayer.subLayerPaths.append(layerB.identifier)
    print(rootLayer.subLayerOffsets)

    layerOffsetA = rootLayer.subLayerOffsets[0]
    rootLayer.subLayerOffsets[0] = Sdf.LayerOffset(offset=layerOffsetA.offset + 10,
                                                   scale=layerOffsetA.scale * 2)
    print(rootLayer.subLayerOffsets)


if __name__ == "__main__":
    main()
