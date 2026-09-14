import os
from pxr import Sdf


def main():
    filePath = os.path.join(
        os.path.dirname(__file__),
        "..",
        "assets",
        "layerIdentifierExample.usd"
    )

    if os.path.exists(filePath):
        os.remove(filePath)

    layer = Sdf.Layer.CreateNew(filePath)
    primSpec = Sdf.CreatePrimInLayer(layer, Sdf.Path("/cube"))
    primSpec.typeName = "Cube"
    print(layer.dirty)
    layer.Save()

    otherLayer = Sdf.Layer.CreateAnonymous()
    otherLayer.TransferContent(layer)
    print(otherLayer.ExportToString())


if __name__ == "__main__":
    main()
