from ctypes import *
sdl=cdll.LoadLibrary("libSDL-1.2.so.0")
openb3d=cdll.LoadLibrary("./libOpenB3D.so")

def Graphics3D(w,h,d=0,m=0):
	sdl.SDL_Init(65535)
	sdl.SDL_GL_SetAttribute(7,1)
	sdl.SDL_SetVideoMode(w,h,d,2)
	openb3d.Graphics3D(w,h,d,m)

openb3d.AddAnimSeq.argtypes = [c_void_p, c_int]
openb3d.AddAnimSeq.restype = c_int
def AddAnimSeq(ent, length):
	return openb3d.AddAnimSeq(ent, length)

openb3d.AddMesh.argtypes = [c_void_p, c_void_p]
def AddMesh(mesh1,mesh2):
	openb3d.AddMesh(mesh1,mesh2)

openb3d.AddTriangle.argtypes = [c_void_p, c_int, c_int, c_int]
openb3d.AddTriangle.restype = c_int
def AddTriangle(surf, v0, v1, v2):
	return openb3d.AddTriangle(surf, v0, v1, v2)

openb3d.AddVertex.argtypes = [c_void_p, c_float, c_float, c_float, c_float, c_float, c_float]
openb3d.AddVertex.restype = c_int
def AddVertex(surf, x, y, z, u, v, w):
	return openb3d.AddVertex(surf, x, y, z, u, v, w)

openb3d.AmbientLight.argtypes = [c_float, c_float, c_float]
def AmbientLight(r, g, b):
	openb3d.AmbientLight(r, g, b)

Animate=openb3d.Animate
openb3d.Animate.argtypes = [c_void_p, c_int, c_float, c_int, c_int]
def Animate(ent, mode=1, speed=1, seq=0, trans=0):
	openb3d.Animate(ent, mode, speed, seq, trans)

openb3d.Animating.argtypes = [c_void_p]
openb3d.Animating.restype = c_int
def Animating(ent):
	return openb3d.Animating(ent)

openb3d.AnimLength.argtypes = [c_void_p]
openb3d.AnimLength.restype = c_int
def AnimLength(ent):
	return openb3d.AnimLength(ent)

openb3d.AnimSeq.argtypes = [c_void_p]
openb3d.AnimSeq.restype = c_int
def AnimSeq(ent):
	return openb3d.AnimSeq(ent)

openb3d.AnimTime.argtypes = [c_void_p]
openb3d.AnimTime.restype = c_float
def AnimTime(ent):
	return openb3d.AnimTime(ent)

openb3d.BackBufferToTex.argtypes = [c_void_p, c_int]
def BackBufferToTex(tex,frame=0):
	openb3d.BackBufferToTex(tex, frame)

openb3d.BrushAlpha.argtypes = [c_void_p, c_float]
def BrushAlpha(brush,a):
	openb3d.BrushAlpha(brush,a)

openb3d.BrushBlend.argtypes = [c_void_p, c_int]
def BrushBlend(brush,blend):
	openb3d.BrushBlend(brush,blend)

openb3d.BrushColor.argtypes = [c_void_p, c_float, c_float, c_float]
def BrushColor(brush,r,g,b):
	openb3d.BrushColor(brush,r,g,b)

openb3d.BrushFX.argtypes = [c_void_p, c_int]
def BrushFX(brush,fx):
	openb3d.BrushFX(brush,fx)

openb3d.BrushShininess.argtypes = [c_void_p, c_float]
def BrushShininess(brush,s):
	openb3d.BrushShininess(brush,s)

openb3d.BrushTexture.argtypes = [c_void_p, c_void_p, c_int, c_int]
def BrushTexture(brush,tex, frame=0, index=0):
	openb3d.BrushTexture(brush, tex, frame, index)

openb3d.CameraClsColor.argtypes = [c_void_p, c_float, c_float, c_float]
def CameraClsColor(cam,r,g,b):
	openb3d.CameraClsColor(cam,r,g,b)

openb3d.CameraClsMode.argtypes = [c_void_p, c_int, c_int]
def CameraClsMode(cam,cls_depth, cls_zbuffer):
	openb3d.CameraClsMode(cam,cls_depth, cls_zbuffer)

openb3d.CameraFogColor.argtypes = [c_void_p, c_float, c_float, c_float]
def CameraFogColor(cam,r,g,b):
	openb3d.CameraFogColor(cam,r,g,b)

openb3d.CameraFogMode.argtypes = [c_void_p, c_int]
def CameraFogMode(cam,mode):
	openb3d.CameraFogMode(cam,mode)

openb3d.CameraFogRange.argtypes = [c_void_p, c_float, c_float]
def CameraFogRange(cam, nnear, nfar):
	openb3d.CameraFogRange(cam, nnear, nfar)

openb3d.CameraPick.argtypes = [c_void_p, c_float, c_float]
openb3d.CameraPick.restype = c_void_p
def CameraPick(cam, x, y):
	return openb3d.CameraPick(cam, x, y)

openb3d.CameraProject.argtypes = [c_void_p, c_float, c_float, c_float]
def CameraProject(cam, x, y, z):
	openb3d.CameraProject(cam, x, y, z)

openb3d.CameraProjMode.argtypes = [c_void_p, c_int]
def CameraProjMode(cam,mode):
	openb3d.CameraProjMode(cam,mode)

openb3d.CameraToTex.argtypes = [c_void_p, c_void_p, c_int]
def CameraToTex(tex, cam, frame=0):
	openb3d.CameraToTex(tex, cam, frame=0)

openb3d.CameraRange.argtypes = [c_void_p, c_float, c_float]
def CameraRange(cam, nnear, nfar):
	openb3d.CameraRange(cam, nnear, nfar)

openb3d.CameraViewport.argtypes = [c_void_p, c_int, c_int, c_int, c_int]
def CameraViewport(cam, x, y, width, height):
	openb3d.CameraViewport(cam, x, y, width, height)

openb3d.CameraZoom.argtypes = [c_void_p, c_float]
def CameraZoom(cam, zoom):
	openb3d.CameraZoom(cam, zoom)

def ClearCollisions():
	openb3d.ClearCollisions()

openb3d.ClearSurface.argtypes = [c_void_p, c_bool, c_bool]
def ClearSurface(surf, clear_verts=1, clear_tris=1):
	openb3d.ClearSurface(surf, clear_verts, clear_tris)

def ClearTextureFilters():
	openb3d.ClearTextureFilters()

openb3d.ClearWorld.argtypes = [c_bool, c_bool, c_bool]
def ClearWorld(entities=1, brushes=1, textures=1):
	openb3d.ClearWorld(entities, brushes, textures)

openb3d.CollisionEntity.argtypes = [c_void_p, c_int]
openb3d.CollisionEntity.restype = c_void_p
def CollisionEntity(ent, index):
	return openb3d.CollisionEntity(ent, index)

openb3d.Collisions.argtypes = [c_int, c_int, c_int, c_int]
def Collisions(src_no, dest_no, method_no, response_no=0):
	openb3d.Collisions(src_no, dest_no, method_no, response_no)

