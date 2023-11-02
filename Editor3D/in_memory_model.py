from Editor3D.model_elements import PolygonalModel, Scene, Camera, Flash


class IModelChangedObserver:
    def apply_update_model(self):
        pass


class IModelChanger:
    def notify_change(self, sender: IModelChanger):
        pass


class ModelStore(IModelChanger):
    models: list[PolygonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]
    _change_observers: list[IModelChangedObserver]

    def __init__(self, change_observer: list[IModelChangedObserver] | None) -> None:
        self.models = [PolygonalModel()]
        self.flashes = [Flash()]
        self.cameras = [Camera()]
        self.scenes = [Scene(0, self.models, self.flashes, self.cameras)]
        self._change_observers = change_observer

    def get_scene(self, id_):
        for scene in self.scenes:
            if scene.id_ == id_:
                return scene

    def notify_change(self, sender: IModelChanger):
        pass
