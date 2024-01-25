from ctypes import *
sdl=cdll.LoadLibrary("libSDL-1.2.so.0")
openb3d=cdll.LoadLibrary("./libOpenB3D.so")

def Graphics3D(w,h,d=0,m=0):
	sdl.SDL_Init(65535)
	sdl.SDL_SetVideoMode(w,h,d,2)
	openb3d.Graphics3D(w,h,d,m)

AddAnimSeq=openb3d.AddAnimSeq
AddAnimSeq.argtypes = [c_void_p, c_int]
AddAnimSeq.restype = c_int

AddMesh=openb3d.AddMesh
AddMesh.argtypes = [c_void_p, c_void_p]

AddTriangle=openb3d.AddTriangle
AddTriangle.argtypes = [c_void_p, c_int, c_int, c_int]
AddTriangle.restype = c_int

AddVertex=openb3d.AddVertex
AddVertex.argtypes = [c_void_p, c_float, c_float, c_float, c_float, c_float, c_float]
AddVertex.restype = c_int

AmbientLight=openb3d.AmbientLight
AmbientLight.argtypes = [c_float, c_float, c_float]

Animate=openb3d.Animate
Animate.argtypes = [c_void_p, c_int, c_float, c_int, c_int]

Animating=openb3d.Animating
Animating.argtypes = [c_void_p]
Animating.restype = c_int

AnimLength=openb3d.AnimLength
AnimLength.argtypes = [c_void_p]
AnimLength.restype = c_int

AnimSeq=openb3d.AnimSeq
AnimSeq.argtypes = [c_void_p]
AnimSeq.restype = c_int

AnimTime=openb3d.AnimTime
AnimTime.argtypes = [c_void_p]
AnimTime.restype = c_float

BackBufferToTex=openb3d.BackBufferToTex
BackBufferToTex.argtypes = [c_void_p, c_int]

BrushAlpha=openb3d.BrushAlpha
BrushAlpha.argtypes = [c_void_p, c_float]

BrushBlend=openb3d.BrushBlend
BrushBlend.argtypes = [c_void_p, c_int]

BrushColor=openb3d.BrushColor
BrushColor.argtypes = [c_void_p, c_float, c_float, c_float]

BrushFX=openb3d.BrushFX
BrushFX.argtypes = [c_void_p, c_int]

BrushShininess=openb3d.BrushShininess
BrushShininess.argtypes = [c_void_p, c_float]

BrushTexture=openb3d.BrushTexture
BrushTexture.argtypes = [c_void_p, c_void_p, c_int, c_int]

CameraClsColor=openb3d.CameraClsColor
CameraClsColor.argtypes = [c_void_p, c_float, c_float, c_float]

CameraClsMode=openb3d.CameraClsMode
CameraClsMode.argtypes = [c_void_p, c_int, c_int]

CameraFogColor=openb3d.CameraFogColor
CameraFogColor.argtypes = [c_void_p, c_float, c_float, c_float]

CameraFogMode=openb3d.CameraFogMode
CameraFogMode.argtypes = [c_void_p, c_int]

CameraFogRange=openb3d.CameraFogRange
CameraFogRange.argtypes = [c_void_p, c_float, c_float]

CameraPick=openb3d.CameraPick
CameraPick.argtypes = [c_void_p, c_float, c_float]
CameraPick.restype = c_void_p

CameraProject=openb3d.CameraProject
CameraProject.argtypes = [c_void_p, c_float, c_float, c_float]

CameraProjMode=openb3d.CameraProjMode
CameraProjMode.argtypes = [c_void_p, c_int]

CameraToTex=openb3d.CameraToTex
CameraToTex.argtypes = [c_void_p, c_void_p, c_int]

CameraRange=openb3d.CameraRange
CameraRange.argtypes = [c_void_p, c_float, c_float]

CameraViewport=openb3d.CameraViewport
CameraViewport.argtypes = [c_void_p, c_int, c_int, c_int, c_int]

CameraZoom=openb3d.CameraZoom
CameraZoom.argtypes = [c_void_p, c_float]

ClearCollisions=openb3d.ClearCollisions

ClearSurface=openb3d.ClearSurface
ClearSurface.argtypes = [c_void_p, c_bool, c_bool]

ClearTextureFilters=openb3d.ClearTextureFilters

ClearWorld=openb3d.ClearWorld
ClearWorld.argtypes = [c_bool, c_bool, c_bool]

CollisionEntity=openb3d.CollisionEntity
CollisionEntity.argtypes = [c_void_p, c_int]
CollisionEntity.restype = c_void_p

Collisions=openb3d.Collisions
Collisions.argtypes = [c_int, c_int, c_int, c_int]

