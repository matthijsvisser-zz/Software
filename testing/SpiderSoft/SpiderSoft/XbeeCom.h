#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PACKET_START_BYTE_1 0x5A
#define PACKET_START_BYTE_2 0x3C
#define PACKET_START_BYTE_3 0x42
#define PACKET_START_BYTE_4 0x99

#define MAX_PACKETS_TX 10
#define MAX_PACKETS_RX 10

typedef struct XBee_packet {
    unsigned char command;
    unsigned char length;
    char data[10]; // maximum 10 bytes of data
    unsigned char checksum;
} XBee_packet;

class XBee_communication {
  public:
    // List of Rxpackets
    XBee_packet *RxPackets;
    unsigned char RxTail;
    unsigned char RxHead;

    // List of Txpackets
    XBee_packet *TxPackets;
    unsigned char TxTail;
    unsigned char TxHead;

    // Temporary packet being received or transmitted
    XBee_packet RxPacket;
    XBee_packet TxPacket;
    unsigned char RxState;
    unsigned char RxChecksum;
    unsigned char RxDataCount;

    XBee_communication(void);
    unsigned char RxPacketsAvailable(void);
    XBee_packet *getRxPacket(void);
    void saveRxPacket(XBee_packet *packet);
    unsigned char processSerialData(char *data, unsigned char length);

};
