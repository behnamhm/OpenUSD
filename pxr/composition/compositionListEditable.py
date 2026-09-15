import os
from pxr import Sdf, Usd


def main():
    pathListOp = Sdf.PathListOp()
    pathListOp.prependedItems = [Sdf.Path("/cube")]
    pathListOp.appendedItems = [Sdf.Path("/sphere")]
    print(pathListOp)
    pathListOp.Clear()
    print(pathListOp)

    pathListOp = Sdf.PathListOp.Create(prependedItems=[Sdf.Path("/cube")],
                                       appendedItems=[Sdf.Path("/sphere")])
    print(pathListOp)
    pathListOp.deletedItems = [Sdf.Path("/sphere")]
    print(pathListOp)

    pathListOp2 = Sdf.PathListOp.Create(prependedItems=[Sdf.Path("/triangle")],
                                        appendedItems=[Sdf.Path("/square")])
    result = Sdf.PathListOp()
    result = result.ApplyOperations(pathListOp)
    result = result.ApplyOperations(pathListOp2)
    print(result)


if __name__ == "__main__":
    main()
