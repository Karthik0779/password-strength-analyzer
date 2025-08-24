from password_tool import analyzer, wordlist

# Test password analysis
result = analyzer.analyze_password("P@ssw0rd123!", user_inputs=["karthik", "2025"])
print("Password Analysis:", result)

# Test wordlist generation
wl = wordlist.generate_wordlist(["karthik", "project"], max_items=10)
print("\nGenerated Wordlist (first 10):", wl)
