import os
from pxr import Usd, UsdGeom, Gf, Sdf


def createPath(fileName):
    file_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        fileName

    )
    if os.path.exists(file_path):
        os.remove(file_path)
    return file_path


def createInitialStage(path):
    stage = Usd.Stage.CreateNew(path)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    stage.SetStartTimeCode(1)
    stage.SetEndTimeCode(192)
    return stage


def addReferenceToGeometry(stage, path):
    geom = UsdGeom.Xform.Define(stage, path)
    geom.GetPrim().GetReferences().AddReference('./topGeom.usd')
    return geom


def addSpin(top):
    spin = top.AddRotateZOp(opSuffix='spin')
    spin.Set(time=1, value=0)
    spin.Set(time=192, value=1440)


def addTilt(top):
    tilt = top.AddRotateXOp(opSuffix='tilt')
    tilt.Set(value=12)


def firstStep():
    file_path = createPath("transformAnimateStep1.usda")
    stage = createInitialStage(file_path)
    stage.SetMetadata('comment', 'Step 1: start and end time codes')
    stage.Save()


def secondStep():
    file_path = createPath("transformAnimateStep2.usda")
    stage = createInitialStage(file_path)
    stage.SetMetadata('comment', 'Step 2: Geometry reference')
    top = addReferenceToGeometry(stage, '/Top')
    stage.Save()


def thirdStep():
    file_path = createPath("transformAnimateStep3.usda")
    stage = createInitialStage(file_path)
    stage.SetMetadata('comment', 'Step 3: Adding spin animation')
    top = addReferenceToGeometry(stage, '/Top')
    addSpin(top)
    stage.Save()


def forthStep():
    file_path = createPath("transformAnimateStep4.usda")
    stage = createInitialStage(file_path)
    stage.SetMetadata('comment', 'Step 4: Adding tilt')
    top = addReferenceToGeometry(stage, '/Top')
    addTilt(top)
    addSpin(top)
    stage.Save()


def main():
    firstStep()
    secondStep()
    thirdStep()
    forthStep()


if __name__ == "__main__":
    main()
