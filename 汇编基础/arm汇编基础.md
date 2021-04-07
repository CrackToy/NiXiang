### arm64手册

https://courses.cs.washington.edu/courses/cse469/18wi/Materials/arm64.pdf

一些arm64topy的理解

```python
# -*- coding: utf-8 -*-

class ARM:

    def BFI(self, rd, rn, lsb, width):
        rd = (rd & (~(((0xFFFFFFFF >> (32 - width))) << lsb))) | ((rn & ((0xFFFFFFFF >> (32 - width)))) << lsb)
        return rd

    def MVN(self, rn):
        return ~rn & 0xffffffff

    def BIC(self, rd, rn):
        return rd & ~rn

    def ORR(self, rd, rn):
        return rd | rn

    def ORN(self, rd, op):
        return rd | ~op

    def EOR(self, rd, rn):
        return rd ^ rn

    def EON(self, rd, rn):
        return rd ^ ~rn

    def ADD(self, rd, rn):
        return rd + rn

    def SUB(self, rd, rn):
        return rd - rn


    def LSR(self, rd, num):
        return rd >> num

    def LSL(self, rd, num):
        return rd << num

```