CollisionNX=openb3d.CollisionNX
CollisionNX.argtypes = [c_void_p, c_int]
CollisionNX.restype = c_float

CollisionNY=openb3d.CollisionNY
CollisionNY.argtypes = [c_void_p, c_int]
CollisionNY.restype = c_float

CollisionNZ=openb3d.CollisionNZ
CollisionNZ.argtypes = [c_void_p, c_int]
CollisionNZ.restype = c_float

CollisionSurface=openb3d.CollisionSurface
CollisionSurface.argtypes = [c_void_p, c_int]
CollisionSurface.restype = c_void_p

CollisionTime=openb3d.CollisionTime
CollisionTime.argtypes = [c_void_p, c_int]
CollisionTime.restype = c_float

CollisionTriangle=openb3d.CollisionTriangle
CollisionTriangle.argtypes = [c_void_p, c_int]
CollisionTriangle.restype = c_int

CollisionX=openb3d.CollisionX
CollisionX.argtypes = [c_void_p, c_int]
CollisionX.restype = c_float

CollisionY=openb3d.CollisionY
CollisionY.argtypes = [c_void_p, c_int]
CollisionY.restype = c_float

CollisionZ=openb3d.CollisionZ
CollisionZ.argtypes = [c_void_p, c_int]
CollisionZ.restype = c_float

CountChildren=openb3d.CountChildren
CountChildren.argtypes = [c_void_p]
CountChildren.restype = c_int

CountCollisions=openb3d.CountCollisions
CountCollisions.argtypes = [c_void_p]
CountCollisions.restype = c_int

CopyEntity=openb3d.CopyEntity
CopyEntity.argtypes = [c_void_p, c_void_p]
CopyEntity.restype = c_void_p

CopyMesh=openb3d.CopyMesh
CopyMesh.argtypes = [c_void_p, c_void_p]
CopyMesh.restype = c_void_p

CountSurfaces=openb3d.CountSurfaces
CountSurfaces.argtypes = [c_void_p]
CountSurfaces.restype = c_int

CountTriangles=openb3d.CountTriangles
CountTriangles.argtypes = [c_void_p]
CountTriangles.restype = c_int

CountVertices=openb3d.CountVertices
CountVertices.argtypes = [c_void_p]
CountVertices.restype = c_int

CreateBlob=openb3d.CreateBlob
CreateBlob.argtypes = [c_void_p, c_float, c_void_p]
CreateBlob.restype = c_void_p

CreateBone=openb3d.CreateBone
CreateBone.argtypes = [c_void_p, c_void_p]
CreateBone.restype = c_void_p

CreateBrush=openb3d.CreateBrush
CreateBrush.argtypes = [c_float, c_float, c_float]
CreateBrush.restype = c_void_p

CreateCamera=openb3d.CreateCamera
CreateCamera.argtypes = [c_void_p]
CreateCamera.restype = c_void_p

CreateConstraint=openb3d.CreateConstraint
CreateConstraint.argtypes = [c_void_p, c_void_p, c_float]
CreateConstraint.restype = c_void_p

CreateCone=openb3d.CreateCone
CreateCone.argtypes = [c_int, c_bool, c_void_p]
CreateCone.restype = c_void_p

CreateCylinder=openb3d.CreateCylinder
CreateCylinder.argtypes = [c_int, c_bool, c_void_p]
CreateCylinder.restype = c_void_p

CreateCube=openb3d.CreateCube
CreateCube.argtypes = [c_void_p]
CreateCube.restype = c_void_p

CreateFluid=openb3d.CreateFluid
CreateFluid.restype = c_void_p

CreateGeosphere=openb3d.CreateGeosphere
CreateGeosphere.argtypes = [c_int, c_void_p]
CreateGeosphere.restype = c_void_p

CreateMesh=openb3d.CreateMesh
CreateMesh.argtypes = [c_void_p]
CreateMesh.restype = c_void_p

CreateLight=openb3d.CreateLight
CreateLight.argtypes = [c_int, c_void_p]
CreateLight.restype = c_void_p

CreatePivot=openb3d.CreatePivot
CreatePivot.argtypes = [c_void_p]
CreatePivot.restype = c_void_p

CreatePlane=openb3d.CreatePlane
CreatePlane.argtypes = [c_int, c_void_p]
CreatePlane.restype = c_void_p

CreateQuad=openb3d.CreateQuad
CreateQuad.argtypes = [c_void_p]
CreateQuad.restype = c_void_p

CreateRigidBody=openb3d.CreateRigidBody
CreateRigidBody.argtypes = [c_void_p, c_void_p, c_void_p, c_void_p, c_void_p]
CreateRigidBody.restype = c_void_p

