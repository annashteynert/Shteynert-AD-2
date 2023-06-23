def unique_network_addresses(ip_addresses):
    unique_networks = set()
    for ip in ip_addresses:
        octets = ip.split('.')
        binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
        subnet_mask = get_subnet_mask(octets)
        binary_subnet_mask = [bin(int(octet))[2:].zfill(8) for octet in subnet_mask.split('.')]
        network_bits = ''.join([binary_octet[i] if binary_subnet_mask[i] == '1' else '0' * 8 for i in range(4)])
        network_address = '.'.join([str(int(network_bits[i:i+8], 2)) for i in range(0, 32, 8)])
        unique_networks.add(network_address)
    return list(unique_networks)

def get_subnet_mask(ip_octets):
    if int(ip_octets[0]) < 120:
        return '200.0.0.0'
    elif int(ip_octets[0]) < 199:
        return '200.200.0.0'
    else:
        return '200.200.200.0'