openb3d.CollisionNX.argtypes = [c_void_p, c_int]
openb3d.CollisionNX.restype = c_float
def CollisionNX(ent, index):
	return openb3d.CollisionNX(ent, index)

openb3d.CollisionNY.argtypes = [c_void_p, c_int]
openb3d.CollisionNY.restype = c_float
def CollisionNY(ent, index):
	return openb3d.CollisionNY(ent, index)

openb3d.CollisionNZ.argtypes = [c_void_p, c_int]
openb3d.CollisionNZ.restype = c_float
def CollisionNZ(ent, index):
	return openb3d.CollisionNZ(ent, index)

openb3d.CollisionSurface.argtypes = [c_void_p, c_int]
openb3d.CollisionSurface.restype = c_void_p
def CollisionSurface(ent, index):
	return openb3d.CollisionSurface(ent, index)

openb3d.CollisionTime.argtypes = [c_void_p, c_int]
openb3d.CollisionTime.restype = c_float
def CollisionTime(ent, index):
	return openb3d.CollisionTime(ent, index)

openb3d.CollisionTriangle.argtypes = [c_void_p, c_int]
openb3d.CollisionTriangle.restype = c_int
def CollisionTriangle(ent, index):
	return openb3d.CollisionTriangle(ent, index)

openb3d.CollisionX.argtypes = [c_void_p, c_int]
openb3d.CollisionX.restype = c_float
def CollisionX(ent, index):
	return openb3d.CollisionX(ent, index)

openb3d.CollisionY.argtypes = [c_void_p, c_int]
openb3d.CollisionY.restype = c_float
def CollisionY(ent, index):
	return openb3d.CollisionY(ent, index)

openb3d.CollisionZ.argtypes = [c_void_p, c_int]
openb3d.CollisionZ.restype = c_float
def CollisionZ(ent, index):
	return openb3d.CollisionZ(ent, index)

openb3d.CountChildren.argtypes = [c_void_p]
openb3d.CountChildren.restype = c_int
def CountChildren(ent):
	return openb3d.CountChildren(ent)

openb3d.CountCollisions.argtypes = [c_void_p]
openb3d.CountCollisions.restype = c_int
def CountCollisions(ent):
	return openb3d.CountCollisions(ent)

openb3d.CopyEntity.argtypes = [c_void_p, c_void_p]
openb3d.CopyEntity.restype = c_void_p
def CopyEntity(ent, parent=0):
	return openb3d.CopyEntity(ent, parent)


openb3d.CopyMesh.argtypes = [c_void_p, c_void_p]
openb3d.CopyMesh.restype = c_void_p
def CopyMesh(ent, parent=0):
	return openb3d.CopyMesh(ent, parent)

openb3d.CountSurfaces.argtypes = [c_void_p]
openb3d.CountSurfaces.restype = c_int
def CountSurfaces(mesh):
	return openb3d.CountSurfaces(mesh)

openb3d.CountTriangles.argtypes = [c_void_p]
openb3d.CountTriangles.restype = c_int
def CountTriangles(surf):
	return openb3d.CountTriangles(surf)

openb3d.CountVertices.argtypes = [c_void_p]
openb3d.CountVertices.restype = c_int
def CountVertices(surf):
	return openb3d.CountVertices(surf)

openb3d.CreateBlob.argtypes = [c_void_p, c_float, c_void_p]
openb3d.CreateBlob.restype = c_void_p
def CreateBlob(fluid, radius, parent=0):
	return openb3d.CreateBlob(fluid, radius, parent)

openb3d.CreateBone.argtypes = [c_void_p, c_void_p]
openb3d.CreateBone.restype = c_void_p
def CreateBone(mesh, parent=0):
	return openb3d.CreateBone(mesh, parent)

openb3d.CreateBrush.argtypes = [c_float, c_float, c_float]
openb3d.CreateBrush.restype = c_void_p
def CreateBrush(r=255, g=255, b=255):
	return openb3d.CreateBrush(r, g, b)

openb3d.CreateCamera.argtypes = [c_void_p]
openb3d.CreateCamera.restype = c_void_p
def CreateCamera(parent=0):
	return openb3d.CreateCamera(parent)

openb3d.CreateConstraint.argtypes = [c_void_p, c_void_p, c_float]
openb3d.CreateConstraint.restype = c_void_p
def CreateConstraint(p1, p2, l):
	return openb3d.CreateConstraint(p1, p2, l)

openb3d.CreateCone.argtypes = [c_int, c_bool, c_void_p]
openb3d.CreateCone.restype = c_void_p
def CreateCone(segments=8, solid=1, parent=0):
	return openb3d.CreateCone(segments, solid, parent)

openb3d.CreateCylinder.argtypes = [c_int, c_bool, c_void_p]
openb3d.CreateCylinder.restype = c_void_p
def CreateCylinder(segments=8, solid=1, parent=0):
	return openb3d.CreateCylinder(segments, solid, parent)

openb3d.CreateCube.argtypes = [c_void_p]
openb3d.CreateCube.restype = c_void_p
def CreateCube(parent=0):
	return openb3d.CreateCube(parent)

openb3d.CreateFluid.restype = c_void_p
def CreateFluid():
	return openb3d.CreateFluid()

openb3d.CreateGeosphere.argtypes = [c_int, c_void_p]
openb3d.CreateGeosphere.restype = c_void_p
def CreateGeosphere(size, parent=0):
	return openb3d.CreateGeosphere(size, parent)

openb3d.CreateMesh.argtypes = [c_void_p]
openb3d.CreateMesh.restype = c_void_p
def CreateMesh(parent=0):
	return openb3d.CreateMesh(parent)

openb3d.CreateLight.argtypes = [c_int, c_void_p]
openb3d.CreateLight.restype = c_void_p
def CreateLight(light=1, parent=0):
	return openb3d.CreateLight(light, parent)

openb3d.CreatePivot.argtypes = [c_void_p]
openb3d.CreatePivot.restype = c_void_p
def CreatePivot(parent=0):
	return openb3d.CreatePivot(parent)

openb3d.CreatePlane.argtypes = [c_int, c_void_p]
openb3d.CreatePlane.restype = c_void_p
def CreatePlane(divisions=1, parent=0):
	return openb3d.CreatePlane(divisions, parent)

openb3d.CreateQuad.argtypes = [c_void_p]
openb3d.CreateQuad.restype = c_void_p
def CreateQuad(parent=0):
	return openb3d.CreateQuad(parent)

openb3d.CreateRigidBody.argtypes = [c_void_p, c_void_p, c_void_p, c_void_p, c_void_p]
openb3d.CreateRigidBody.restype = c_void_p
def CreateRigidBody(body, p1, p2, p3, p4):
	return openb3d.CreateRigidBody(body, p1, p2, p3, p4)

openb3d.CreateShadow.argtypes = [c_void_p, c_char]
openb3d.CreateShadow.restype = c_void_p
def CreateShadow(parent, static=0):
	return openb3d.CreateShadow(parent, static)

openb3d.CreateSphere.argtypes = [c_int, c_void_p]
openb3d.CreateSphere.restype = c_void_p
def CreateSphere(segments=8, parent=0):
	return openb3d.CreateSphere(segments, parent)

