import hmac
import hashlib
import base64

def create_secure_signing_helper(secret_key, timestamp, message):
    """
    Create secure signing helper for iOS (Swift) using HMAC-SHA256.
    
    Args:
    secret_key (str): Secret key for HMAC-SHA256.
    timestamp (int): Timestamp in seconds.
    message (str): Message to be signed.
    
    Returns:
    str: Signed message.
    """
    
    # Create HMAC object with secret key and SHA256 hash function
    hmac_object = hmac.new(secret_key.encode(), digestmod=hashlib.sha256)
    
    # Update HMAC object with timestamp and message
    hmac_object.update(str(timestamp).encode())
    hmac_object.update(message.encode())
    
    # Get digest of HMAC object
    digest = hmac_object.digest()
    
    # Encode digest to base64
    encoded_digest = base64.b64encode(digest)
    
    # Return signed message
    return encoded_digest.decode()

# Example usage
secret_key = "your_secret_key_here"
timestamp = 1643723400
message = "your_message_here"

signed_message = create_secure_signing_helper(secret_key, timestamp, message)
print(signed_message)
```

Kodni ishlatish uchun, `secret_key`, `timestamp` va `message` o'rniga sizga kerakli ma'lumotlarni kiritishingiz kerak.
