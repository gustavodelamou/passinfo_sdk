class PassInfoSDKError(Exception):
    """Base exception class for all PassInfo SDK errors.

    This is the parent class for all exceptions raised by the PassInfo SDK. It
    provides a foundation for error handling and helps distinguish SDK-specific
    errors from other Python exceptions.

    All specific exceptions in the SDK should inherit from this class, allowing
    users to catch any SDK-related error by catching PassInfoSDKError.

    Example:
        >>> try:
        ...     # SDK operations
        ... except PassInfoSDKError as e:
        ...     print(f"SDK Error: {str(e)}")
        ...     # Handle any SDK-related error
    """
    
    pass

class PassInfoAPIError(PassInfoSDKError):
    """Exception raised for errors that occur during PassInfo API operations.

    This exception is raised when an API request fails, whether due to client-side
    validation errors, server-side errors, or network issues. It provides both an
    error message and an HTTP status code to help diagnose and handle the error
    appropriately.

    Args:
        message (str): A human-readable error message describing what went wrong.
        status_code (int): The HTTP status code associated with the error.
            Common codes include:
            - 400: Bad Request (invalid parameters)
            - 401: Unauthorized (invalid API credentials)
            - 404: Not Found (resource doesn't exist)
            - 500: Internal Server Error

    Attributes:
        message (str): The error message passed to the constructor.
        status_code (int): The HTTP status code passed to the constructor.

    Example:
        >>> try:
        ...     client.send_message(message=None, contact="123", sender_name="Test")
        ... except PassInfoAPIError as e:
        ...     print(f"API Error {e.status_code}: {e.message}")
        ...     if e.status_code == 400:
        ...         print("Please check your input parameters")
        API Error 400: Message is required.
        Please check your input parameters
    """
    
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code