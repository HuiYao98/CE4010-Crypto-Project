from e2e.server import *
from certAuthority import *

# server private key
server_private_key = generate_private_key("server-private-key.pem", "password")
# server generate csr
generate_csr(
    server_private_key,
    filename="server-csr.pem",
    country="US",
    state="Maryland",
    locality="Baltimore",
    org="My Company",
    alt_names=["localhost", "https://127.0.0.1:5000", "121.0.0.1", "121.0.0.1:5000"],
    hostname="127.0.0.1",
)

# generate private and public key
private_key = generate_private_key("ca-private-key.pem", "password")
generate_public_key(
    private_key,
    filename="ca-public-key.pem",
    country="SG",
    state="SG",
    locality="NTU",
    org="Intro to Cryptography",
    hostname="google.com",
)

# Begin by loading your CSR:
# Opening server-csr.pem file
csr_file = open("server-csr.pem", "rb")
# Create csr object
csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())

# Load CA public key
# opening ca-public-key.pem
ca_public_key_file = open("ca-public-key.pem", "rb")
# Create CA public key object
ca_public_key = x509.load_pem_x509_certificate(
    ca_public_key_file.read(), default_backend()
)

# load CA private key
from getpass import getpass

# reading ca-private-key.pem
ca_private_key_file = open("ca-private-key.pem", "rb")
# create CA private key object - private key was encrpted using password specifed
ca_private_key = serialization.load_pem_private_key(
    ca_private_key_file.read(),
    getpass().encode("utf-8"),
    default_backend(),
)

# sign csr and generate public key
sign_csr(csr, ca_public_key, ca_private_key, "server-public-key.pem")
