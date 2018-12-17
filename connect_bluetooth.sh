#!/bin/bash
bluetoothctl << EOF
disconnect
connect 88:C6:26:1E:72:22
EOF
