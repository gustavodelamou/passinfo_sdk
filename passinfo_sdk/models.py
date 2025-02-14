class Contact:
    """A class representing a contact in the PassInfo system.

    This class encapsulates the basic information needed for a contact, including
    their first name, last name, and phone number. It serves as a data structure
    for managing contact information within the PassInfo platform.

    Attributes:
        first_name (str): The first name of the contact.
        last_name (str): The last name of the contact.
        phone_number (str): The contact's phone number in a format accepted by PassInfo.

    Example:
        >>> contact = Contact("John", "Doe", "+1234567890")
        >>> print(f"{contact.first_name} {contact.last_name}")
        'John Doe'
        >>> print(contact.phone_number)
        '+1234567890'
    """

    def __init__(self, first_name, last_name, phone_number):
        """Initialize a new Contact instance.

        Args:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
            phone_number (str): The contact's phone number in a format accepted by PassInfo.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

class PassInfoAPI:
    """A class for interacting with the PassInfo API.

    This class provides a high-level interface for managing contacts and groups
    through the PassInfo platform. It handles various operations such as creating
    contacts, managing groups, and monitoring SMS usage.

    The API requires authentication through both an API key and a client ID, which
    should be obtained from your PassInfo dashboard.

    Attributes:
        api_key (str): The authentication key for the PassInfo API.
        client_id (str): Your unique client identifier for the PassInfo platform.

    Example:
        >>> api = PassInfoAPI(
        ...     api_key="your-secret-api-key",
        ...     client_id="your-client-id"
        ... )
        >>> contact = api.create_contact(
        ...     first_name="Jane",
        ...     last_name="Doe",
        ...     phone_number="+1987654321"
        ... )
        >>> groups = api.get_user_groups()
    """

    def __init__(self, api_key, client_id):
        """Initialize a new PassInfoAPI instance.

        Args:
            api_key (str): The API key for authentication with PassInfo services.
                This key must be obtained from your PassInfo dashboard and should
                be kept secure. It is used to authenticate all API requests and
                identify your account.
            client_id (str): Your unique client identifier for the PassInfo platform.
                This ID is used to track API usage and manage access permissions.
                It must be included in all API requests alongside the API key.

        Example:
            >>> # Initialize with both required credentials
            >>> api = PassInfoAPI(
            ...     api_key="your-secret-api-key",
            ...     client_id="your-client-id"
            ... )

        Note:
            Both api_key and client_id are required for authentication. Keep your
            API key secure and never share it in public repositories or client-side code.
        """
        self.api_key = api_key
        self.client_id = client_id
        
    def create_contact(self, first_name, last_name, phone_number):
        """Create a new contact in the PassInfo system.

        This method creates a new contact with the specified information. The contact
        will be stored in the PassInfo platform and can be used for messaging and
        group management.

        Args:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
            phone_number (str): The contact's phone number in a format accepted by PassInfo.

        Returns:
            Contact: A new Contact instance representing the created contact.

        Example:
            >>> api = PassInfoAPI("your-api-key", "your-client-id")
            >>> contact = api.create_contact(
            ...     first_name="John",
            ...     last_name="Smith",
            ...     phone_number="+1234567890"
            ... )
        """
        from .client import PassInfoSDKClient
        
        client = PassInfoSDKClient(api_key=self.api_key, client_id=self.client_id)
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        }
        try:
            response = client._make_request(
                method='POST',
                endpoint='v1/contact/add_contact',
                data=data
            )
            if response.get('success', False):
                return Contact(first_name, last_name, phone_number)
            return None
        except Exception:
            return None
    
    def get_user_groups(self):
        """Retrieve all user groups associated with the current account.

        This method fetches all groups that have been created under the current
        PassInfo account. These groups can be used for organizing contacts and
        sending bulk messages.

        Returns:
            list: A list of group objects, each containing group information such
                as ID, name, and member count.

        Example:
            >>> api = PassInfoAPI("your-api-key", "your-client-id")
            >>> groups = api.get_user_groups()
            >>> for group in groups:
            ...     print(group['name'])
        """
        from .client import PassInfoSDKClient
        
        client = PassInfoSDKClient(api_key=self.api_key, client_id=self.client_id)
        try:
            response = client._make_request(
                method='GET',
                endpoint='v1/groupe/get_all_my_groupes'
            )
            return response
        except Exception:
            return []
    
    def add_contact_to_group(self, contact_id, group_id):
        """Add a contact to a specified group.

        This method associates an existing contact with an existing group, allowing
        the contact to receive messages sent to that group.

        Args:
            contact_id (str): The unique identifier of the contact to add.
            group_id (str): The unique identifier of the target group.

        Returns:
            bool: True if the contact was successfully added to the group,
                False otherwise.

        Example:
            >>> api = PassInfoAPI("your-api-key", "your-client-id")
            >>> success = api.add_contact_to_group(
            ...     contact_id="contact_123",
            ...     group_id="group_456"
            ... )
        """
        from .client import PassInfoSDKClient
        
        client = PassInfoSDKClient(api_key=self.api_key, client_id=self.client_id)
        data = {
            "contact_id": contact_id,
            "group_id": group_id
        }
        try:
            response = client._make_request(
                method='POST',
                endpoint='v1/groupe/add_contact_to_group',
                data=data
            )
            return response.get('success', False)
        except Exception:
            return False
    
    def get_sms_count(self):
        """Get the remaining SMS credit balance for the account.

        This method queries the current balance of SMS credits available for
        sending messages through the PassInfo platform.

        Returns:
            int: The number of SMS credits remaining in the account.

        Example:
            >>> api = PassInfoAPI("your-api-key", "your-client-id")
            >>> remaining_credits = api.get_sms_count()
            >>> print(f"You have {remaining_credits} SMS credits remaining")
        """
        from .client import PassInfoSDKClient
        
        client = PassInfoSDKClient(api_key=self.api_key, client_id=self.client_id)
        try:
            response = client._make_request(
                method='GET',
                endpoint='v1/user/get_solde'
            )
            return response.get('solde', 0)
        except Exception:
            return 0
    
    def renew_api_key(self):
        """Generate a new API key for the account.

        This method invalidates the current API key and generates a new one. This
        should be used when you need to rotate your API credentials for security
        purposes.

        Returns:
            str: The newly generated API key.

        Example:
            >>> api = PassInfoAPI("old-api-key", "your-client-id")
            >>> new_key = api.renew_api_key()
            >>> print("Your new API key:", new_key)
        """
        from .client import PassInfoSDKClient
        
        client = PassInfoSDKClient(api_key=self.api_key, client_id=self.client_id)
        try:
            response = client._make_request(
                method='GET',
                endpoint='v1/user/renew_api_key'
            )
            return response.get('new_api_key', '')
        except Exception:
            return ''
    
    def get_contacts_list(self, page=1, limit=10):
        """Retrieve a paginated list of contacts.

        This method returns a list of contacts associated with the account,
        with support for pagination to handle large numbers of contacts efficiently.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            limit (int, optional): The number of contacts per page. Defaults to 10.

        Returns:
            list: A list of Contact objects for the requested page.

        Example:
            >>> api = PassInfoAPI("your-api-key", "your-client-id")
            >>> # Get the first page of contacts, 10 per page
            >>> contacts = api.get_contacts_list(page=1, limit=10)
            >>> # Get the second page
            >>> more_contacts = api.get_contacts_list(page=2, limit=10)
        """
        from .client import PassInfoSDKClient
        
        client = PassInfoSDKClient(api_key=self.api_key, client_id=self.client_id)
        params = {
            "page": page,
            "limit": limit
        }
        try:
            response = client._make_request(
                method='GET',
                endpoint='v1/contact/all_my_contacts',
                params=params
            )
            contacts_data = response.get('contacts', [])
            return [Contact(
                first_name=contact.get('first_name', ''),
                last_name=contact.get('last_name', ''),
                phone_number=contact.get('phone_number', '')
            ) for contact in contacts_data]
        except Exception:
            return []
    
    def add_users_to_contact(self, contact_id, user_ids):
        """Associate multiple users with a contact.

        This method allows you to link multiple user accounts to a single contact,
        which can be useful for managing shared contacts or contact permissions.

        Args:
            contact_id (str): The unique identifier of the target contact.
            user_ids (list): A list of user IDs to associate with the contact.

        Returns:
            bool: True if all users were successfully added to the contact,
                False otherwise.

        Example:
            >>> api = PassInfoAPI("your-api-key", "your-client-id")
            >>> user_ids = ["user_123", "user_456", "user_789"]
            >>> success = api.add_users_to_contact(
            ...     contact_id="contact_123",
            ...     user_ids=user_ids
            ... )
        """
        from .client import PassInfoSDKClient
        
        client = PassInfoSDKClient(api_key=self.api_key, client_id=None)
        data = {
            "contact_id": contact_id,
            "user_ids": user_ids
        }
        try:
            response = client._make_request(
                method='POST',
                endpoint='v1/contact/add_users',
                data=data
            )
            return response.get('success', False)
        except Exception:
            return False
