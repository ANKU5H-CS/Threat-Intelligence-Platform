import subprocess

print("=" * 50)
print("Threat Intelligence Platform")
print("Firewall Monitoring Module")
print("=" * 50)

try:
    result = subprocess.run(
        ["sudo", "iptables", "-L"],
        capture_output=True,
        text=True
    )

    print("\nCurrent Firewall Status:\n")
    print(result.stdout)

except Exception as e:
    print("Error:", e)
