
//
//  XbeeCom.h
//  XbeeComTest
//
//  Created by Sander van Doesburg on 12/01/16.
//  Copyright (c) 2016 Sander van Doesburg. All rights reserved.
//

#ifndef __XbeeComTest__XbeeCom__
#define __XbeeComTest__XbeeCom__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PACKET_START_BYTE_1 0x5A
#define PACKET_START_BYTE_2 0x3C
#define PACKET_START_BYTE_3 0x42
#define PACKET_START_BYTE_4 0x99

#define MAX_PACKETS_TX 10
#define MAX_PACKETS_RX 10
#define MAX_DATA_SIZE 64

typedef struct XBee_packet {
	unsigned char command;
	unsigned char length;
	char data[MAX_DATA_SIZE]; // maximum 10 bytes of data
	unsigned char checksum;
} XBee_packet;


void XBee_communication_init(void);
unsigned char XBee_communication_RxPacketsAvailable(void);
XBee_packet *XBee_communication_getRxPacket(void);
void XBee_communication_saveRxPacket(XBee_packet *packet);
unsigned char XBee_communication_processSerialData(char *data, unsigned char length);

#endif /* defined(__XbeeComTest__XbeeCom__) */
