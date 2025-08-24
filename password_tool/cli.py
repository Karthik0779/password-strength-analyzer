import argparse
import getpass
import json
from password_tool import analyzer, wordlist

# For colored output
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Dummy:
        def __getattr__(self, item): return ""
    Fore = Style = Dummy()

def print_strength(strength: str):
    """Return colored strength text."""
    if strength in ["Very Weak", "Weak"]:
        return Fore.RED + strength + Style.RESET_ALL
    elif strength in ["Fair"]:
        return Fore.YELLOW + strength + Style.RESET_ALL
    elif strength in ["Strong", "Very Strong"]:
        return Fore.GREEN + strength + Style.RESET_ALL
    return strength

def suggest_improvements(result):
    """Suggest improvements based on analysis issues."""
    suggestions = []
    if "Too short" in result["issues"]:
        suggestions.append("Use at least 12 characters.")
    if "Contains sequence" in result["issues"]:
        suggestions.append("Avoid predictable sequences like 1234 or abcd.")
    if "Contains repetition" in result["issues"]:
        suggestions.append("Avoid repeating characters (aaa, !!!).")
    if "Common password" in result["issues"]:
        suggestions.append("Don’t use common passwords.")
    if result["classification"] in ["Very Weak", "Weak"]:
        suggestions.append("Mix uppercase, lowercase, numbers, and symbols.")
    return suggestions

def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Analyzer & Wordlist Generator"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Analyze command ---
    analyze_parser = subparsers.add_parser("analyze", help="Analyze password strength")
    analyze_parser.add_argument("-p", "--password", help="Password string (use with caution)")
    analyze_parser.add_argument("--stdin", action="store_true", help="Read password securely from input")
    analyze_parser.add_argument("--user-inputs", nargs="*", default=[], help="Personal info to check against")
    analyze_parser.add_argument("--detailed", action="store_true", help="Show detailed analysis")
    analyze_parser.add_argument("--json", help="Save results as JSON file")

    # --- Wordlist command ---
    wordlist_parser = subparsers.add_parser("wordlist", help="Generate custom wordlist")
    wordlist_parser.add_argument("--seeds", nargs="+", required=True, help="Seed words (names, dates, etc.)")
    wordlist_parser.add_argument("--max", type=int, default=20, help="Max number of items in wordlist")
    wordlist_parser.add_argument("-o", "--output", help="Save wordlist to a file (e.g., wordlist.txt)")

    args = parser.parse_args()

    if args.command == "analyze":
        if args.password:
            pwd = args.password
        elif args.stdin:
            pwd = getpass.getpass("Enter password: ")
        else:
            print("❌ Please provide a password with -p or use --stdin")
            return

        result = analyzer.analyze_password(pwd, user_inputs=args.user_inputs)

        print("\nPassword Analysis Result:")
        print(f"  Password: {result['password']}")
        print(f"  Length: {result['length']}")
        print(f"  Entropy: {result['entropy_bits']} bits")
        print(f"  Strength: {print_strength(result['classification'])}")

        if result['issues']:
            print(f"  Issues: {', '.join(result['issues'])}")
        else:
            print("  Issues: None ✅")

        # Show suggestions
        suggestions = suggest_improvements(result)
        if suggestions:
            print("\nSuggestions:")
            for s in suggestions:
                print("  - " + s)

        # Detailed mode
        if args.detailed:
            print("\nDetailed Report:")
            print(f"  Contains Uppercase: {any(c.isupper() for c in pwd)}")
            print(f"  Contains Lowercase: {any(c.islower() for c in pwd)}")
            print(f"  Contains Digits: {any(c.isdigit() for c in pwd)}")
            print(f"  Contains Special: {any(not c.isalnum() for c in pwd)}")

        # Export JSON
        if args.json:
            with open(args.json, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4)
            print(f"\n✅ Results saved to {args.json}")

    elif args.command == "wordlist":
        wl = wordlist.generate_wordlist(args.seeds, max_items=args.max)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                for w in wl:
                    f.write(w + "\n")
            print(f"\n✅ Wordlist saved to {args.output} with {len(wl)} entries.")
        else:
            print("\nGenerated Wordlist:")
            for w in wl:
                print(w)

if __name__ == "__main__":
    main()
