# PassInfo SDK
# ![PASSEINFO](https://api.passinfo.net/v1/content/logo.png "PassInfo Logo")

A powerful and intuitive Python SDK for seamless integration with the PassInfo API, enabling fast, reliable, and secure message delivery across multiple channels. This SDK simplifies complex messaging operations into clean, maintainable code, making it the ideal choice for businesses seeking robust communication solutions.

## Description

PassInfo SDK is a powerful and user-friendly Python library designed to simplify the integration of PassInfo messaging services into your applications. This SDK abstracts the complexity of direct API interactions, offering a clean and intuitive interface for sending messages through various channels.

The SDK handles all the necessary API authentication, request formatting, and response parsing, allowing developers to focus on implementing their messaging logic rather than dealing with low-level API details. It provides robust error handling, automatic retries for failed requests, and comprehensive logging capabilities.

Key advantages of using PassInfo SDK include:
- **Simplified Integration**: Easy-to-use methods for all messaging operations
- **Type Safety**: Built-in validation for all API parameters
- **Flexible Configuration**: Customizable settings for different use cases
- **Production Ready**: Battle-tested in high-volume messaging scenarios
- **Well Documented**: Comprehensive documentation with practical examples
- **Efficient Resource Usage**: Optimized for handling both single and bulk message operations

Whether you're sending transactional messages, marketing communications, or system notifications, PassInfo SDK provides the tools and flexibility you need to implement robust messaging functionality in your Python applications.

## Features

- Send single messages to individual contacts
- Send bulk messages to multiple contacts simultaneously
- Send messages to predefined contact groups
- Track message delivery status for single and bulk messages
- Monitor batch message status and delivery reports
- Comprehensive error handling
- Automatic request formatting and validation
- Secure API authentication

## Installation

PassInfo SDK can be easily installed using pip, Python's package installer. The SDK is compatible with all major operating systems (Windows, macOS, Linux) and requires minimal dependencies. Before installing, ensure you have Python 3.6 or higher installed on your system.

### Requirements

- Python 3.6 or higher
- `requests` library

### Install via pip

```bash
pip install passinfo-sdk
```

## Quick Start

This section will guide you through the essential steps to start using the PassInfo SDK in your application. You'll learn how to initialize the client, send messages to individual contacts, groups, and handle multiple recipients efficiently. Before proceeding, ensure you have:

- Installed the PassInfo SDK package
- Obtained your API credentials from the PassInfo dashboard
- Basic understanding of Python programming

### Initialize the Client

Create a new instance of the PassInfo SDK client with your API credentials. You can obtain these credentials from your PassInfo dashboard:

> **Note**: Keep your API credentials secure and never expose them in your code. Use environment variables or secure configuration management for production deployments.

Here's how to initialize the client:

```python
from passinfo_sdk import PassInfoSDKClient

client = PassInfoSDKClient(
    api_key="your_api_key",    # Your PassInfo API key
    client_id="your_client_id" # Your PassInfo client ID
)
```

### Send a Single Message

Send a message to an individual contact. This method provides a simple way to deliver messages to specific recipients:

```python
response = client.send_message(
    message="Hello World",           # Message content
    contact="phoneNumber",          # Recipient's phone number
    sender_name="senderName"       # Name that appears as the sender
)
print(response)
# Example output: {"status": "success", "message": "123"}
```

#### Parameters
- `message` (str): The content of your message. Keep it clear and concise.
- `contact` (str): The recipient's phone number in a valid format (e.g., "622000001").
- `sender_name` (str): Your sender ID that recipients will see.

#### Response
The method returns a dictionary containing:
- `status`: Success or failure status of the send operation
- `message`: Unique identifier for tracking the message

#### Best Practices
- Validate phone numbers before sending
- Keep message content within character limits
- Store message_id for delivery tracking
- Handle potential API errors using try-except blocks

### Send Bulk Messages