CreateShadow=openb3d.CreateShadow
CreateShadow.argtypes = [c_void_p, c_char]
CreateShadow.restype = c_void_p

CreateSphere=openb3d.CreateSphere
CreateSphere.argtypes = [c_int, c_void_p]
CreateSphere.restype = c_void_p

CreateSprite=openb3d.CreateSprite
CreateSprite.argtypes = [c_void_p]
CreateSprite.restype = c_void_p

CreateSurface=openb3d.CreateSurface
CreateSurface.argtypes = [c_void_p, c_void_p]
CreateSurface.restype = c_void_p

CreateStencil=openb3d.CreateStencil
CreateStencil.restype = c_void_p

CreateTerrain=openb3d.CreateTerrain
CreateTerrain.argtypes = [c_int, c_void_p]
CreateTerrain.restype = c_void_p

CreateTexture=openb3d.CreateTexture
CreateTexture.argtypes = [c_int, c_int, c_int, c_int]
CreateTexture.restype = c_void_p

CreateVoxelSprite=openb3d.CreateVoxelSprite
CreateVoxelSprite.argtypes = [c_int, c_void_p]
CreateVoxelSprite.restype = c_void_p

DeltaPitch=openb3d.DeltaPitch
DeltaPitch.argtypes = [c_void_p, c_void_p]
DeltaPitch.restype = c_float

DeltaYaw=openb3d.DeltaYaw
DeltaYaw.argtypes = [c_void_p, c_void_p]
DeltaYaw.restype = c_float

DepthBufferToTex=openb3d.DepthBufferToTex
DepthBufferToTex.argtypes = [c_void_p, c_void_p]

EmitterVector=openb3d.EmitterVector
EmitterVector.argtypes = [c_void_p, c_float, c_float, c_float]

EmitterRate=openb3d.EmitterRate
EmitterRate.argtypes = [c_void_p, c_float]

EmitterParticleLife=openb3d.EmitterParticleLife
EmitterParticleLife.argtypes = [c_void_p, c_int]

EmitterParticleSpeed=openb3d.EmitterParticleSpeed
EmitterParticleSpeed.argtypes = [c_void_p, c_float]

EmitterVariance=openb3d.EmitterVariance
EmitterVariance.argtypes = [c_void_p, c_float]

EntityAlpha=openb3d.EntityAlpha
EntityAlpha.argtypes = [c_void_p, c_float]

EntityBlend=openb3d.EntityBlend
EntityBlend.argtypes = [c_void_p, c_int]

EntityBox=openb3d.EntityBox
EntityBox.argtypes = [c_void_p, c_float, c_float, c_float, c_float, c_float, c_float]

EntityClass=openb3d.EntityClass
EntityClass.argtypes = [c_void_p]
EntityClass.restype = c_char_p

EntityCollided=openb3d.EntityCollided
EntityCollided.argtypes = [c_void_p, c_int]
EntityCollided.restype = c_void_p

EntityColor=openb3d.EntityColor
EntityColor.argtypes = [c_void_p, c_float, c_float, c_float]

EntityDistance=openb3d.EntityDistance
EntityDistance.argtypes = [c_void_p, c_void_p]
EntityDistance.restype = c_float

EntityFX=openb3d.EntityFX
EntityFX.argtypes = [c_void_p, c_int]

EntityInView=openb3d.EntityInView
EntityInView.argtypes = [c_void_p, c_void_p]
EntityInView.restype = c_float

EntityName=openb3d.EntityName
EntityName.argtypes = [c_void_p]
EntityName.restype = c_char_p

EntityOrder=openb3d.EntityOrder
EntityOrder.argtypes = [c_void_p, c_int]

EntityParent=openb3d.EntityParent
EntityParent.argtypes = [c_void_p, c_void_p, c_bool]

EntityPick=openb3d.EntityPick
EntityPick.argtypes = [c_void_p, c_float]
EntityPick.restype = c_void_p

EntityPickMode=openb3d.EntityPickMode
EntityPickMode.argtypes = [c_void_p, c_int, c_bool]

EntityPitch=openb3d.EntityPitch
EntityPitch.argtypes = [c_void_p, c_bool]
EntityPitch.restype = c_float

EntityRadius=openb3d.EntityRadius
EntityRadius.argtypes = [c_void_p, c_float, c_float]

EntityRoll=openb3d.EntityRoll
EntityRoll.argtypes = [c_void_p, c_bool]
EntityRoll.restype = c_float

EntityShininess=openb3d.EntityShininess
EntityShininess.argtypes = [c_void_p, c_bool]
EntityShininess.restype = c_float

EntityTexture=openb3d.EntityTexture
EntityTexture.argtypes = [c_void_p, c_void_p, c_int, c_int]

