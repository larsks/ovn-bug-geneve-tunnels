ovs-vsctl set open_vswitch .  \
  external_ids:ovn-remote=tcp:192.168.122.100:6642 \
  external_ids:ovn-encap-ip=$(ip addr show eth0 | awk '$1 == "inet" {print $2}' | cut -f1 -d/) \
  external_ids:ovn-encap-type=geneve \
  external_ids:system-id=$(hostname)
