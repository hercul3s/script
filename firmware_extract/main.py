import os, sys
import binwalk
from binascii import hexlify, unhexlify




if __name__ == '__main__':
    nargs = len(sys.argv)

    if nargs != 3:
        print("please give file ")
                                    
    else:
        f = open(sys.argv[1], "rb")
        f.seek(92)
        lzma_header = f.read(5)
        uncompressed_size = '\x00\x00\x00\x10\x00\x00\x00\x00'
        data = f.read()

        output = open(sys.argv[2], 'wb')

        output.write(lzma_header + uncompressed_size.encode('ascii') + data)

        f.close()

        print("Success...")
        print("Scanning",sys.argv[2])
        
        #new_input = open(sys.argv[2], 'rb')

        #for module in binwalk.scan('output.bin', signature=True, quiet=True):

        for module in binwalk.scan(sys.argv[2], signature=True):
        
            print("%s Results:" % module.name)

            print("%s Module:" % module.results)