openb3d.CreateSprite.argtypes = [c_void_p]
openb3d.CreateSprite.restype = c_void_p
def CreateSprite(parent=0):
	return openb3d.CreateSprite(parent)

openb3d.CreateSurface.argtypes = [c_void_p, c_void_p]
openb3d.CreateSurface.restype = c_void_p
def CreateSurface(mesh, brush=0):
	return openb3d.CreateSurface(mesh, brush)

openb3d.CreateStencil.restype = c_void_p
def CreateStencil():
	return openb3d.CreateStencil()

openb3d.CreateTerrain.argtypes = [c_int, c_void_p]
openb3d.CreateTerrain.restype = c_void_p
def CreateTerrain(size, parent=0):
	return openb3d.CreateTerrain(size, parent)

openb3d.CreateTexture.argtypes = [c_int, c_int, c_int, c_int]
openb3d.CreateTexture.restype = c_void_p
def CreateTexture(width, height, flags=1,frames=1):
	return openb3d.CreateTexture(width, height, flags, frames)

openb3d.CreateVoxelSprite.argtypes = [c_int, c_void_p]
openb3d.CreateVoxelSprite.restype = c_void_p
def CreateVoxelSprite(slices=64, parent=0):
	return openb3d.CreateVoxelSprite(slices, parent)

openb3d.DeltaPitch.argtypes = [c_void_p, c_void_p]
openb3d.DeltaPitch.restype = c_float
def DeltaPitch(ent1, ent2):
	return openb3d.DeltaPitch(ent1, ent2)

openb3d.DeltaYaw.argtypes = [c_void_p, c_void_p]
openb3d.DeltaYaw.restype = c_float
def DeltaYaw(ent1, ent2):
	return openb3d.DeltaYaw(ent1, ent2)

openb3d.DepthBufferToTex.argtypes = [c_void_p, c_void_p]
def DepthBufferToTex(tex, cam=0):
	openb3d.DepthBufferToTex(tex, cam)

openb3d.EmitterVector.argtypes = [c_void_p, c_float, c_float, c_float]
def EmitterVector(emit, x, y, z):
	openb3d.EmitterVector(emit, x, y, z)

openb3d.EmitterRate.argtypes = [c_void_p, c_float]
def EmitterRate(emit, r):
	openb3d.EmitterRate(emit, r)

openb3d.EmitterParticleLife.argtypes = [c_void_p, c_int]
def EmitterParticleLife(emit, l):
	openb3d.EmitterParticleLife(emit, l)

openb3d.EmitterParticleSpeed.argtypes = [c_void_p, c_float]
def EmitterParticleSpeed(emit, s):
	openb3d.EmitterParticleSpeed(emit, s)

openb3d.EmitterVariance.argtypes = [c_void_p, c_float]
def EmitterVariance(emit, v):
	openb3d.EmitterVariance(emit, v)

openb3d.EntityAlpha.argtypes = [c_void_p, c_float]
def EntityAlpha(ent, alpha):
	openb3d.EntityAlpha(ent, alpha)

openb3d.EntityBlend.argtypes = [c_void_p, c_int]
def EntityBlend(ent, blend):
	openb3d.EntityBlend(ent, blend)

openb3d.EntityBox.argtypes = [c_void_p, c_float, c_float, c_float, c_float, c_float, c_float]
def EntityBox(ent, x, y, z, w, h, d):
	openb3d.EntityBox(ent, x, y, z, w, h, d)

openb3d.EntityClass.argtypes = [c_void_p]
openb3d.EntityClass.restype = c_char_p
def EntityClass(ent):
	return openb3d.EntityClass(ent)

openb3d.EntityCollided.argtypes = [c_void_p, c_int]
openb3d.EntityCollided.restype = c_void_p
def EntityCollided(ent, type_no):
	return openb3d.EntityCollided(ent, type_no)

openb3d.EntityColor.argtypes = [c_void_p, c_float, c_float, c_float]
def EntityColor(ent, red, green, blue):
	openb3d.EntityColor(ent, red, green, blue)

openb3d.EntityDistance.argtypes = [c_void_p, c_void_p]
openb3d.EntityDistance.restype = c_float
def EntityDistance(ent1, ent2):
	return openb3d.EntityDistance(ent1, ent2)

openb3d.EntityFX.argtypes = [c_void_p, c_int]
def EntityFX(ent, fx):
	openb3d.EntityFX(ent, fx)

openb3d.EntityInView.argtypes = [c_void_p, c_void_p]
openb3d.EntityInView.restype = c_int
def EntityInView(ent, cam):
	return openb3d.EntityInView(ent, cam)

openb3d.EntityName.argtypes = [c_void_p]
openb3d.EntityName.restype = c_char_p
def EntityName(ent):
	return openb3d.EntityName(ent)

openb3d.EntityOrder.argtypes = [c_void_p, c_int]
def EntityOrder(ent, order):
	openb3d.EntityOrder(ent, order)

openb3d.EntityParent.argtypes = [c_void_p, c_void_p, c_bool]
def EntityParent(ent, parent, glob=1):
	openb3d.EntityParent(ent, parent, glob)

openb3d.EntityPick.argtypes = [c_void_p, c_float]
openb3d.EntityPick.restype = c_void_p
def EntityPick(ent, range):
	return openb3d.EntityPick(ent. range)

openb3d.EntityPickMode.argtypes = [c_void_p, c_int, c_bool]
def EntityPickMode(ent, pick_mode, obscurer=1):
	openb3d.EntityPickMode(ent, pick_mode, obscurer)

openb3d.EntityPitch.argtypes = [c_void_p, c_bool]
openb3d.EntityPitch.restype = c_float
def EntityPitch(ent, glob=0):
	return openb3d.EntityPitch(ent, glob)

openb3d.EntityRadius.argtypes = [c_void_p, c_float, c_float]
def EntityRadius(ent, radius_x, radius_y=0):
	openb3d.EntityRadius(ent, radius_x, radius_y)

openb3d.EntityRoll.argtypes = [c_void_p, c_bool]
openb3d.EntityRoll.restype = c_float
def EntityRoll(ent, glob=0):
	return openb3d.EntityRoll(ent, glob)

openb3d.EntityShininess.argtypes = [c_void_p, c_float]
def EntityShininess(ent, shine):
	openb3d.EntityShininess(ent, shine)

openb3d.EntityTexture.argtypes = [c_void_p, c_void_p, c_int, c_int]
def EntityTexture(ent, tex, frame=0, index=0):
	openb3d.EntityTexture(ent, tex, frame, index)

openb3d.EntityType.argtypes = [c_void_p, c_int, c_bool]
def EntityType(ent, type_no, recursive=0):
	openb3d.EntityTexture(ent, type_no, recursive)

openb3d.EntityVisible.argtypes = [c_void_p, c_void_p]
openb3d.EntityVisible.restype = c_int
def EntityVisible(src_ent, dest_ent):
	return openb3d.EntityVisible(src_ent, dest_ent)

