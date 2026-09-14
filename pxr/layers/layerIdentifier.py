import os
from pxr import Sdf


def main():
    layer = Sdf.Layer.CreateAnonymous()
    print(layer.identifier)
    layer = Sdf.Layer.CreateAnonymous("customAnonLayer")
    print(layer.identifier)
    print(layer.anonymous, layer.resolvedPath or "-",
          layer.realPath or "-", layer.fileExtension)
    print(Sdf.Layer.IsAnonymousLayerIdentifier(layer.identifier))

    layer.identifier = "/my/file/path/example.usd"
    print(layer.anonymous, layer.resolvedPath or "-",
          layer.realPath or "-", layer.fileExtension)


if __name__ == "__main__":
    main()