EntityType=openb3d.EntityType
EntityType.argtypes = [c_void_p, c_int, c_bool]

EntityVisible=openb3d.EntityVisible
EntityVisible.argtypes = [c_void_p, c_void_p]
EntityVisible.restype = c_int

EntityX=openb3d.EntityX
EntityX.argtypes = [c_void_p, c_bool]
EntityX.restype = c_float

EntityY=openb3d.EntityY
EntityY.argtypes = [c_void_p, c_bool]
EntityY.restype = c_float

EntityYaw=openb3d.EntityYaw
EntityYaw.argtypes = [c_void_p, c_bool]
EntityYaw.restype = c_float

EntityZ=openb3d.EntityZ
EntityZ.argtypes = [c_void_p, c_bool]
EntityZ.restype = c_float

ExtractAnimSeq=openb3d.ExtractAnimSeq
ExtractAnimSeq.argtypes = [c_void_p, c_int, c_int, c_int]
ExtractAnimSeq.restype = c_int

FindChild=openb3d.FindChild
FindChild.argtypes = [c_void_p, c_char_p]
FindChild.restype = c_void_p

FitMesh=openb3d.FitMesh
FitMesh.argtypes = [c_void_p, c_float, c_float, c_float, c_float, c_float, c_float, c_bool]

FlipMesh=openb3d.FlipMesh
FlipMesh.argtypes = [c_void_p, c_bool]

FluidThreshold=openb3d.FluidThreshold
FluidThreshold.argtypes = [c_void_p, c_float]

FreeBrush=openb3d.FreeBrush
FreeBrush.argtypes = [c_void_p]

FreeConstraint=openb3d.FreeConstraint
FreeConstraint.argtypes = [c_void_p]

FreeEntity=openb3d.FreeEntity
FreeEntity.argtypes = [c_void_p]

FreeRigidBody=openb3d.FreeRigidBody
FreeRigidBody.argtypes = [c_void_p]

FreeShader=openb3d.FreeShader
FreeShader.argtypes = [c_void_p]

FreeShadow=openb3d.FreeShadow
FreeShadow.argtypes = [c_void_p]

FreeTexture=openb3d.FreeTexture
FreeTexture.argtypes = [c_void_p]

GeosphereHeight=openb3d.GeosphereHeight
GeosphereHeight.argtypes = [c_void_p, c_float]

GetBrushTexture=openb3d.GetBrushTexture
GetBrushTexture.argtypes = [c_void_p, c_int]
GetBrushTexture.restype = c_void_p

GetChild=openb3d.GetChild
GetChild.argtypes = [c_void_p, c_int]
GetChild.restype = c_void_p

GetEntityBrush=openb3d.GetEntityBrush
GetEntityBrush.argtypes = [c_void_p]
GetEntityBrush.restype = c_void_p

GetEntityType=openb3d.GetEntityType
GetEntityType.argtypes = [c_void_p]
GetEntityType.restype = c_int

GetParentEntity=openb3d.GetParentEntity
GetParentEntity.argtypes = [c_void_p]
GetParentEntity.restype = c_void_p

GetSurface=openb3d.GetSurface
GetSurface.argtypes = [c_void_p, c_int]
GetSurface.restype = c_void_p

GetSurfaceBrush=openb3d.GetSurfaceBrush
GetSurfaceBrush.argtypes = [c_void_p]
GetSurfaceBrush.restype = c_void_p

HandleSprite=openb3d.HandleSprite
HandleSprite.argtypes = [c_void_p, c_float, c_float]

HideEntity=openb3d.HideEntity
HideEntity.argtypes = [c_void_p]

LightColor=openb3d.LightColor
LightColor.argtypes = [c_void_p, c_float, c_float, c_float]

LightConeAngles=openb3d.LightConeAngles
LightConeAngles.argtypes = [c_void_p, c_float, c_float]

LightRange=openb3d.LightRange
LightRange.argtypes = [c_void_p, c_float]

LinePick=openb3d.LinePick
LinePick.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float, c_float]
LinePick.restype = c_void_p

LoadAnimMesh=openb3d.LoadAnimMesh
LoadAnimMesh.argtypes = [c_char_p, c_void_p]
LoadAnimMesh.restype = c_void_p

LoadAnimSeq=openb3d.LoadAnimSeq
LoadAnimSeq.argtypes = [c_void_p, c_char_p]
LoadAnimSeq.restype = c_int

LoadAnimTexture=openb3d.LoadAnimTexture
LoadAnimTexture.argtypes = [c_char_p, c_int, c_int, c_int, c_int, c_int]
LoadAnimTexture.restype = c_void_p