openb3d.EntityX.argtypes = [c_void_p, c_bool]
openb3d.EntityX.restype = c_float
def EntityX(ent, glob=0):
	return openb3d.EntityX(ent, glob)

openb3d.EntityY.argtypes = [c_void_p, c_bool]
openb3d.EntityY.restype = c_float
def EntityY(ent, glob=0):
	return openb3d.EntityY(ent, glob)

openb3d.EntityYaw.argtypes = [c_void_p, c_bool]
openb3d.EntityYaw.restype = c_float
def EntityYaw(ent, glob=0):
	return openb3d.EntityYaw(ent, glob)

openb3d.EntityZ.argtypes = [c_void_p, c_bool]
openb3d.EntityZ.restype = c_float
def EntityZ(ent, glob=0):
	return openb3d.EntityZ(ent, glob)

openb3d.ExtractAnimSeq.argtypes = [c_void_p, c_int, c_int, c_int]
openb3d.ExtractAnimSeq.restype = c_int
def EntityZ(ent, first_frame , last_frame, seq=0):
	return openb3d.EntityZ(ent, first_frame , last_frame, seq)

openb3d.FindChild.argtypes = [c_void_p, c_char_p]
openb3d.FindChild.restype = c_void_p
def FindChild(ent, child_name):
	return openb3d.FindChild(ent, child_name)

openb3d.FitMesh.argtypes = [c_void_p, c_float, c_float, c_float, c_float, c_float, c_float, c_bool]
def FitMesh(mesh , x, y, z, width, height, depth, uniform=0):
	openb3d.FitMesh(mesh , x, y, z, width, height, depth, uniform)

openb3d.FlipMesh.argtypes = [c_void_p]
def FlipMesh(mesh):
	openb3d.FlipMesh(mesh)

openb3d.FluidThreshold.argtypes = [c_void_p, c_float]
def FluidThreshold(fluid, threshold):
	openb3d.FluidThreshold(fluid, threshold)

openb3d.FreeBrush.argtypes = [c_void_p]
def FreeBrush(brush):
	openb3d.FreeBrush(brush)

openb3d.FreeConstraint.argtypes = [c_void_p]
def FreeConstraint(con):
	openb3d.FreeConstraint(con)

openb3d.FreeEntity.argtypes = [c_void_p]
def FreeEntity(ent):
	openb3d.FreeEntity(ent)

openb3d.FreeRigidBody.argtypes = [c_void_p]
def FreeRigidBody(body):
	openb3d.FreeRigidBody(body)

openb3d.FreeShader.argtypes = [c_void_p]
def FreeShader(shader):
	openb3d.FreeShader(shader)

openb3d.FreeShadow.argtypes = [c_void_p]
def FreeShadow(shadow):
	openb3d.FreeShadow(shadow)

openb3d.FreeTexture.argtypes = [c_void_p]
def FreeTexture(tex):
	openb3d.FreeTexture(tex)

openb3d.GeosphereHeight.argtypes = [c_void_p, c_float]
def GeosphereHeight(geo, h):
	openb3d.GeosphereHeight(geo, h)

openb3d.GetBrushTexture.argtypes = [c_void_p, c_int]
openb3d.GetBrushTexture.restype = c_void_p
def GetBrushTexture(brush, index=0):
	return openb3d.GetBrushTexture(brush, index)

openb3d.GetChild.argtypes = [c_void_p, c_int]
openb3d.GetChild.restype = c_void_p
def GetChild(ent, child_no):
	return openb3d.GetChild(ent, child_no)

openb3d.GetEntityBrush.argtypes = [c_void_p]
openb3d.GetEntityBrush.restype = c_void_p
def GetEntityBrush(ent):
	return openb3d.GetEntityBrush(ent)

openb3d.GetEntityType.argtypes = [c_void_p]
openb3d.GetEntityType.restype = c_int
def GetEntityType(ent):
	return openb3d.GetEntityType(ent)

openb3d.GetParentEntity.argtypes = [c_void_p]
openb3d.GetParentEntity.restype = c_void_p
def GetParentEntity(ent):
	return openb3d.GetParentEntity(ent)

openb3d.GetSurface.argtypes = [c_void_p, c_int]
openb3d.GetSurface.restype = c_void_p
def GetSurface(mesh, surf_no):
	return openb3d.GetSurface(mesh, surf_no)

openb3d.GetSurfaceBrush.argtypes = [c_void_p]
openb3d.GetSurfaceBrush.restype = c_void_p
def GetSurfaceBrush(surf):
	return openb3d.GetSurfaceBrush(surf)

openb3d.HandleSprite.argtypes = [c_void_p, c_float, c_float]
def HandleSprite(sprite, h_x, h_y):
	openb3d.HandleSprite(sprite, h_x, h_y)

openb3d.HideEntity.argtypes = [c_void_p]
def HideEntity(ent):
	openb3d.HideEntity(ent)

openb3d.LightColor.argtypes = [c_void_p, c_float, c_float, c_float]
def LightColor(light, red, green, blue):
	openb3d.LightColor(light, red, green, blue)

openb3d.LightConeAngles.argtypes = [c_void_p, c_float, c_float]
def LightConeAngles(light, inner_ang, outer_ang):
	openb3d.LightConeAngles(light, inner_ang, outer_ang)

openb3d.LightRange.argtypes = [c_void_p, c_float]
def LightRange(light, range):
	openb3d.LightRange(light, range)

openb3d.LinePick.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float, c_float]
openb3d.LinePick.restype = c_void_p
def LinePick(x, y, z, dx, dy, dz, radius=0):
	return openb3d.LinePick(x, y, z, dx, dy, dz, radius)

openb3d.LoadAnimMesh.argtypes = [c_char_p, c_void_p]
openb3d.LoadAnimMesh.restype = c_void_p
def LoadAnimMesh(file, parent=0):
	return openb3d.LoadAnimMesh(file, parent)

openb3d.LoadAnimSeq.argtypes = [c_void_p, c_char_p]
openb3d.LoadAnimSeq.restype = c_int
def LoadAnimSeq(ent, name):
	return openb3d.LoadAnimSeq(ent, name)

openb3d.LoadAnimTexture.argtypes = [c_char_p, c_int, c_int, c_int, c_int, c_int]
openb3d.LoadAnimTexture.restype = c_void_p
def LoadAnimTexture(file, flags, frame_width, frame_height, first_frame, frame_count):
	return openb3d.LoadAnimTexture(file, flags, frame_width, frame_height, first_frame, frame_count)

openb3d.LoadBrush.argtypes = [c_char_p, c_int, c_float, c_float]
openb3d.LoadBrush.restype = c_void_p
def LoadBrush(file, flags=1, u_scale=1, v_scale=1):
	return openb3d.LoadBrush(file,flags,u_scale,v_scale)

openb3d.LoadGeosphere.argtypes = [c_char_p, c_void_p]
openb3d.LoadGeosphere.restype = c_void_p
def LoadGeosphere(file, parent=0):
	return openb3d.LoadGeosphere(file, parent)

