--------------------------------------------------------------------
PART 1 - Routing
--------------------------------------------------------------------
You are building the connection load balancer that sits in front of a pool
of servers holding long-lived WebSocket connections.

INPUT (stdin)
  line 1:  N            the number of servers, indexed 0 .. N-1
  line 2:  N integers    the capacity of each server, in index order
  line 3:  M            the number of events
  next M lines:          the events, in the order they occurred

  Events in this part:

    CONNECT <connectionId> <objectId>

  connectionId and objectId are non-empty strings of letters and digits.
  connectionId is unique among the connections currently connected.

  For Part 1 the inputs are guaranteed never to reach a server's capacity,
  so you can ignore line 2 for now. It is in the input from the start
  because the format does not change in later parts.

RULES
  Route each CONNECT to the server with the smallest current load, where
  load is the number of connections currently on that server.
  If several servers tie for the smallest load, choose the one with the
  smallest index.
  Every server starts with a load of 0.

OUTPUT (stdout)
  One line for each connection you place, in the order it was placed:

      ROUTED <connectionId> <serverIndex>

  Then exactly one final line giving the load of every server, in index
  order, separated by single spaces:

      LOADS <load0> <load1> ... <loadN-1>

EXAMPLE
  input                    output
  3                        ROUTED c1 0
  10 10 10                 ROUTED c2 1
  5                        ROUTED c3 2
  CONNECT c1 objA          ROUTED c4 0
  CONNECT c2 objB          ROUTED c5 1
  CONNECT c3 objC          LOADS 2 2 1
  CONNECT c4 objD
  CONNECT c5 objE