LoadBrush=openb3d.LoadBrush
LoadBrush.argtypes = [c_char_p, c_int, c_float, c_float]
LoadBrush.restype = c_void_p

LoadGeosphere=openb3d.LoadGeosphere
LoadGeosphere.argtypes = [c_char_p, c_void_p]
LoadGeosphere.restype = c_void_p

LoadMesh=openb3d.LoadMesh
LoadMesh.argtypes = [c_char_p, c_void_p]
LoadMesh.restype = c_void_p

LoadTerrain=openb3d.LoadTerrain
LoadTerrain.argtypes = [c_char_p, c_void_p]
LoadTerrain.restype = c_void_p

LoadTexture=openb3d.LoadTexture
LoadTexture.argtypes = [c_char_p, c_int]
LoadTexture.restype = c_void_p

LoadSprite=openb3d.LoadSprite
LoadSprite.argtypes = [c_char_p, c_int, c_void_p]
LoadSprite.restype = c_void_p

MeshCSG=openb3d.MeshCSG
MeshCSG.argtypes = [c_void_p, c_void_p, c_int]
MeshCSG.restype = c_void_p

MeshCullRadius=openb3d.MeshCullRadius
MeshCullRadius.argtypes = [c_void_p, c_float]

MeshDepth=openb3d.MeshDepth
MeshDepth.argtypes = [c_void_p]
MeshDepth.restype = c_float

MeshesIntersect=openb3d.MeshesIntersect
MeshesIntersect.argtypes = [c_void_p, c_void_p]
MeshesIntersect.restype = c_int

MeshHeight=openb3d.MeshHeight
MeshHeight.argtypes = [c_void_p]
MeshHeight.restype = c_float

MeshWidth=openb3d.MeshWidth
MeshWidth.argtypes = [c_void_p]
MeshWidth.restype = c_float

ModifyGeosphere=openb3d.ModifyTerrain
ModifyGeosphere.argtypes = [c_void_p, c_int, c_int, c_float]

ModifyTerrain=openb3d.ModifyTerrain
ModifyTerrain.argtypes = [c_void_p, c_int, c_int, c_float]

MoveEntity=openb3d.MoveEntity
MoveEntity.argtypes = [c_void_p, c_float, c_float, c_float]

NameEntity=openb3d.NameEntity
NameEntity.argtypes = [c_void_p, c_char_p]

PaintEntity=openb3d.PaintEntity
PaintEntity.argtypes = [c_void_p, c_void_p]

PaintMesh=openb3d.PaintMesh
PaintMesh.argtypes = [c_void_p, c_void_p]

PaintSurface=openb3d.PaintSurface
PaintSurface.argtypes = [c_void_p, c_void_p]

ParticleColor=openb3d.ParticleColor
ParticleColor.argtypes = [c_void_p, c_float, c_float, c_float, c_float]

ParticleVector=openb3d.ParticleVector
ParticleVector.argtypes = [c_void_p, c_float, c_float, c_float]

ParticleTrail=openb3d.ParticleTrail
ParticleTrail.argtypes = [c_void_p, c_int]

PickedEntity=openb3d.PickedEntity
PickedEntity.restype = c_void_p

PickedNX=openb3d.PickedNX
PickedNX.restype = c_float

PickedNY=openb3d.PickedNY
PickedNY.restype = c_float

PickedNZ=openb3d.PickedNZ
PickedNZ.restype = c_float

PickedSurface=openb3d.PickedSurface
PickedSurface.restype = c_void_p

PickedTime=openb3d.PickedTime
PickedTime.restype = c_float

PickedTriangle=openb3d.PickedTriangle
PickedTriangle.restype = c_int

PickedX=openb3d.PickedX
PickedX.restype = c_float

PickedY=openb3d.PickedY
PickedY.restype = c_float

PickedZ=openb3d.PickedZ
PickedZ.restype = c_float

PointEntity=openb3d.PointEntity
PointEntity.argtypes = [c_void_p, c_void_p, c_float]

PositionEntity=openb3d.PositionEntity
PositionEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]

PositionMesh=openb3d.PositionMesh
PositionMesh.argtypes = [c_void_p, c_float, c_float, c_float]

PositionTexture=openb3d.PositionTexture
PositionTexture.argtypes = [c_void_p, c_float, c_float]

ProjectedX=openb3d.ProjectedX
ProjectedX.restype = c_float

ProjectedY=openb3d.ProjectedY
ProjectedY.restype = c_float

ProjectedZ=openb3d.ProjectedZ
ProjectedZ.restype = c_float

RenderWorld=openb3d.RenderWorld

RepeatMesh=openb3d.RepeatMesh
RepeatMesh.argtypes = [c_void_p, c_void_p]
RepeatMesh.restype = c_void_p

