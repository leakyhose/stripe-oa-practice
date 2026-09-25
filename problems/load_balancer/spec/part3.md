--------------------------------------------------------------------
PART 3 - Stickiness
--------------------------------------------------------------------
Connections that share an objectId need to land on the same server, so that
the server can hold that object's state in memory. Everything from Parts 1
and 2 still applies and must still pass.

RULES
  When routing a CONNECT, first check whether any CURRENTLY CONNECTED
  connection has the same objectId.

    - If one does, route this connection to that same server, even if it
      is not the least loaded server.
    - If none does, fall back to the Part 1 rule: smallest load, then
      smallest index.

  "Currently connected" means exactly that: once every connection for an
  objectId has disconnected, that objectId has no sticky server any more
  and the next CONNECT for it is routed by load again.

OUTPUT
  Unchanged.

EXAMPLE
  input                    output
  3                        ROUTED c1 0
  10 10 10                 ROUTED c2 1
  7                        ROUTED c3 0
  CONNECT c1 objA          ROUTED c4 2
  CONNECT c2 objB          ROUTED c5 0
  CONNECT c3 objA          LOADS 1 1 1
  CONNECT c4 objC
  DISCONNECT c1
  DISCONNECT c3
  CONNECT c5 objA

  c3 sticks to objA's server 0 even though server 2 is emptier. After both
  objA connections drop, objA has no sticky server, so c5 is routed by load
  and lands on server 0 because it is empty again and has the lowest index.
