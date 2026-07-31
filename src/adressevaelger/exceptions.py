class ApiError(Exception):
    def __init__(self, message: str | None):
        self.message = message
        super().__init__(self.message)


class ApiConnectionError(ApiError):
    pass


class ApiRetryError(ApiError):
    pass


class ApiTooManyRequests(ApiError):
    pass


class ApiUnkownError(ApiError):
    pass
