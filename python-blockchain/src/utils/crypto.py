def hash_data(data):
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()

def sign_data(private_key, data):
    from cryptography.hazmat.primitives.asymmetric import signing
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend

    private_key = serialization.load_pem_private_key(
        private_key.encode(),
        password=None,
        backend=default_backend()
    )
    signature = private_key.sign(
        data.encode(),
        signing.Prehashed(hashlib.sha256())
    )
    return signature

def verify_signature(public_key, data, signature):
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend

    public_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )
    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PKCS1v15(),
            hashlib.sha256()
        )
        return True
    except Exception:
        return False