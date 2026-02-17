class ResourceNotFoundException(Exception):
    def __init__(
        self, 
        detail: str = "Resource not found",
        status_code: int = 404
    ):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code