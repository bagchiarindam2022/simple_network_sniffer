import scapy.all as scapy


def packet_handler(packet):
    print("\n[Packet Detected]")
    try:
        if packet.haslayer(scapy.IP):
            print(f"Source: {packet[scapy.IP].src}")
            print(f"Destination: {packet[scapy.IP].dst}")
            print(f"Protocol: {packet.proto}")
            if packet.haslayer(scapy.TCP):
                print(f"Source Port: {packet[scapy.TCP].sport}")
                print(f"Destination Port: {packet[scapy.TCP].dport}")
            elif packet.haslayer(scapy.UDP):
                print(f"Source Port: {packet[scapy.UDP].sport}")
                print(f"Destination Port: {packet[scapy.UDP].dport}")
            else:
                print("Other Protocol: Non-TCP/UDP Packet")
        else:
            print("Not an IP Packet")
    except Exception as e:
        print(f"Error handling packet: {e}")
    print("_____________________________")


def start_sniffing(interface):
    print(f"[*] Sniffing packets on {interface}...")
    try:
      
        scapy.sniff(iface=interface, store=0, prn=packet_handler)
    except Exception as e:
        print(f"Error sniffing on {interface}: {e}")

# Ask for the network interface to listen on
interface = input("Enter the network interface (e.g., Wi-Fi, Ethernet): ")
start_sniffing(interface)
