from os import system
from psycopg2 import connect, ProgrammingError, OperationalError, InternalError

from app.api.settings import config
from app.api.uuid import generate_uuid, generate_host


def connection():
    try:
        conn = connect(
            host=config["db_config"]["host"],
            dbname=config["db_config"]["dbname"],
            user=config["db_config"]["user"],
            password=config["db_config"]["password"])
        return conn
    except OperationalError as e:
        start_psql()
        return connection()


def start_psql():
    system("sudo service postgresql start")


def psql_command(conn, command, values=None, fetch=True, fetchall=False):
    if not command.endswith(';'):
        command += ';'
    cur = conn.cursor()
    try:
        if values:
            cur.execute(command, values)
        else:
            cur.execute(command)
        if fetch:
            if fetchall:
                response = cur.fetchall()
            else:
                response = cur.fetchone()
        else:
            response = None
    except (ProgrammingError, InternalError) as e:
        print(str(e))
        response = None
    conn.commit()
    cur.close()
    return response


def add_to_hosts_table(conn, hostname, detected_os):
    uuid = generate_uuid()
    response = psql_command(
        conn,
        "INSERT INTO public.hosts(uuid, hostname, detected_os) VALUES(%s, %s, %s) returning *;",
        values=(uuid, hostname, detected_os))
    return response


def get_host_table(conn, uuid):
    table = psql_command(
        conn, "SELECT * FROM %s LIMIT 100;" % uuid, fetchall=True)
    return table


def create_host_table(conn, uuid, open_ports, exploit_status, other):
    table = psql_command(
        conn,
        "CREATE TABLE %s (id SERIAL PRIMARY KEY, type VARCHAR(255) NOT NULL, value VARCHAR(255) NOT NULL, state BOOLEAN NOT NULL);"
        % uuid,
        fetch=False)
    if open_ports:
        add_open_ports(conn, uuid, open_ports)
    if exploit_status:
        add_exploit_status(conn, uuid, exploit_status)
    if other:
        for item in other.keys():
            add_info(conn, uuid, item, other[item], True)
    return get_host_table(conn, uuid)


def add_info(conn, uuid, type, value, state):
    psql_command(
        conn,
        "INSERT INTO " + uuid +
        " (type, value, state) VALUES(%s, %s, %s) returning *;",
        values=(type, value, state),
        fetch=False)


def add_open_ports(conn, uuid, open_ports):
    for port in open_ports:
        add_info(conn, uuid, 'port', port, True)


def add_exploit_status(conn, uuid, exploit_status):
    add_info(conn, uuid, 'exploit', exploit_status["exploit"],
             exploit_status["successful"])


def create_host(conn,
                hostname,
                detected_os,
                open_ports=[],
                exploit_status={},
                other=[]):
    if not hostname:
        hostname = generate_host()
    host = add_to_hosts_table(conn, hostname, detected_os)
    uuid = host[1]
    table = create_host_table(conn, uuid, open_ports, exploit_status, other)
    return (host, table)
