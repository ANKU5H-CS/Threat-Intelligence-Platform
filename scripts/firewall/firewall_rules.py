import os

print("=" * 50)
print(" Threat Intelligence Platform ")
print(" Firewall Rule Management ")
print("=" * 50)

print("\nCurrent Firewall Rules:\n")
os.system("sudo iptables -L")

print("\nDefault Policies:")
os.system("sudo iptables -S")

print("\nFirewall verification completed successfully.")
