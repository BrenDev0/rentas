class DependencyNotRegistered(Exception):
    def __init__(self, detail: str = "Dependency not registered"):
        super().__init__(detail)