ResetEntity=openb3d.ResetEntity
ResetEntity.argtypes = [c_void_p]

ResetShadow=openb3d.ResetShadow
ResetShadow.argtypes = [c_void_p]

RotateEntity=openb3d.RotateEntity
RotateEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]

RotateMesh=openb3d.RotateMesh
RotateMesh.argtypes = [c_void_p, c_float, c_float, c_float]

RotateSprite=openb3d.RotateSprite
RotateSprite.argtypes = [c_void_p, c_float]

RotateTexture=openb3d.RotateTexture
RotateTexture.argtypes = [c_void_p, c_float]

ScaleEntity=openb3d.ScaleEntity
ScaleEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]

ScaleMesh=openb3d.ScaleMesh
ScaleMesh.argtypes = [c_void_p, c_float, c_float, c_float]

ScaleSprite=openb3d.ScaleSprite
ScaleSprite.argtypes = [c_void_p, c_float, c_float]

ScaleTexture=openb3d.ScaleTexture
ScaleTexture.argtypes = [c_void_p, c_float, c_float]

SetAnimKey=openb3d.SetAnimKey
SetAnimKey.argtypes = [c_void_p, c_float, c_int, c_int, c_int]

SetAnimTime=openb3d.SetAnimTime
SetAnimTime.argtypes = [c_void_p, c_float, c_int]

SetCubeFace=openb3d.SetCubeFace
SetCubeFace.argtypes = [c_void_p, c_int]

SetCubeMode=openb3d.SetCubeFace
SetCubeMode.argtypes = [c_void_p, c_int]

ShowEntity=openb3d.ShowEntity
ShowEntity.argtypes = [c_void_p]

SkinMesh=openb3d.SkinMesh
SkinMesh.argtypes = [c_void_p, c_int, c_int, c_int, c_float, c_int, c_float, c_int, c_float, c_int, c_float]

SpriteRenderMode=openb3d.SpriteRenderMode
SpriteRenderMode.argtypes = [c_void_p, c_int]

SpriteViewMode=openb3d.SpriteViewMode
SpriteViewMode.argtypes = [c_void_p, c_int]

StencilAlpha=openb3d.StencilAlpha
StencilAlpha.argtypes = [c_void_p, c_float]

StencilClsColor=openb3d.StencilClsColor
StencilClsColor.argtypes = [c_void_p, c_float, c_float, c_float]

StencilClsMode=openb3d.StencilClsMode
StencilClsMode.argtypes = [c_void_p, c_int, c_int]

StencilMesh=openb3d.StencilMesh
StencilMesh.argtypes = [c_void_p, c_void_p, c_int]

StencilMode=openb3d.StencilMode
StencilMode.argtypes = [c_void_p, c_int, c_int]

TerrainHeight=openb3d.TerrainHeight
TerrainHeight.argtypes = [c_void_p, c_int, c_int]
TerrainHeight.restype = c_float

TerrainX=openb3d.TerrainX
TerrainX.argtypes = [c_void_p, c_float, c_float, c_float]
TerrainX.restype = c_float

TerrainY=openb3d.TerrainY
TerrainY.argtypes = [c_void_p, c_float, c_float, c_float]
TerrainY.restype = c_float

TerrainZ=openb3d.TerrainZ
TerrainZ.argtypes = [c_void_p, c_float, c_float, c_float]
TerrainZ.restype = c_float

TextureBlend=openb3d.TextureBlend
TextureBlend.argtypes = [c_void_p, c_int]

TextureCoords=openb3d.TextureCoords
TextureCoords.argtypes = [c_void_p, c_int]

TextureHeight=openb3d.TextureHeight
TextureHeight.argtypes = [c_void_p]
TextureHeight.restype = c_int

TextureFilter=openb3d.TextureFilter
TextureFilter.argtypes = [c_char_p, c_int]

TextureName=openb3d.TextureName
TextureName.argtypes = [c_void_p]
TextureName.restype = c_char_p

TextureWidth=openb3d.TextureWidth
TextureWidth.argtypes = [c_void_p]
TextureWidth.restype = c_int

TFormedX=openb3d.TFormedX
TFormedX.restype = c_float

TFormedY=openb3d.TFormedY
TFormedY.restype = c_float

TFormedZ=openb3d.TFormedZ
TFormedZ.restype = c_float

TFormNormal=openb3d.TFormNormal
TFormNormal.argtypes = [c_float, c_float, c_float, c_void_p, c_void_p]

TFormPoint=openb3d.TFormPoint
TFormPoint.argtypes = [c_float, c_float, c_float, c_void_p, c_void_p]

