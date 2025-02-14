import requests
import json
from .exceptions import PassInfoAPIError

class PassInfoSDKClient:
    """A client for interacting with the PassInfo API to send messages.

    This class provides a convenient interface for sending messages through the PassInfo
    messaging platform. It supports various messaging capabilities including:
    - Sending single messages to individual contacts
    - Sending bulk messages to multiple contacts
    - Sending messages to predefined groups

    The client handles authentication, request formatting, and error handling for all
    API interactions. It requires valid API credentials (api_key and client_id) which
    can be obtained from your PassInfo dashboard.

    Attributes:
        api_key (str): The API key for authentication with PassInfo API.
        client_id (str): Your unique client identifier for the PassInfo platform.
        base_url (str): The base URL for the PassInfo API endpoints.

    Example:
        >>> # Initialize the client
        >>> client = PassInfoSDKClient(
        ...     api_key="your-api-key",
        ...     client_id="your-client-id"
        ... )
        >>>
        >>> # Send a single message
        >>> response = client.send_message(
        ...     message="Hello!",
        ...     contact="1234567890",
        ...     sender_name="MyApp"
        ... )
        >>>
        >>> # Send bulk messages
        >>> contacts = ["1234567890", "0987654321"]
        >>> response = client.send_message_bulk(
        ...     message="Hello everyone!",
        ...     sender_name="MyApp",
        ...     contacts=contacts
        ... )
    """
    
    def __init__(self, api_key, client_id, base_url="https://api.passinfo.net"):
        """Initialize a new PassInfo SDK client instance.

        Args:
            api_key (str): The API key used for authentication with the PassInfo API.
                This key must be obtained from your PassInfo dashboard and is required
                for all API requests. Keep this key secure and do not share it.
            client_id (str): Your unique client identifier provided by PassInfo.
                This ID is used to track and manage your API usage and must be included
                in all API requests.
            base_url (str, optional): The base URL for the PassInfo API endpoints.
                Use this to specify a different API environment (e.g., staging or testing).
                Defaults to "https://api.passinfo.net".

        Example:
            >>> client = PassInfoSDKClient(
            ...     api_key="your-api-key-here",
            ...     client_id="your-client-id",
            ...     base_url="https://api.passinfo.net"
            ... )
        """
        self.api_key = api_key
        self.base_url = base_url
        self.client_id = client_id
        
    def _make_request(self, method, endpoint, params=None, data=None):
        """Makes an HTTP request to the PassInfo API endpoint.

        This internal method handles all HTTP communication with the PassInfo API,
        including request formatting, header management, and error handling.

        Args:
            method (str): The HTTP method to use for the request (e.g., 'GET', 'POST',
                'PUT', 'DELETE'). This determines the type of operation to perform on
                the specified endpoint.
            endpoint (str): The API endpoint path to send the request to, relative to
                the base URL (e.g., 'v1/message/single_message'). Do not include the
                base URL or leading slash.
            params (dict, optional): URL query parameters to include in the request.
                These are added to the URL after the '?' character. For example,
                {'limit': 10, 'offset': 20}. Defaults to None.
            data (dict, optional): The request body data to send, which will be
                serialized to JSON. This is typically used for POST/PUT requests
                to send data to the API. Defaults to None.

        Raises:
            PassInfoAPIError: Raised when the API request fails for any reason,
                including network errors, authentication failures, or invalid
                responses. The error will include the HTTP status code (if available)
                and a descriptive error message.

        Returns:
            dict: The parsed JSON response from the API. The exact structure depends
                on the endpoint being called, but typically includes a success
                indicator and any requested data.

        Example:
            >>> client = PassInfoSDKClient('api_key', 'client_id')
            >>> response = client._make_request(
            ...     method='POST',
            ...     endpoint='v1/message/single_message',
            ...     data={'message': 'Hello', 'contact': '1234567890'}
            ... )
            >>> print(response)
            {'status': 'success', 'message_id': '123'}
        """
        
        headers = {
            "Api-Key": str(self.api_key),
            "Client-Id": str(self.client_id),
            "Content-Type": 'application/json',
            "Accept": 'application/json'
        }
        
        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.request(method=method, url=url, headers=headers, params=params, json=data, verify=True)
            print(response.request.headers)
            print(response.json())
            return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
            raise PassInfoAPIError(
                status_code=getattr(e.response, 'status_code', 500),
                message=f"API request failed: {str(e)}"
            )
            
    def send_message(self, message, contact, sender_name):
        """Send a single message to a specific contact through the PassInfo platform.

        This method sends a single message to an individual contact. It handles the
        validation of required parameters and formats the request appropriately before
        sending it to the PassInfo API.

        Args:
            message (str): The content of the message to be sent. This is the actual
                text that will be delivered to the recipient.
            contact (str): The contact identifier (e.g., phone number) of the message
                recipient. This should be in a format accepted by the PassInfo platform.
            sender_name (str): The name that will appear as the sender of the message.
                This helps recipients identify who sent the message.

        Raises:
            PassInfoAPIError: Raised in the following cases:
                - If message is None (status_code=400)
                - If contact is None (status_code=400)
                - If sender_name is None (status_code=400)
                - If the API request fails (status_code varies)

        Returns:
            dict: The API response containing the status of the message send operation.
                Typically includes fields like 'status' and 'message_id'.

        Example:
            >>> client = PassInfoSDKClient('api_key', 'client_id')
            >>> response = client.send_message(
            ...     message='Your verification code is 123456',
            ...     contact='1234567890',
            ...     sender_name='MyApp'
            ... )
            >>> print(response)
            {'status': 'success', 'message_id': '123'}
        """
        if message is None:
            raise PassInfoAPIError(status_code=400, message="Message is required.")
        elif contact is None:
            raise PassInfoAPIError(status_code=400, message="Contact is required.")
        elif sender_name is None:
            raise PassInfoAPIError(status_code=400, message="Sender name is required.")
        
        data = dict(
            message=message,
            contact=contact,
            senderName=sender_name,
        )
        return self._make_request(method='POST', endpoint='v1/message/single_message', data=data)
    
    def send_message_bulk(self, message, sender_name, contacts):
        """Send a message to multiple contacts simultaneously through the PassInfo platform.

        This method enables sending the same message to multiple contacts in a single API
        call, which is more efficient than sending individual messages when you need to
        reach multiple recipients.

        Args:
            message (str): The content of the message to be sent. This same text will
                be delivered to all specified contacts.
            sender_name (str): The name that will appear as the sender of the message
                to all recipients. This helps recipients identify who sent the message.
            contacts (list): A list of contact identifiers (e.g., phone numbers) who
                should receive the message. Each contact should be in a format accepted
                by the PassInfo platform.

        Raises:
            PassInfoAPIError: Raised in the following cases:
                - If message is None (status_code=400)
                - If contacts is None or empty (status_code=400)
                - If sender_name is None (status_code=400)
                - If the API request fails (status_code varies)

        Returns:
            dict: The API response containing the status of the bulk message send
                operation. Typically includes information about successful and failed
                deliveries.

        Example:
            >>> client = PassInfoSDKClient('api_key', 'client_id')
            >>> contacts = ['1234567890', '0987654321']
            >>> response = client.send_message_bulk(
            ...     message='Join our event tomorrow!',
            ...     sender_name='MyApp',
            ...     contacts=contacts
            ... )
            >>> print(response)
            {'status': 'success', 'successful_sends': 2, 'failed_sends': 0}
        """
        if message is None:
            raise PassInfoAPIError(status_code=400, message="Message is required.")
        elif contacts is None or len(contacts) == 0:
            raise PassInfoAPIError(status_code=400, message="Contacts are required.")
        elif sender_name is None:
            raise PassInfoAPIError(status_code=400, message="Sender name is required.")
        
        data = dict(
            message=message,
            contacts=contacts,
            senderName=sender_name,
        )
        return self._make_request(method='POST', endpoint='v1/message/send_bulk_contacts_messages', data=data)
    
    def send_message_group(self, message, sender_name, group_id):
        """Send a message to a predefined group of contacts through the PassInfo platform.

        This method sends a message to all contacts that are members of the specified
        group. Groups must be created and managed through the PassInfo dashboard before
        they can be used for messaging.

        Args:
            message (str): The content of the message to be sent. This text will be
                delivered to all members of the specified group.
            sender_name (str): The name that will appear as the sender of the message
                to all group members. This helps recipients identify who sent the message.
            group_id (str): The unique identifier of the group to send the message to.
                This ID can be obtained from your PassInfo dashboard.

        Raises:
            PassInfoAPIError: Raised in the following cases:
                - If message is None (status_code=400)
                - If sender_name is None (status_code=400)
                - If group_id is None (status_code=400)
                - If the API request fails (status_code varies)

        Returns:
            dict: The API response containing the status of the group message send
                operation. Typically includes information about the delivery status
                and number of recipients.

        Example:
            >>> client = PassInfoSDKClient('api_key', 'client_id')
            >>> response = client.send_message_group(
            ...     message='Monthly update: New features available!',
            ...     sender_name='MyApp',
            ...     group_id='group_123'
            ... )
            >>> print(response)
            {'status': 'success', 'group_size': 50, 'messages_queued': 50}
        """
        
        if message is None:
            raise PassInfoAPIError(status_code=400, message="Message is required.")
        elif sender_name is None:
            raise PassInfoAPIError(status_code=400, message="Sender name is required.")
        elif group_id is None:
            raise PassInfoAPIError(status_code=400, message="Group ID is required.")
        
        data = dict(
            message=message,
            senderName=sender_name,
        )
        return self._make_request(method='POST', endpoint=f'v1/message/send_message_to_group/{group_id}', data=data)
    
    def get_message_status(self, message_id):
        """Retrieve the status of a previously sent message.

        This method allows you to query the status of a message that you have already
        sent. It uses the unique message ID to identify the message and provides the
        current status, such as 'pending', 'sent', or 'failed'. This is particularly
        useful for tracking important messages and implementing delivery confirmation
        workflows in your application.

        The method performs a real-time status check against the PassInfo API and
        returns the most up-to-date information about the message's delivery status.
        This can be used to build message tracking dashboards, implement retry logic
        for failed messages, or provide delivery confirmation to your users.

        Args:
            message_id (str): The unique identifier of the message whose status you
                want to check. This ID is returned in the response when the message
                is initially sent through any of the send message methods.
                Must be a valid message ID from a previous send operation.

        Raises:
            PassInfoAPIError: Raised in the following cases:
                - If message_id is None (status_code=400)
                - If message_id is invalid or not found (status_code=404)
                - If authentication fails (status_code=401)
                - If the API request fails (status_code varies)

        Returns:
            dict: The API response containing the status of the message. This typically
                includes the following fields:
                - status (str): Current delivery status ('pending', 'sent', 'failed', 'delivered')
                - message_id (str): The unique identifier of the tracked message
                - timestamp (str): The timestamp of the last status update
                - error_message (str, optional): Description of any delivery errors

        Example:
            >>> client = PassInfoSDKClient('api_key', 'client_id')
            >>> response = client.get_message_status(message_id='1234567890')
            >>> print(response)
            {
                'status': 'delivered',
                'message_id': '1234567890',
                'timestamp': '2024-01-20T15:30:45Z'
            }

        Note:
            - Status polling should be implemented with appropriate intervals to avoid
              API rate limiting
            - Consider implementing exponential backoff for status checks of pending messages
            - Store and track message IDs for messages that require delivery confirmation
        """

        
        if message_id is None:
            raise PassInfoAPIError(status_code=400, message="Message ID is required.")

        return self._make_request(method='GET', endpoint=f'v1/message/get_single_status/{message_id}')
    
    def get_message_status_bulk(self, batch_id):
        """Retrieve the status of multiple messages sent in a single batch.

        This method provides a way to efficiently track the delivery status of multiple
        messages that were sent as part of a bulk operation. It's particularly useful
        for monitoring large-scale message campaigns or batch notifications where
        individual message tracking would be impractical.

        The method performs a real-time query against the PassInfo API to get the
        current status of all messages in the specified batch. This can be used to:
        - Monitor overall delivery success rates
        - Identify and handle failed deliveries
        - Track progress of large message campaigns
        - Generate delivery reports and analytics

        Args:
            batch_id (str): The unique identifier of the batch whose status you want
                to check. This ID is returned when sending messages through the
                send_message_bulk method. Must be a valid batch ID from a previous
                bulk send operation.

        Raises:
            PassInfoAPIError: Raised in the following cases:
                - If batch_id is None (status_code=400)
                - If batch_id is invalid or not found (status_code=404)
                - If authentication fails (status_code=401)
                - If the API request fails (status_code varies)

        Returns:
            dict: The API response containing detailed status information about the
                batch. This includes:
                - status (str): Overall batch status ('processing', 'completed', 'failed')
                - successful (int): Number of successfully delivered messages
                - failed (int): Number of failed message deliveries
                - pending (int): Number of messages still in the delivery queue
                - timestamp (str): Last status update timestamp
                - error_details (list, optional): Details of any delivery failures

        Example:
            >>> client = PassInfoSDKClient('api_key', 'client_id')
            >>> response = client.get_message_status_bulk(batch_id='1234567890')
            >>> print(response)
            {
                'status': 'processing',
                'successful': 45,
                'failed': 2,
                'pending': 3,
                'timestamp': '2024-01-20T15:30:45Z'
            }

        Note:
            - Implement appropriate polling intervals to avoid API rate limits
            - Consider using webhooks for real-time status updates on large batches
            - Store batch IDs for tracking and reporting purposes
            - Set up monitoring for failed deliveries that may need retry logic
        """


        if batch_id is None:
            raise PassInfoAPIError(status_code=400, message="Batch ID is required.")
        
        return self._make_request(method='GET', endpoint=f'v1/message/get_bulk_status/{batch_id}')
    