openb3d.LoadMesh.argtypes = [c_char_p, c_void_p]
openb3d.LoadMesh.restype = c_void_p
def LoadMesh(file, parent=0):
	return openb3d.LoadMesh(file, parent)

openb3d.LoadTerrain.argtypes = [c_char_p, c_void_p]
openb3d.LoadTerrain.restype = c_void_p
def LoadTerrain(file, parent=0):
	return openb3d.LoadTerrain(file, parent)

openb3d.LoadTexture.argtypes = [c_char_p, c_int]
openb3d.LoadTexture.restype = c_void_p
def LoadTexture(file, flags=1):
	return openb3d.LoadTexture(file, flags)

openb3d.LoadSprite.argtypes = [c_char_p, c_int, c_void_p]
openb3d.LoadSprite.restype = c_void_p
def LoadSprite(file, tex_flags=1, parent=0):
	return openb3d.LoadSprite(file, tex_flags, parent)

openb3d.MeshCSG.argtypes = [c_void_p, c_void_p, c_int]
openb3d.MeshCSG.restype = c_void_p
def MeshCSG(m1, m2, method=1):
	return openb3d.MeshCSG(m1, m2, method=1)

openb3d.MeshCullRadius.argtypes = [c_void_p, c_float]
def MeshCullRadius(ent, radius):
	openb3d.MeshCullRadius(ent, radius)

openb3d.MeshDepth.argtypes = [c_void_p]
openb3d.MeshDepth.restype = c_float
def MeshDepth(mesh):
	return openb3d.MeshDepth(mesh)

openb3d.MeshesIntersect.argtypes = [c_void_p, c_void_p]
openb3d.MeshesIntersect.restype = c_int
def MeshesIntersect(mesh1, mesh2):
	return openb3d.MeshesIntersect(mesh1, mesh2)

openb3d.MeshHeight.argtypes = [c_void_p]
openb3d.MeshHeight.restype = c_float
def MeshHeight(mesh):
	return openb3d.MeshHeight(mesh)

openb3d.MeshWidth.argtypes = [c_void_p]
openb3d.MeshWidth.restype = c_float
def MeshWidth(mesh):
	return openb3d.MeshWidth(mesh)

openb3d.ModifyGeosphere.argtypes = [c_void_p, c_int, c_int, c_float]
def ModifyGeosphere(geo, x, z, height):
	openb3d.ModifyGeosphere(geo, x, z, height)

openb3d.ModifyTerrain.argtypes = [c_void_p, c_int, c_int, c_float]
def ModifyTerrain(terr, x, z, height):
	openb3d.ModifyTerrain(terr, x, z, height)

openb3d.MoveEntity.argtypes = [c_void_p, c_float, c_float, c_float]
def MoveEntity(ent, x, y, z):
	openb3d.MoveEntity(ent, x, y, z)

openb3d.NameEntity.argtypes = [c_void_p, c_char_p]
def NameEntity(ent, name):
	openb3d.NameEntity(ent, name)

openb3d.PaintEntity.argtypes = [c_void_p, c_void_p]
def PaintEntity(ent, brush):
	openb3d.PaintEntity(ent, brush)

openb3d.PaintMesh.argtypes = [c_void_p, c_void_p]
def PaintMesh(mesh, brush):
	openb3d.PaintMesh(mesh, brush)

openb3d.PaintSurface.argtypes = [c_void_p, c_void_p]
def PaintSurface(surf, brush):
	openb3d.PaintSurface(surf, brush)

openb3d.ParticleColor.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
def ParticleColor(sprite, r, g, b, a=0):
	openb3d.ParticleColor(sprite, r, g, b, a)

openb3d.ParticleVector.argtypes = [c_void_p, c_float, c_float, c_float]
def ParticleVector(sprite, x, y, z):
	openb3d.ParticleVector(sprite, x, y, z)

openb3d.ParticleTrail.argtypes = [c_void_p, c_int]
def ParticleTrail(sprite, length):
	openb3d.ParticleTrail(sprite, length)

openb3d.PickedEntity.restype = c_void_p
def PickedEntity():
	return openb3d.PickedEntity()

openb3d.PickedNX.restype = c_float
def PickedNX():
	return openb3d.PickedNX()

openb3d.PickedNY.restype = c_float
def PickedNY():
	return openb3d.PickedNY()

openb3d.PickedNZ.restype = c_float
def PickedNZ():
	return openb3d.PickedNZ()

openb3d.PickedSurface.restype = c_void_p
def PickedSurface():
	return openb3d.PickedSurface()

openb3d.PickedTime.restype = c_float
def PickedTime():
	return openb3d.PickedTime()

openb3d.PickedTriangle.restype = c_int
def PickedTriangle():
	return openb3d.PickedTriangle()

openb3d.PickedX.restype = c_float
def PickedX():
	return openb3d.PickedX()

openb3d.PickedY.restype = c_float
def PickedY():
	return openb3d.PickedY()

openb3d.PickedZ.restype = c_float
def PickedZ():
	return openb3d.PickedZ()

openb3d.PointEntity.argtypes = [c_void_p, c_void_p, c_float]
def PointEntity(ent, target, roll=0):
	openb3d.PointEntity(ent, target, roll)

openb3d.PositionEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]
def PositionEntity(ent, x, y, z, glob=0):
	openb3d.PositionEntity(ent, x, y, z, glob)

openb3d.PositionMesh.argtypes = [c_void_p, c_float, c_float, c_float]
def PositionMesh(mesh, px, py, pz):
	openb3d.PositionMesh(mesh, px, py, pz)

openb3d.PositionTexture.argtypes = [c_void_p, c_float, c_float]
def PositionTexture(tex, u_pos, v_pos):
	openb3d.PositionTexture(tex, u_pos, v_pos)

openb3d.ProjectedX.restype = c_float
def ProjectedX():
	return openb3d.ProjectedX()

openb3d.ProjectedY.restype = c_float
def ProjectedY():
	return openb3d.ProjectedY()

openb3d.ProjectedZ.restype = c_float
def ProjectedZ():
	return openb3d.ProjectedZ()

def RenderWorld():
	openb3d.RenderWorld()

openb3d.RepeatMesh.argtypes = [c_void_p, c_void_p]
openb3d.RepeatMesh.restype = c_void_p
def RepeatMesh(mesh, parent=0):
	return openb3d.RepeatMesh(mesh, parent=0)

openb3d.ResetEntity.argtypes = [c_void_p]
def ResetEntity(ent):
	openb3d.ResetEntity(ent)

openb3d.ResetShadow.argtypes = [c_void_p]
def ResetShadow(s):
	openb3d.ResetShadow(s)

openb3d.RotateEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]
def RotateEntity(ent, x, y, z, glob=0):
	openb3d.RotateEntity(ent, x, y, z, glob)

openb3d.RotateMesh.argtypes = [c_void_p, c_float, c_float, c_float]
def RotateMesh(mesh, pitch, yaw, roll):
	openb3d.RotateMesh(mesh, pitch, yaw, roll)

openb3d.RotateSprite.argtypes = [c_void_p, c_float]
def RotateSprite(sprite, ang):
	openb3d.RotateSprite(sprite, ang)