Send a message to multiple contacts simultaneously. This method provides an efficient way to deliver the same message to multiple recipients in a single API call:

```python
contacts = ["622000001", "622000002", "622000003"]
response = client.send_message_bulk(
    message="Hello Everyone",        # Message content
    sender_name="senderName",       # Name that appears as the sender
    contacts=contacts               # List of recipient phone numbers
)
print(response)
# Example output: {"status": "success", "successful_sends": 3, "failed_sends": 0}
```

#### Parameters
- `message` (str): The content of your message that will be sent to all recipients.
- `sender_name` (str): Your sender ID that will appear as the sender to all recipients.
- `contacts` (list): A list of phone numbers to send the message to.

#### Response
The method returns a dictionary containing:
- `status`: Success or failure status of the bulk send operation
- `successful_sends`: Number of messages successfully queued for delivery
- `failed_sends`: Number of messages that failed to queue

 

#### Best Practices
- Keep the contact list size reasonable to avoid timeouts
- Validate all phone numbers before sending
- Monitor the response for failed sends
- Implement retry logic for failed deliveries

### Send Message to Group

Send a message to a predefined group of contacts. This method allows you to efficiently deliver messages to groups that have been created and managed through your PassInfo dashboard:

```python
response = client.send_message_group(
    message="Hello Group",           # Message content
    sender_name="senderName",       # Name that appears as the sender
    group_id="groupId"             # ID of the target group
)
print(response)
# Example output: {"status": "success", "group_size": 50, "messages_queued": 50}
```

#### Parameters
- `message` (str): The content of your message that will be sent to all group members.
- `sender_name` (str): Your sender ID that will appear as the sender to all group members.
- `group_id` (str): The unique identifier of your target group (available in PassInfo dashboard).

#### Response
The method returns a dictionary containing:
- `status`: Success or failure status of the group send operation
- `group_size`: Total number of contacts in the group
- `messages_queued`: Number of messages successfully queued for delivery

#### Best Practices
- Verify group existence before sending
- Keep group sizes manageable
- Monitor delivery status for large groups
- Consider message timing for different time zones

### Get Message Status

Track the delivery status of a single message using its unique message ID:

```python
response = client.get_message_status(
    message_id="1234567890"        # Unique message identifier
)
print(response)
# Example output: {"status": "sent", "message_id": "1234567890"}
```

#### Parameters
- `message_id` (str): The unique identifier of the message to track, returned when the message was sent.

#### Response
The method returns a dictionary containing:
- `status`: Current status of the message (e.g., 'pending', 'sent', 'failed')
- `message_id`: The unique identifier of the tracked message

#### Best Practices
- Store message IDs for important communications
- Implement status polling with appropriate intervals
- Handle all possible status values in your application

### Get Bulk Message Status

Track the delivery status of multiple messages sent in a batch:

```python
response = client.get_message_status_bulk(
    batch_id="1234567890"         # Unique batch identifier
)
print(response)
# Example output: {"status": "processing", "successful": 45, "failed": 2, "pending": 3}
```

#### Parameters
- `batch_id` (str): The unique identifier of the message batch to track.

#### Response
The method returns a dictionary containing:
- `status`: Overall status of the batch
- `successful`: Number of successfully delivered messages
- `failed`: Number of failed deliveries
- `pending`: Number of messages still in queue

#### Best Practices
- Store batch IDs for bulk operations
- Implement retry logic for failed messages
- Monitor delivery rates and patterns
- Set up alerts for high failure rates

## Error Handling

The SDK provides comprehensive error handling through the `PassInfoAPIError` exception:

```python
from passinfo_sdk.exceptions import PassInfoAPIError

try:
    response = client.send_message(
        message="Hello World",
        contact="phoneNumber",
        sender_name="senderName"
    )
except PassInfoAPIError as e:
    print(f"Error {e.status_code}: {e.message}")
```

### Get SMS Credit Balance

Check the remaining SMS credit balance for your account:

