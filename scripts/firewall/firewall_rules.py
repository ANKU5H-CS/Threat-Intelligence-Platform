import os

print("=" * 40)
print(" Threat Intelligence Platform ")
print(" Firewall Rule Verification ")
print("=" * 40)

os.system("sudo iptables -L")

print("\nFirewall rule verification completed.")