openb3d.RotateTexture.argtypes = [c_void_p, c_float]
def RotateTexture(tex, ang):
	openb3d.RotateTexture(tex, ang)

openb3d.ScaleEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]
def ScaleEntity(ent, x, y, z, glob=0):
	openb3d.ScaleEntity(ent, x, y, z, glob)

openb3d.ScaleMesh.argtypes = [c_void_p, c_float, c_float, c_float]
def ScaleMesh(mesh, sx, sy, sz):
	openb3d.ScaleMesh(mesh, sx, sy, sz)

openb3d.ScaleSprite.argtypes = [c_void_p, c_float, c_float]
def ScaleSprite(sprite, sx, sy):
	openb3d.ScaleSprite(sprite, sx, sy)

openb3d.ScaleTexture.argtypes = [c_void_p, c_float, c_float]
def ScaleTexture(tex, sx, sy):
	openb3d.ScaleTexture(tex, sx, sy)

openb3d.SetAnimKey.argtypes = [c_void_p, c_float, c_int, c_int, c_int]
def SetAnimKey(ent, frame , pos_key=1, rot_key=1, scale_key=1):
	openb3d.SetAnimKey(ent, frame , pos_key, rot_key, scale_key)

openb3d.SetAnimTime.argtypes = [c_void_p, c_float, c_int]
def SetAnimTime(ent, time, seq=0):
	openb3d.SetAnimTime(ent, time, seq)

openb3d.SetCubeFace.argtypes = [c_void_p, c_int]
def SetCubeFace(tex, face):
	openb3d.SetCubeFace(tex, face)

openb3d.SetCubeMode.argtypes = [c_void_p, c_int]
def SetCubeMode(tex, mode):
	openb3d.SetCubeMode(tex, mode)

openb3d.ShowEntity.argtypes = [c_void_p]
def ShowEntity(ent):
	openb3d.ShowEntity(ent)

openb3d.SkinMesh.argtypes = [c_void_p, c_int, c_int, c_int, c_float, c_int, c_float, c_int, c_float, c_int, c_float]
def SkinMesh(mesh, surf_no, vid , bone1, weight1=1.0, bone2=0, weight2=0, bone3=0, weight3 =0, bone4=0, weight4=0):
	openb3d.SkinMesh(mesh, surf_no, vid , bone1, weight1, bone2, weight2, bone3, weight3, bone4, weight4)

openb3d.SpriteRenderMode.argtypes = [c_void_p, c_int]
def SpriteRenderMode(sprite, mode):
	openb3d.SpriteRenderMode(sprite, mode)

openb3d.SpriteViewMode.argtypes = [c_void_p, c_int]
def SpriteViewMode(sprite, mode):
	openb3d.SpriteViewMode(sprite, mode)

openb3d.StencilAlpha.argtypes = [c_void_p, c_float]
def StencilAlpha(stencil, a):
	openb3d.StencilAlpha(stencil, a)

openb3d.StencilClsColor.argtypes = [c_void_p, c_float, c_float, c_float]
def StencilClsColor(stencil, r, g, b):
	openb3d.StencilClsColor(stencil, r, g, b)

openb3d.StencilClsMode.argtypes = [c_void_p, c_int, c_int]
def StencilClsMode(stencil, color, zbuffer):
	openb3d.StencilClsMode(stencil, color, zbuffer)

openb3d.StencilMesh.argtypes = [c_void_p, c_void_p, c_int]
def StencilMesh(stencil, mesh, mode=1):
	openb3d.StencilMesh(stencil, mesh, mode)

openb3d.StencilMode.argtypes = [c_void_p, c_int, c_int]
def StencilMode(stencil, m, o=1):
	openb3d.StencilMode(stencil, m, o)

openb3d.TerrainHeight.argtypes = [c_void_p, c_int, c_int]
openb3d.TerrainHeight.restype = c_float
def TerrainHeight(terr, x, z):
	return openb3d.TerrainHeight(terr, x, z)

openb3d.TerrainX.argtypes = [c_void_p, c_float, c_float, c_float]
openb3d.TerrainX.restype = c_float
def TerrainX(terr, x, y, z):
	return openb3d.TerrainX(terr, x, y, z)

openb3d.TerrainY.argtypes = [c_void_p, c_float, c_float, c_float]
openb3d.TerrainY.restype = c_float
def TerrainY(terr, x, y, z):
	return openb3d.TerrainY(terr, x, y, z)

openb3d.TerrainZ.argtypes = [c_void_p, c_float, c_float, c_float]
openb3d.TerrainZ.restype = c_float
def TerrainZ(terr, x, y, z):
	return openb3d.TerrainZ(terr, x, y, z)

openb3d.TextureBlend.argtypes = [c_void_p, c_int]
def TextureBlend(tex, blend):
	openb3d.TextureBlend(tex, blend)

openb3d.TextureCoords.argtypes = [c_void_p, c_int]
def TextureCoords(tex, coords):
	openb3d.TextureCoords(tex, coords)

openb3d.TextureHeight.argtypes = [c_void_p]
openb3d.TextureHeight.restype = c_int
def TextureHeight(tex):
	return openb3d.TextureHeight(tex)

TextureFilter=openb3d.TextureFilter
openb3d.TextureFilter.argtypes = [c_char_p, c_int]
def TextureFilter(match_text, flags):
	openb3d.TextureFilter(match_text, flags)

openb3d.TextureName.argtypes = [c_void_p]
openb3d.TextureName.restype = c_char_p
def TextureName(tex):
	return openb3d.TextureName(tex)

openb3d.TextureWidth.argtypes = [c_void_p]
openb3d.TextureWidth.restype = c_int
def TextureWidth(tex):
	return openb3d.TextureWidth(tex)

openb3d.TFormedX.restype = c_float
def TFormedX():
	return openb3d.TFormedX()

openb3d.TFormedY.restype = c_float
def TFormedY():
	return openb3d.TFormedY()

openb3d.TFormedZ.restype = c_float
def TFormedZ():
	return openb3d.TFormedZ()

openb3d.TFormNormal.argtypes = [c_float, c_float, c_float, c_void_p, c_void_p]
def TFormNormal(x, y, z, src_ent, dest_ent):
	openb3d.TFormNormal(x, y, z, src_ent, dest_ent)

openb3d.TFormPoint.argtypes = [c_float, c_float, c_float, c_void_p, c_void_p]
def TFormPoint(x, y, z, src_ent, dest_ent):
	openb3d.TFormPoint(x, y, z, src_ent, dest_ent)

openb3d.TFormVector.argtypes = [c_float, c_float, c_float, c_void_p, c_void_p]
def TFormVector(x, y, z, src_ent, dest_ent):
	openb3d.TFormVector(x, y, z, src_ent, dest_ent)

openb3d.TranslateEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]
def TranslateEntity(ent, x, y, z, glob=0):
	openb3d.TranslateEntity(ent, x, y, z, glob)

openb3d.TriangleVertex.argtypes = [c_void_p, c_int, c_int]
openb3d.TriangleVertex.restype = c_int
def TriangleVertex(surf, tri, corner):
	return openb3d.TriangleVertex(surf, tri, corner)

