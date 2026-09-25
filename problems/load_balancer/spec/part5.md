--------------------------------------------------------------------
PART 5 - Shutdown
--------------------------------------------------------------------
Servers get taken out of service for deploys. Everything from Parts 1-4
still applies and must still pass.

  SHUTDOWN <serverIndex>

RULES
  The server is taken out of service permanently. It never accepts another
  connection, and it is never chosen by load-based routing or by stickiness.

  Every connection currently on that server is evicted and then re-routed,
  one at a time, using ALL the rules from Parts 1-4.

  Re-routing order: the evicted connections are re-routed in the order they
  originally connected, oldest first.

  A re-routed connection is placed like any other connection - it prints a
  ROUTED line for its new server, or a REJECTED line if it cannot be placed
  anywhere, in which case it is dropped.

  All evictions happen before any re-routing begins: a connection is never
  considered "currently connected" on a server that has been shut down.

  SHUTDOWN of a server that is already out of service is ignored entirely.

OUTPUT
  Unchanged, except that in the final LOADS line a server that is out of
  service is reported as a single dash instead of a number:

      LOADS 3 - 1

EXAMPLE
  input                    output
  3                        ROUTED c1 0
  10 10 10                 ROUTED c2 1
  5                        ROUTED c3 0
  CONNECT c1 objA          ROUTED c1 2
  CONNECT c2 objB          ROUTED c3 2
  CONNECT c3 objA          ROUTED c4 1
  SHUTDOWN 0               LOADS - 2 2
  CONNECT c4 objC

  c1 and c3 are both on server 0. Shutting it down evicts both, oldest first.
  c1 re-routes by load: server 1 has load 1, server 2 has load 0, so it goes
  to server 2. c3 then sticks to objA's new server, 2. c4 routes by load to
  server 1.
