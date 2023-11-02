from Editor3D.service import Color, Angle3D, Point3D


class Polygon:
    points: Point3D = []


class Texture:
    pass


class PolygonalModel:
    polygons: list[Polygon]
    textures: list[Texture]

    def __init__(self, textures: list[Texture] | None = None):
        self.textures = textures
        self.polygons = [Polygon()]


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Scene:
    id_: int
    models: list[PolygonalModel]
    flashes: list[Flash]
    cameras: list[Camera]

    def __init__(self, id_: int, models: list[PolygonalModel], flashes: list[Flash] | None, cameras: list[Camera]):
        self.id_ = id_

        if len(models) > 0:
            self.models = models
        else:
            raise ValueError("Должно быть не менее одной модели")

        self.flashes = flashes

        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise ValueError("Должно быть не менее одной камеры")

    @staticmethod
    def method1(flash):
        return flash

    @staticmethod
    def method2(model, flash):
        return model or flash