openb3d.TurnEntity.argtypes = [c_void_p, c_float, c_float, c_float, c_bool]
def TurnEntity(ent, x, y, z, glob=0):
	openb3d.TurnEntity(ent, x, y, z, glob)

openb3d.UpdateNormals.argtypes = [c_void_p]
def UpdateNormals(ent):
	openb3d.UpdateNormals(ent)

openb3d.UpdateTexCoords.argtypes = [c_void_p]
def UpdateTexCoords(surf):
	openb3d.UpdateTexCoords(surf)

openb3d.UpdateWorld.argtypes=[c_float]
def UpdateWorld(anim_speed=1):
	openb3d.UpdateWorld(anim_speed)

openb3d.UseStencil.argtypes = [c_void_p]
def UseStencil(stencil):
	openb3d.UseStencil(stencil)

openb3d.VectorPitch.argtypes = [c_float, c_float, c_float]
openb3d.VectorPitch.restype = c_float
def VectorPitch(vx, vy, vz):
	return openb3d.VectorPitch(vx, vy, vz)

openb3d.VectorYaw.argtypes = [c_float, c_float, c_float]
openb3d.VectorYaw.restype = c_float
def VectorYaw(vx, vy, vz):
	return openb3d.VectorYaw(vx, vy, vz)

openb3d.VertexAlpha.argtypes = [c_void_p, c_int]
openb3d.VertexAlpha.restype = c_float
def VertexAlpha(surf, vid):
	return openb3d.VertexAlpha(surf, vid)

openb3d.VertexBlue.argtypes = [c_void_p, c_int]
openb3d.VertexBlue.restype = c_float
def VertexBlue(surf, vid):
	return openb3d.VertexBlue(surf, vid)

openb3d.VertexColor.argtypes = [c_void_p, c_int, c_float, c_float, c_float, c_float]
def VertexColor(surf, vid, r, g, b, a=1):
	openb3d.VertexColor(surf, vid, r, g, b, a)

openb3d.VertexCoords.argtypes = [c_void_p, c_int, c_float, c_float, c_float]
def VertexCoords(surf, vid, x, y, z):
	openb3d.VertexCoords(surf, vid, x, y, z)

openb3d.VertexGreen.argtypes = [c_void_p, c_int]
openb3d.VertexGreen.restype = c_float
def VertexGreen(surf, vid):
	return openb3d.VertexGreen(surf, vid)

openb3d.VertexNormal.argtypes = [c_void_p, c_int, c_float, c_float, c_float]
def VertexNormal(surf, vid, nx, ny, nz):
	openb3d.VertexNormal(surf, vid, nx, ny, nz)

openb3d.VertexNX.argtypes = [c_void_p, c_int]
openb3d.VertexNX.restype = c_float
def VertexNX(surf, vid):
	return openb3d.VertexNX(surf, vid)

openb3d.VertexNY.argtypes = [c_void_p, c_int]
openb3d.VertexNY.restype = c_float
def VertexNY(surf, vid):
	return openb3d.VertexNY(surf, vid)

openb3d.VertexNZ.argtypes = [c_void_p, c_int]
openb3d.VertexNZ.restype = c_float
def VertexNZ(surf, vid):
	return openb3d.VertexNZ(surf, vid)

openb3d.VertexRed.argtypes = [c_void_p, c_int]
openb3d.VertexRed.restype = c_float
def VertexRed(surf, vid):
	return openb3d.VertexRed(surf, vid)

openb3d.VertexTexCoords.argtypes = [c_void_p, c_int, c_float, c_float, c_float, c_int]
def VertexTexCoords(surf, vid, u, v, w=0, coord_set=0):
	openb3d.VertexTexCoords(surf, vid, u, v, w, coord_set)

openb3d.VertexU.argtypes = [c_void_p, c_int, c_int]
openb3d.VertexU.restype = c_float
def VertexU(surf, vid):
	return openb3d.VertexU(surf, vid)

openb3d.VertexV.argtypes = [c_void_p, c_int, c_int]
openb3d.VertexV.restype = c_float
def VertexV(surf, vid):
	return openb3d.VertexV(surf, vid)

openb3d.VertexW.argtypes = [c_void_p, c_int, c_int]
openb3d.VertexW.restype = c_float
def VertexW(surf, vid):
	return openb3d.VertexW(surf, vid)

openb3d.VertexX.argtypes = [c_void_p, c_int]
openb3d.VertexX.restype = c_float
def VertexX(surf, vid):
	return openb3d.VertexX(surf, vid)

openb3d.VertexY.argtypes = [c_void_p, c_int]
openb3d.VertexY.restype = c_float
def VertexY(surf, vid):
	return openb3d.VertexY(surf, vid)

openb3d.VertexZ.argtypes = [c_void_p, c_int]
openb3d.VertexZ.restype = c_float
def VertexZ(surf, vid):
	return openb3d.VertexZ(surf, vid)

openb3d.VoxelSpriteMaterial.argtypes = [c_void_p, c_void_p]
def VoxelSpriteMaterial(voxelspr, mat):
	openb3d.VoxelSpriteMaterial(voxelspr, mat)

openb3d.Wireframe.argtypes = [c_int]
def Wireframe(enable):
	openb3d.Wireframe(enable)

openb3d.EntityScaleX.argtypes = [c_void_p, c_bool]
openb3d.EntityScaleX.restype = c_float
def EntityScaleX(ent, glob=0):
	return openb3d.EntityScaleX(ent, glob)

openb3d.EntityScaleY.argtypes = [c_void_p, c_bool]
openb3d.EntityScaleY.restype = c_float
def EntityScaleY(ent, glob=0):
	return openb3d.EntityScaleY(ent, glob)

openb3d.EntityScaleZ.argtypes = [c_void_p, c_bool]
openb3d.EntityScaleZ.restype = c_float
def EntityScaleZ(ent, glob=0):
	return openb3d.EntityScaleZ(ent, glob)

openb3d.LoadShader.argtypes = [c_char_p, c_char_p, c_char_p]
openb3d.LoadShader.restype = c_void_p
def LoadShader(shader_name, vert, frag):
	return openb3d.LoadShader(shader_name, vert, frag)

openb3d.CreateShader.argtypes = [c_char_p, c_char_p, c_char_p]
openb3d.CreateShader.restype = c_void_p
def CreateShader(shader_name, vert, frag):
	return openb3d.CreateShader(shader_name, vert, frag)

openb3d.ShadeSurface.argtypes = [c_void_p, c_void_p]
def ShadeSurface(surf, shader):
	openb3d.ShadeSurface(surf, shader)

openb3d.ShadeMesh.argtypes = [c_void_p, c_void_p]
def ShadeMesh(mesh, shader):
	openb3d.ShadeMesh(mesh, shader)

openb3d.ShadeEntity.argtypes = [c_void_p, c_void_p]
def ShadeEntity(ent, shader):
	openb3d.ShadeEntity(ent, shader)

openb3d.ShaderTexture.argtypes = [c_void_p, c_void_p, c_char_p, c_int]
def ShaderTexture(shader, tex, name, index=0):
	openb3d.ShaderTexture(shader, tex, name, index)

