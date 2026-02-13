import inspect

class Injector:
    def __init__(self):
        self._registry = {}
        self._singletons = {}


    def register(self, instance_type, resolve_as=None, *, singleton=True):
        if not resolve_as:
            resolve_as = instance_type

        self._registry[instance_type] = {
            "resolve_as": resolve_as,
            "singleton": singleton
        }


    def resolve(self, instance_type):
        if instance_type in self._singletons:
            return self._singletons[instance_type]
        
        if instance_type not in self._registry:
            raise Exception(f"{instance_type} not registered")
        
        registration = self._registry[instance_type]
        instance = self._build(instance_type)

        if registration["singleton"]:
            self._singletons[instance_type] = instance

        return instance


    def _build(self, cls):
        signature = inspect.signature(cls.__init__)
        dependencies = []

        for name, params in signature.parameters.items():
            if name == "self":
                continue

            dependency_type = params.annotation
            dependency = self.resolve(dependency_type)
            dependencies.append(dependencies)

            return cls(*dependencies)

        
