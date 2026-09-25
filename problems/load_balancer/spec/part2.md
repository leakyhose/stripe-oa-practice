--------------------------------------------------------------------
PART 2 - Disconnect
--------------------------------------------------------------------
Connections do not last forever. Everything from Part 1 still applies and
must still pass.

  DISCONNECT <connectionId>

RULES
  The connection leaves the server it was on, freeing one unit of load.
  If connectionId is not currently connected - it was never seen, or it
  already disconnected - the event is ignored entirely. It produces no
  output and changes nothing.
  DISCONNECT never produces an output line, even when it succeeds.

OUTPUT
  Unchanged. Note that LOADS reports the load at the END of the event
  stream, so disconnects must be fully reflected there.

EXAMPLE
  input                    output
  2                        ROUTED c1 0
  10 10                    ROUTED c2 1
  6                        ROUTED c3 0
  CONNECT c1 objA          LOADS 1 1
  CONNECT c2 objB
  DISCONNECT c1
  CONNECT c3 objC
  DISCONNECT c9
  DISCONNECT c1
