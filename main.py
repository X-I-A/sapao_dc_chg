import sys, base64, gzip

if __name__ == '__main__':

    nameo = sys.argv[1]
    named = sys.argv[2]

    # String is Base64 Encoded
    with open('origin.txt', 'rb') as fo:
        raw = fo.read()

    # raw_zip = Decoded ByteString
    raw_zip = bytearray(base64.b64decode(raw))[4:]

    # gzip_header to be kept
    zip_header = raw_zip[:10]

    # xml file
    raw_content = gzip.decompress(raw_zip)

    # replacement here
    result_content = raw_content.decode().replace(nameo, named).encode()

    # compress the data and append the sap AO accepted gzip header
    result_zip = gzip.compress(result_content, 6)
    result_zip = zip_header+bytearray(result_zip)[10:]

    # add AO accepted string header and base64 encoding
    result = base64.b64encode(len(result_content).to_bytes(4, "little") + result_zip)

    # generating output
    with open('result.txt', 'wb') as fw:
        fw.write(result)

    with open('debug_raw.txt', 'wb') as fw:
        fw.write(raw_content)

    with open('debug_result.txt', 'wb') as fw:
        fw.write(result_content)

    print("Please check result.txt to see if the transformation is successful")
