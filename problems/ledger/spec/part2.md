--------------------------------------------------------------------
PART 2 - Transfers
--------------------------------------------------------------------
A new transaction type is added. Everything from Part 1 still applies
and must still pass.

  <txnId> TRANSFER <fromUserId> <toUserId> <amount>

RULES
  If fromUserId's current balance is greater than or equal to amount,
  subtract amount from fromUserId and add amount to toUserId.
  Otherwise the transaction is REJECTED and nothing changes - no money
  moves and toUserId is not created.

  fromUserId and toUserId may be the same user.

OUTPUT
  Unchanged from Part 1.

EXAMPLE
  input                            output
  4                                alice 600
  t1 DEPOSIT alice 1000            bob 400
  t2 TRANSFER alice bob 400        REJECTED t3
  t3 TRANSFER carol alice 50
  t4 TRANSFER bob bob 400