```python
try:
    remaining_credits = client.get_sms_count()
    print(f"You have {remaining_credits} SMS credits remaining")
except PassInfoAPIError as e:
    print(f"Error checking SMS balance: {e}")
```

#### Returns
- `int`: The number of SMS credits remaining in the account. Returns 0 if the request fails or if there are no credits available.

#### Best Practices
- Implement regular balance checks to ensure sufficient credits
- Set up low balance alerts in your application
- Handle potential API errors gracefully
- Consider implementing automatic credit top-up mechanisms
- Monitor credit usage patterns for capacity planning

 
### Renew API Key

Rotate your API key for enhanced security using the renew_api_key method. This operation invalidates your current API key and generates a new one:

```python
try:
    response = client.renew_api_key()
    if response.get('api_key'):
        new_key = response['api_key']
        print(f"New API key generated successfully")
        # Update your configuration with the new key
    else:
        print("Failed to generate new API key")
except PassInfoAPIError as e:
    print(f"Error renewing API key: {e}")
```

#### Returns
- `dict`: Contains the new API key in the response
  - `api_key` (str): The newly generated API key

#### Best Practices
- Schedule regular key rotations (e.g., every 90 days)
- Implement proper key transition periods
- Store new keys securely (e.g., environment variables)
- Update all application instances with new key
- Maintain backup access during rotation
- Log all key rotation events

#### Implementation Guidelines
1. **Preparation**
   - Back up current configuration
   - Plan maintenance window if needed
   - Ensure all systems are ready for update

2. **Execution**
   - Generate new API key
   - Validate new key functionality
   - Update configuration files/variables
   - Restart affected services if required

3. **Verification**
   - Test API connectivity with new key
   - Monitor for any authentication errors
   - Verify all systems are functioning

4. **Rollback Plan**
   - Keep old key temporarily accessible
   - Document rollback procedures
   - Set up monitoring for issues

#### Security Considerations
- Never log or display full API keys
- Use secure channels for key distribution
- Implement least-privilege access
- Monitor for unauthorized key usage
- Set up alerts for key-related events

