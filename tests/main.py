from app.api.database import connection, create_host


def test():
    print("Trying to create host")
    conn = connection()
    #hostname = "Test"
    hostname = None
    detected_os = "Windows 7"
    open_ports = [21, 80, 443]
    exploit_status = {"exploit": "CVE-2018-1", "successful": True}
    (host, table) = create_host(
        conn,
        hostname,
        detected_os,
        open_ports=open_ports,
        exploit_status=exploit_status)
    print(host)
    print(table)
