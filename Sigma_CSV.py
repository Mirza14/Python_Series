import yaml
import csv

def yaml_to_csv(yaml_file, csv_file):
  """
  Reads data from a YAML file and writes it to a CSV file.

  Args:
      yaml_file: Path to the YAML file.
      csv_file: Path to the output CSV file.
  """
  # Open the YAML file and load the data
  with open(yaml_file, 'r') as f:
    data = yaml.safe_load(f)

# title: Disable Microsoft Defender Firewall via Registry
# id: 974515da-6cc5-4c95-ae65-f97f9150ec7f
# status: test
# description: Adversaries may disable or modify system firewalls in order to bypass controls limiting network usage
# references:
#     - https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004.md#atomic-test-2---disable-microsoft-defender-firewall-via-registry
# author: frack113
# date: 2022/01/09
# modified: 2024/03/25
# tags:
#     - attack.defense_evasion
#     - attack.t1562.004
# logsource:
#     category: registry_set
#     product: windows
# detection:
#     selection:
#         # HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\EnableFirewall
#         # HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile\EnableFirewall
#         # HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\EnableFirewall
#         TargetObject|contains: '\Services\SharedAccess\Parameters\FirewallPolicy\'
#         TargetObject|endswith: '\EnableFirewall'
#         Details: 'DWORD (0x00000000)'
#     condition: selection
# falsepositives:
#     - Unknown
# level: medium

  # Extract relevant data based on the YAML structure
  rows_to_write = []
  for server in data:
    row = [server['title'], server['status'], server['level']]
    rows_to_write.append(row)

  # Open the CSV file for writing
  with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header row
    csv_writer.writerow(['Rule Title', 'Rule Status', 'Rule Level'])
    # Write the data rows
    csv_writer.writerows(rows_to_write)


# Replace with your actual file paths
yaml_file = 'Users/mirzamansooralibaig/Desktop/Sigma_Repo/sigma/rules/windows/registry/registry_set/registry_set_disable_defender_firewall.yml'
csv_file = 'Users/mirzamansooralibaig/Desktop/Sigma_Repo/sigma/Sigma_Excel.csv'

yaml_to_csv(yaml_file, csv_file)

print(f"Data converted from YAML to CSV. Output file: {csv_file}")
