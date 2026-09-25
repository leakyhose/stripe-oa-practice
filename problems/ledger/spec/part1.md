--------------------------------------------------------------------
PART 1 - Balances
--------------------------------------------------------------------
You are building the ledger component of a payments system. It reads a
stream of transactions and reports the resulting account balances.

INPUT (stdin)
  The first line contains an integer N, the number of transactions.
  The next N lines each describe one transaction, in the order they
  occurred. Every transaction line begins with a unique transaction id.

  <txnId> DEPOSIT  <userId> <amount>
  <txnId> WITHDRAW <userId> <amount>

  amount is a non-negative integer number of cents.
  txnId and userId are non-empty strings of letters and digits.
  A userId is only known to the ledger once it appears in a transaction.

RULES
  DEPOSIT  adds amount to the user's balance.
  WITHDRAW subtracts amount from the user's balance, but ONLY if the
           user's current balance is greater than or equal to amount.
           Otherwise the transaction is REJECTED: it changes nothing.
  A user's balance starts at 0.

OUTPUT (stdout)
  First, one line for every user whose final balance is NOT zero, sorted
  lexicographically ascending by userId:

      <userId> <balance>

  Then exactly one more line listing the ids of every rejected
  transaction, in the order they appeared in the input:

      REJECTED <id1> <id2> ...

  If nothing was rejected, that line is exactly:

      REJECTED

EXAMPLE
  input                       output
  5                           alice 700
  t1 DEPOSIT alice 1000       bob 300
  t2 DEPOSIT bob 500          REJECTED t5
  t3 WITHDRAW alice 300
  t4 WITHDRAW bob 200
  t5 WITHDRAW bob 9999
