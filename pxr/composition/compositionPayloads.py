import os
from pxr import Sdf, Usd


def main():
    payload = Sdf.Payload("/file/path.usd", "/prim/path",
                          Sdf.LayerOffset(offset=10, scale=1))
    print(payload.assetPath)
    print(payload.primPath)
    print(payload.layerOffset)
    try:
        payload.assetPath = "/some/other/file/path.usd"
    except Exception:
        print("Read only Sdf.Payload!")


if __name__ == "__main__":
    main()
