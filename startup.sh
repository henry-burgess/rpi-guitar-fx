#! /bin/sh

# Start JACK
pkill jackd
pkill guitarix

/usr/bin/jackd -dalsa -dhw:ATR2xUSB,0 -r192000 -p512 -n2 &

# Start guitarix
guitarix