#### Example Implementation
```python
from passinfo_sdk import PassInfoSDKClient
from passinfo_sdk.exceptions import PassInfoAPIError
import os

def rotate_api_key(client):
    try:
        # Generate new key
        response = client.renew_api_key()
        if not response.get('api_key'):
            raise ValueError("No API key in response")

        new_key = response['api_key']
        
        # Validate new key
        test_client = PassInfoSDKClient(
            api_key=new_key,
            client_id=client.client_id
        )
        
        # Test new key
        test_client.get_sms_count()
        
        # Update configuration
        update_api_key_config(new_key)
        
        print("API key rotated successfully")
        return True
        
    except PassInfoAPIError as e:
        print(f"Error rotating API key: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def update_api_key_config(new_key):
    # Update environment variable
    os.environ['PASSINFO_API_KEY'] = new_key
    
    # Update configuration file
    # Implement your configuration update logic here
    pass


## Best Practices
   
### Message Handling

- Implement message queuing for high-volume scenarios
- Use batch processing for bulk messages to optimize performance
- Set up proper retry mechanisms with exponential backoff
- Implement message delivery status tracking
- Handle message priority based on business requirements
- Validate message content before sending

### Performance Optimization

- Use connection pooling for better resource management
- Implement caching for frequently used data
- Optimize batch sizes for bulk operations
- Monitor and adjust concurrent request limits
- Use asynchronous operations where applicable
- Implement proper timeout handling

### Integration Best Practices

- Follow the singleton pattern for client initialization
- Implement proper dependency injection
- Use environment variables for configuration
- Set up comprehensive logging
- Implement proper error boundaries
- Use proper exception handling

### API Rate Limits

- Be mindful of API rate limits when sending bulk messages
- Implement appropriate error handling for rate limit responses
- Consider using exponential backoff for retries

### Security

- Keep your API credentials secure and never expose them in your code
- Use environment variables for storing sensitive information
- Regularly rotate your API keys

### Message Content

- Keep messages concise and clear
- Respect character limits for messages
- Include opt-out instructions when required

### Testing and Monitoring

- Implement comprehensive unit tests
- Set up integration tests for critical paths
- Monitor message delivery rates and latency
- Track and analyze error patterns
- Set up alerts for critical failures
- Maintain test coverage for new features

## API Reference

### PassInfoSDKClient

#### Parameters

- `api_key` (str): Your API key for authentication
- `client_id` (str/int): Your client ID
- `base_url` (str, optional): API base URL. Defaults to "https://api.passinfo.net"

#### Methods

- `send_message(message, contact, sender_name)`: Send a single message
  - `message` (str): Message content
  - `contact` (str): Recipient's phone number
  - `sender_name` (str): Sender's display name

- `send_message_bulk(message, sender_name, contacts)`: Send messages to multiple contacts
  - `message` (str): Message content
  - `sender_name` (str): Sender's display name
  - `contacts` (list): List of recipient phone numbers

- `send_message_group(message, sender_name, group_id)`: Send a message to a group
  - `message` (str): Message content
  - `sender_name` (str): Sender's display name
  - `group_id` (str): Target group ID

## Troubleshooting
 
### Common Issues

1. Authentication Errors
   - Verify your API key and client ID are correct
   - Check if your API key is active
   - Ensure proper formatting of credentials
   - Common causes:
     * Expired API key
     * Incorrect client ID format
     * Missing or malformed authentication headers
   - Solutions:
     * Regenerate API key from PassInfo dashboard
     * Verify credentials using test endpoints
     * Check API key permissions and scope

2. Rate Limiting
   - Implement proper request throttling
   - Add delay between bulk message requests
   - Monitor your API usage
   - Common scenarios:
     * Too many requests in a short time period
     * Exceeding daily/monthly message quota
     * Concurrent request limits reached
   - Best practices:
     * Implement exponential backoff
     * Use batch processing for large volumes
     * Monitor rate limit headers in responses

3. Message Delivery Issues
   - Verify recipient phone numbers are properly formatted
   - Check sender name restrictions
   - Monitor delivery status responses
   - Common problems:
     * Invalid phone number format
     * Recipient opt-out or blocking
     * Network carrier restrictions
   - Troubleshooting steps:
     * Validate phone numbers before sending
     * Check delivery status regularly
     * Review error codes and descriptions

4. API Connectivity
   - Network connectivity problems
   - DNS resolution issues
   - SSL/TLS certificate validation
   - Resolution steps:
     * Verify network connectivity
     * Check DNS settings
     * Ensure proper SSL certificate handling
     * Test with API status endpoints

5. Request Timeout Issues
   - Long-running bulk operations
   - Network latency problems
   - Server processing delays
   - Recommendations:
     * Set appropriate timeout values
     * Break large requests into smaller batches
     * Implement retry mechanisms

6. Data Validation Errors
   - Invalid message format
   - Incorrect parameter types
   - Missing required fields
   - Solutions:
     * Validate data before sending
     * Check API documentation for requirements
     * Use SDK validation methods

### Debugging Tips

1. Enable Debug Logging
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. Test with Minimal Example
   ```python
   # Simple test to verify connectivity
   try:
       response = client.send_message(
           message="Test message",
           contact="1234567890",
           sender_name="Test"
       )
       print(f"Success: {response}")
   except PassInfoAPIError as e:
       print(f"Error: {e}")
   ```

3. Check Response Headers
   - Monitor rate limit information
   - Track request IDs for support
   - Verify API versions

4. Use Status Endpoints
   ```python
   # Check API status
   try:
       status = client.get_message_status("message_id")
       print(f"Message status: {status}")
   except PassInfoAPIError as e:
       print(f"Status check failed: {e}")
   ```
