# ═══════════════════════════════════════════════
# Mini Project: Bank Account Summary Generator
# Uses: variables, types, casting, methods, f-str
# ═══════════════════════════════════════════════

# ── 1. Variables with good naming ──────────────
account_holder = "  ravi kumar  "   # messy input
account_number = "SBI00987654"
opening_balance_str = "50000"        # from file (string!)
INTEREST_RATE   = 0.065             # constant: 6.5% p.a.

# ── 2. Type casting & string methods ───────────
clean_name    = account_holder.strip().title()   # 'Ravi Kumar'
balance       = float(opening_balance_str)       # 50000.0
account_short = account_number[-4:]              # last 4 digits

# ── 3. Calculations ─────────────────────────────
interest      = balance * INTEREST_RATE
new_balance   = balance + interest
is_premium    = new_balance >= 50000

# ── 4. f-String report ──────────────────────────
report = f"""
╔══════════════════════════════════════════╗
║        ANNUAL ACCOUNT STATEMENT          ║
╠══════════════════════════════════════════╣
║ Account Holder : {clean_name:<22} ║
║ Account No     : XXXX-XXXX-{account_short:<14} ║
║ Account Type   : {'Premium' if is_premium else 'Regular':<22} ║
╠══════════════════════════════════════════╣
║ Opening Balance: ₹{balance:>20,.2f}   ║
║ Interest ({INTEREST_RATE:.1%})  : ₹{interest:>20,.2f}   ║
║ Closing Balance: ₹{new_balance:>20,.2f}   ║
╚══════════════════════════════════════════╝"""

print(report)
