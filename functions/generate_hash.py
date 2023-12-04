import hashlib

def generate_md5_hash(ecgain, bidno, filename):
    input_string = f"{ecgain}{bidno}{filename}"

    input_bytes = input_string.encode("utf-8")

    # CREATE A MD5 HASH OBJECT
    md5_hash = hashlib.md5()

    # UPDATE THE HASH OBJECT WITH INPUT BYTES
    md5_hash.update(input_bytes)

    # GET THE HEXADECIMAL REPRESENTATION OF THE HASH
    hash = md5_hash.hexdigest()

    return hash