TFormVector=openb3d.TFormVector
TFormVector.argtypes = [c_float, c_float, c_float, c_void_p, c_void_p]

TranslateEntity=openb3d.TranslateEntity
TranslateEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]

TriangleVertex=openb3d.TriangleVertex
TriangleVertex.argtypes = [c_void_p, c_int, c_int]
TriangleVertex.restype = c_int

TurnEntity=openb3d.TurnEntity
TurnEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]

UpdateNormals=openb3d.UpdateNormals
UpdateNormals.argtypes = [c_void_p]

UpdateTexCoords=openb3d.UpdateTexCoords
UpdateTexCoords.argtypes = [c_void_p]

UpdateWorld=openb3d.UpdateWorld
UpdateWorld.argtypes=[c_float]

UseStencil=openb3d.UseStencil
UseStencil.argtypes = [c_void_p]

VectorPitch=openb3d.VectorPitch
VectorPitch.argtypes = [c_float, c_float, c_float]
VectorPitch.restype = c_float

VectorYaw=openb3d.VectorYaw
VectorYaw.argtypes = [c_float, c_float, c_float]
VectorYaw.restype = c_float

VertexAlpha=openb3d.VertexAlpha
VertexAlpha.argtypes = [c_void_p, c_int]
VertexAlpha.restype = c_float

VertexBlue=openb3d.VertexBlue
VertexBlue.argtypes = [c_void_p, c_int]
VertexBlue.restype = c_float

VertexColor=openb3d.VertexColor
VertexColor.argtypes = [c_void_p, c_int, c_float, c_float, c_float, c_float]

VertexCoords=openb3d.VertexCoords
VertexCoords.argtypes = [c_void_p, c_int, c_float, c_float, c_float]

VertexGreen=openb3d.VertexGreen
VertexGreen.argtypes = [c_void_p, c_int]
VertexGreen.restype = c_float

VertexNormal=openb3d.VertexNormal
VertexNormal.argtypes = [c_void_p, c_int, c_float, c_float, c_float]

VertexNX=openb3d.VertexNX
VertexNX.argtypes = [c_void_p, c_int]
VertexNX.restype = c_float

VertexNY=openb3d.VertexNY
VertexNY.argtypes = [c_void_p, c_int]
VertexNY.restype = c_float

VertexNZ=openb3d.VertexNZ
VertexNZ.argtypes = [c_void_p, c_int]
VertexNZ.restype = c_float

VertexRed=openb3d.VertexRed
VertexRed.argtypes = [c_void_p, c_int]
VertexRed.restype = c_float

VertexTexCoords=openb3d.VertexTexCoords
VertexTexCoords.argtypes = [c_void_p, c_int, c_float, c_float, c_float, c_int]

VertexU=openb3d.VertexU
VertexU.argtypes = [c_void_p, c_int, c_int]
VertexU.restype = c_float

VertexV=openb3d.VertexV
VertexV.argtypes = [c_void_p, c_int, c_int]
VertexV.restype = c_float

VertexW=openb3d.VertexW
VertexW.argtypes = [c_void_p, c_int, c_int]
VertexW.restype = c_float

VertexX=openb3d.VertexX
VertexX.argtypes = [c_void_p, c_int]
VertexX.restype = c_float

VertexY=openb3d.VertexY
VertexY.argtypes = [c_void_p, c_int]
VertexY.restype = c_float

VertexZ=openb3d.VertexZ
VertexZ.argtypes = [c_void_p, c_int]
VertexZ.restype = c_float

VoxelSpriteMaterial=openb3d.VoxelSpriteMaterial
VoxelSpriteMaterial.argtypes = [c_void_p, c_void_p]

Wireframe=openb3d.Wireframe
Wireframe.argtypes = [c_int]

EntityScaleX=openb3d.EntityScaleX
EntityScaleX.argtypes = [c_void_p, c_bool]
EntityScaleX.restype = c_float

EntityScaleY=openb3d.EntityScaleY
EntityScaleY.argtypes = [c_void_p, c_bool]
EntityScaleY.restype = c_float

EntityScaleZ=openb3d.EntityScaleZ
EntityScaleZ.argtypes = [c_void_p, c_bool]
EntityScaleZ.restype = c_float

LoadShader=openb3d.LoadShader
LoadShader.argtypes = [c_char_p, c_char_p, c_char_p]
LoadShader.restype = c_void_p

CreateShader=openb3d.CreateShader
CreateShader.argtypes = [c_char_p, c_char_p, c_char_p]
CreateShader.restype = c_void_p

ShadeSurface=openb3d.ShadeSurface
ShadeSurface.argtypes = [c_void_p, c_void_p]

ShadeMesh=openb3d.ShadeMesh
ShadeMesh.argtypes = [c_void_p, c_void_p]

