--------------------------------------------------------------------
PART 3 - Reversals
--------------------------------------------------------------------
Disputes happen. A new transaction type undoes an earlier one.
Everything from Parts 1 and 2 still applies and must still pass.

  <txnId> REVERSE <targetTxnId>

RULES
  A REVERSE is APPLIED only if targetTxnId refers to an earlier
  transaction that:
    - is a DEPOSIT, WITHDRAW, or TRANSFER (never a REVERSE), AND
    - was itself applied (not rejected), AND
    - has not already been reversed.
  Otherwise the REVERSE is REJECTED.

  Applying a REVERSE undoes the exact balance effect of the target:
    DEPOSIT  -> subtract amount from the user
    WITHDRAW -> add amount back to the user
    TRANSFER -> move amount from toUserId back to fromUserId

  A reversal is ALWAYS applied when the conditions above hold, even if
  it drives a balance below zero. Balances may be negative.

  A rejected REVERSE is listed in the REJECTED line like any other
  rejected transaction.

OUTPUT
  Unchanged. Note that negative balances are non-zero and so they are
  printed, formatted like -250.

EXAMPLE
  input                            output
  6                                alice 1400
  t1 DEPOSIT alice 1000            bob -400
  t2 DEPOSIT bob 400               REJECTED t5 t6
  t3 TRANSFER bob alice 400
  t4 REVERSE t2
  t5 REVERSE t99
  t6 REVERSE t4
