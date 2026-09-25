--------------------------------------------------------------------
PART 4 - Capacity
--------------------------------------------------------------------
Line 2 of the input now matters. Everything from Parts 1-3 still applies
and must still pass.

RULES
  A server whose load equals its capacity is FULL and cannot accept another
  connection.

    - When routing by load, only consider servers that are not full. Among
      those, smallest load wins, then smallest index.
    - Stickiness does NOT override capacity. If an objectId's sticky server
      is full, the connection is REJECTED - it is not sent anywhere else.
    - If a connection cannot be placed, it is REJECTED. It does not occupy
      any server and it is not remembered.

  A capacity may be 0, meaning that server can never accept a connection.

OUTPUT
  For every connection that cannot be placed, print, in event order:

      REJECTED <connectionId>

  These lines are interleaved with the ROUTED lines in event order. LOADS is
  unchanged.

EXAMPLE
  input                    output
  2                        ROUTED c1 0
  1 2                      ROUTED c2 1
  5                        REJECTED c3
  CONNECT c1 objA          ROUTED c4 1
  CONNECT c2 objB          REJECTED c5
  CONNECT c3 objA          LOADS 1 2
  CONNECT c4 objB
  CONNECT c5 objC