ShadeEntity=openb3d.ShadeEntity
ShadeEntity.argtypes = [c_void_p, c_void_p]

ShaderTexture=openb3d.ShaderTexture
ShaderTexture.argtypes = [c_void_p, c_void_p, c_char_p, c_int]

SetFloat=openb3d.SetFloat
SetFloat.argtypes = [c_void_p, c_char_p, c_float]

SetFloat2=openb3d.SetFloat2
SetFloat2.argtypes = [c_void_p, c_char_p, c_float, c_float]

SetFloat3=openb3d.SetFloat3
SetFloat3.argtypes = [c_void_p, c_char_p, c_float, c_float, c_float]

SetFloat4=openb3d.SetFloat4
SetFloat4.argtypes = [c_void_p, c_char_p, c_float, c_float, c_float, c_float]

SetInteger=openb3d.SetInteger
SetInteger.argtypes = [c_void_p, c_char_p, c_int]

SetInteger2=openb3d.SetInteger2
SetInteger2.argtypes = [c_void_p, c_char_p, c_int, c_int]

SetInteger3=openb3d.SetInteger3
SetInteger3.argtypes = [c_void_p, c_char_p, c_int, c_int, c_int]

SetInteger4=openb3d.SetInteger4
SetInteger4.argtypes = [c_void_p, c_char_p, c_int, c_int, c_int, c_int]

UseSurface=openb3d.UseSurface
UseSurface.argtypes = [c_void_p, c_char_p, c_void_p, c_int]

UseMatrix=openb3d.UseMatrix
UseMatrix.argtypes = [c_void_p, c_char_p, c_int]

LoadMaterial=openb3d.LoadMaterial
LoadMaterial.argtypes = [c_char_p, c_int, c_int, c_int, c_int, c_int]
LoadMaterial.restype = c_void_p

ShaderMaterial=openb3d.ShaderMaterial
ShaderMaterial.argtypes = [c_void_p, c_void_p, c_char_p, c_int]

AmbientShader=openb3d.AmbientShader
AmbientShader.argtypes = [c_void_p]

CreateOcTree=openb3d.CreateOcTree
CreateOcTree.argtypes = [c_float, c_float, c_float, c_void_p]
CreateOcTree.restype = c_void_p

OctreeBlock=openb3d.OctreeBlock
OctreeBlock.argtypes = [c_void_p, c_void_p, c_int, c_float, c_float, c_float, c_float, c_float]

OctreeMesh=openb3d.OctreeMesh
OctreeMesh.argtypes = [c_void_p, c_void_p, c_int, c_float, c_float, c_float, c_float, c_float]

CreateParticleEmitter=openb3d.CreateParticleEmitter
CreateParticleEmitter.argtypes = [c_void_p, c_void_p]
CreateParticleEmitter.restype = c_void_p

ActMoveBy=openb3d.ActMoveBy
ActMoveBy.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
ActMoveBy.restype = c_void_p

ActTurnBy=openb3d.ActTurnBy
ActTurnBy.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
ActTurnBy.restype = c_void_p

ActVector=openb3d.ActVector
ActVector.argtypes = [c_void_p, c_float, c_float, c_float]
ActVector.restype = c_void_p

ActMoveTo=openb3d.ActMoveTo
ActMoveTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
ActMoveTo.restype = c_void_p

ActTurnTo=openb3d.ActTurnTo
ActTurnTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
ActTurnTo.restype = c_void_p

ActScaleTo=openb3d.ActScaleTo
ActScaleTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
ActScaleTo.restype = c_void_p

ActFadeTo=openb3d.ActFadeTo
ActFadeTo.argtypes = [c_void_p, c_float, c_float]
ActFadeTo.restype = c_void_p

ActTintTo=openb3d.ActTintTo
ActTintTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
ActTintTo.restype = c_void_p

ActTrackByPoint=openb3d.ActTrackByPoint
ActTrackByPoint.argtypes = [c_void_p, c_void_p, c_float, c_float, c_float, c_float]
ActTrackByPoint.restype = c_void_p

ActTrackByDistance=openb3d.ActTrackByDistance
ActTrackByDistance.argtypes = [c_void_p, c_void_p, c_float, c_float]
ActTrackByDistance.restype = c_void_p

ActNewtonian=openb3d.ActNewtonian
ActNewtonian.argtypes = [c_void_p, c_float]
ActNewtonian.restype = c_void_p

AppendAction=openb3d.AppendAction
AppendAction.argtypes = [c_void_p, c_void_p]

FreeAction=openb3d.FreeAction
FreeAction.argtypes = [c_void_p]

Flip=sdl.SDL_GL_SwapBuffers

