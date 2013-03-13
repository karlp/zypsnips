#!/usr/bin/env python
# Source: http://paste.jvnv.net/raw/XdBz7
# zyp, March 2013
# Used for dumping tracewswo output via BMP

import usb1, libusb1
import time, struct

ctx = usb1.LibUSBContext()

dev = ctx.getByVendorIDAndProductID(0x1d50, 0x6018)

if not dev:
	print 'Device not found.'
	exit(1)

handle = dev.open()
handle.claimInterface(5)

def transfer_cb(t):
	print t.getBuffer()[:t.getActualLength()].encode('hex')
	
	return True

th = usb1.USBTransferHelper()
th.setEventCallback(libusb1.LIBUSB_TRANSFER_COMPLETED, transfer_cb)

t = handle.getTransfer()
t.setBulk(0x85, 64, th)
t.submit()

while 1:
	ctx.handleEvents()
