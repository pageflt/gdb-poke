# gdb-poke

This utility encapsulates arbitrary data into GDB remote protocol packets and
transmits them to a remote GDB server instance. Unless otherwise specified, the
packets are sent to `localhost:1234`.

# Usage
```
$ ./gdb-poke DATA [HOST:PORT]
```
