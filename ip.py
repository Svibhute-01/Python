
server_ip = ("192.168.1.100")  
allowed_ips = ["192.168.1.1", "192.168.1.10"]  

def update_allowed_ips(ip_list, new_ip):
    if new_ip not in ip_list:
        ip_list.append(new_ip)
        print(f"Added '{new_ip}' to allowed IPs.")
    else:
        print(f"'{new_ip}' is already allowed.")


def display_config(server_ip, allowed_ips):
    print("\n--- Server Configuration ---")
    print(f"Server IP (immutable): {server_ip}")
    print(f"Allowed IPs (mutable): {allowed_ips}")


display_config(server_ip, allowed_ips)

new_ip=str(input("Enter new ip to allow:"))
update_allowed_ips(allowed_ips,new_ip)
display_config(server_ip, allowed_ips)