openb3d.SetFloat.argtypes = [c_void_p, c_char_p, c_float]
def SetFloat(shader, name, v1):
	openb3d.SetFloat(shader, name, v1)

openb3d.SetFloat2.argtypes = [c_void_p, c_char_p, c_float, c_float]
def SetFloat2(shader, name, v1, v2):
	openb3d.SetFloat2(shader, name, v1. v2)

openb3d.SetFloat3.argtypes = [c_void_p, c_char_p, c_float, c_float, c_float]
def SetFloat3(shader, name, v1, v2, v3):
	openb3d.SetFloat3(shader, name, v1, v2, v3)

openb3d.SetFloat4.argtypes = [c_void_p, c_char_p, c_float, c_float, c_float, c_float]
def SetFloat4(shader, name, v1, v2, v3, v4):
	openb3d.SetFloat4(shader, name, v1, v2, v3, v4)

openb3d.SetInteger.argtypes = [c_void_p, c_char_p, c_int]
def SetInteger(shader, name, v1):
	openb3d.SetInteger(shader, name, v1)

openb3d.SetInteger2.argtypes = [c_void_p, c_char_p, c_int, c_int]
def SetInteger2(shader, name, v1, v2):
	openb3d.SetInteger2(shader, name, v1, v2)

openb3d.SetInteger3.argtypes = [c_void_p, c_char_p, c_int, c_int, c_int]
def SetInteger3(shader, name, v1, v2, v3):
	openb3d.SetInteger3(shader, name, v1, v2, v3)

openb3d.SetInteger4.argtypes = [c_void_p, c_char_p, c_int, c_int, c_int, c_int]
def SetInteger4(shader, name, v1, v2, v3, v4):
	openb3d.SetInteger4(shader, name, v1, v2, v3, v4)

openb3d.UseSurface.argtypes = [c_void_p, c_char_p, c_void_p, c_int]
def UseSurface(shader, name, surf, vbo):
	openb3d.UseSurface(shader, name, surf, vbo)

openb3d.UseMatrix.argtypes = [c_void_p, c_char_p, c_int]
def UseMatrix(shader, name, mode):
	openb3d.UseMatrix(shader, name, mode)

openb3d.LoadMaterial.argtypes = [c_char_p, c_int, c_int, c_int, c_int, c_int]
openb3d.LoadMaterial.restype = c_void_p
def LoadMaterial(file, flags, frame_width, frame_height, first_frame, frame_count):
	return openb3d.LoadMaterial(file, flags, frame_width, frame_height, first_frame, frame_count)

openb3d.ShaderMaterial.argtypes = [c_void_p, c_void_p, c_char_p, c_int]
def ShaderMaterial(shader, tex, name, index):
	openb3d.ShaderMaterial(shader, tex, name, index)

openb3d.AmbientShader.argtypes = [c_void_p]
def AmbientShader(shader):
	openb3d.AmbientShader(shader)

openb3d.CreateOcTree.argtypes = [c_float, c_float, c_float, c_void_p]
openb3d.CreateOcTree.restype = c_void_p
def CreateOcTree(w, h, d, parent=0):
	return openb3d.CreateOcTree(w, h, d, parent)

openb3d.OctreeBlock.argtypes = [c_void_p, c_void_p, c_int, c_float, c_float, c_float, c_float, c_float]
def OctreeBlock(octree, mesh, level, x, y, z, near=0, far=1000):
	openb3d.OctreeBlock(octree, mesh, level, x, y, z, near, far)

openb3d.OctreeMesh.argtypes = [c_void_p, c_void_p, c_int, c_float, c_float, c_float, c_float, c_float]
def OctreeBlock(octree, mesh, level, x, y, z, near=0, far=1000):
	openb3d.OctreeBlock(octree, mesh, level, x, y, z, near, far)

openb3d.CreateParticleEmitter.argtypes = [c_void_p, c_void_p]
openb3d.CreateParticleEmitter.restype = c_void_p
def CreateParticleEmitter(particle, parent=0):
	return openb3d.CreateParticleEmitter(particle, parent)

openb3d.ActMoveBy.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
openb3d.ActMoveBy.restype = c_void_p
def ActMoveBy(ent, a, b, c, r):
	return openb3d.ActMoveBy(ent, a, b, c, r)

openb3d.ActTurnBy.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
openb3d.ActTurnBy.restype = c_void_p
def ActTurnBy(ent, a, b, c, r):
	return openb3d.ActTurnBy(ent, a, b, c, r)

openb3d.ActVector.argtypes = [c_void_p, c_float, c_float, c_float]
openb3d.ActVector.restype = c_void_p
def ActVector(ent, a, b, c):
	return openb3d.ActVector(ent, a, b, c)

openb3d.ActMoveTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
openb3d.ActMoveTo.restype = c_void_p
def ActMoveTo(ent, a, b, c, r):
	return openb3d.ActMoveTo(ent, a, b, c, r)

openb3d.ActTurnTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
openb3d.ActTurnTo.restype = c_void_p
def ActTurnTo(ent, a, b, c, r):
	return openb3d.ActTurnTo(ent, a, b, c, r)

openb3d.ActScaleTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
openb3d.ActScaleTo.restype = c_void_p
def ActScaleTo(ent, a, b, c, r):
	return openb3d.ActScaleTo(ent, a, b, c, r)

openb3d.ActFadeTo.argtypes = [c_void_p, c_float, c_float]
openb3d.ActFadeTo.restype = c_void_p
def ActFadeTo(ent, a, r):
	return openb3d.ActFadeTo(ent, a, r)

openb3d.ActTintTo.argtypes = [c_void_p, c_float, c_float, c_float, c_float]
openb3d.ActTintTo.restype = c_void_p
def ActTintTo(ent, a, b, c, r):
	return openb3d.ActTintTo(ent, a, b, c, r)

openb3d.ActTrackByPoint.argtypes = [c_void_p, c_void_p, c_float, c_float, c_float, c_float]
openb3d.ActTrackByPoint.restype = c_void_p
def ActTrackByPoint(ent, t, a, b, c, r):
	return openb3d.ActTrackByPoint(ent, t, a, b, c, r)

openb3d.ActTrackByDistance.argtypes = [c_void_p, c_void_p, c_float, c_float]
openb3d.ActTrackByDistance.restype = c_void_p
def ActTrackByDistance(ent, t, a , r):
	return openb3d.ActTrackByDistance(ent, t, a, r)

openb3d.ActNewtonian.argtypes = [c_void_p, c_float]
openb3d.ActNewtonian.restype = c_void_p
def ActNewtonian(ent, r):
	return openb3d.ActNewtonian(ent, a, r)

openb3d.AppendAction.argtypes = [c_void_p, c_void_p]
def AppendAction(act1, act2):
	return openb3d.AppendAction(act1, act2)

openb3d.FreeAction.argtypes = [c_void_p]
def FreeAction(act):
	openb3d.FreeAction(act)

def Flip():
	sdl.SDL_GL_SwapBuffers()

