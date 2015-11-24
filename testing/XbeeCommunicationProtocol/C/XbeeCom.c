#include "XbeeCom.h"

class XBee_packet {
  public:
    unsigned char command;
    unsigned char length;
    char *data;
    unsigned char checksum;
}

XBee_packet::XBee_packet() {
  command, length, checksum = 0;
}

XBee_packet::initBuffer(unsigned char length) {
  data = malloc(sizeof(char) * length);
}

class XBee_communication {
  public:
    // List of packets
    XBee_packet *RxPackets;
    XBee_packet *TxPackets;

    // Temporary packet being received or transmitted
    XBee_packet RxPacket;
    XBee_packet TxPacket;
    unsigned char RxState;
    unsigned char RxChecksum;
    unsigned char RxDataCount;

}

XBee_communication::XBee_communication() {
  RxState, RxChecksum, RxDataCount = 0;
}

XBee_communication::processSerialData(char *data, unsigned char length) {
  unsigned char countNewPackets = 0;

  for(unsigned char i = 0; i < length; i++) {
    char c = data[i];

    if(RxState == 0) {
      if (c == PACKET_START_BYTE_1) {
        RxState = 1;
      } else {
        RxState = 0;
      }
    } else if(RxState == 1) {
      if(c == PACKET_START_BYTE_2) {
        RxState = 2;
      } else {
        RxState = 0;
      }
    } else if(RxState == 2) {
      if(c == PACKET_START_BYTE_3) {
        RxState = 3;
      } else {
        RxState = 0;
      }
    } else if(RxState == 3) {
      if(c == PACKET_START_BYTE_4) {
        RxState = 4;
      } else {
        RxState = 0;
      }
    } else if(RxState == 4) {
      RxPacket.length = c;
      RxChecksum |= c;
      RxState = 5;
    } else if(RxState == 5) {
      RxPacket.command = c;
      RxChecksum |= c;

      // Initialize packet buffer to receive data
      RxPacket.initBuffer(RxPacket.length);

      RxState = 6;
    } else if(RxState == 6) {
      if(RxDataCount < RxPacket.length) {
        RxPacket.data[RxDataCount++] = c;
        RxChecksum |= c;
      }
      if(RxDataCount >= RxPacket.length){
        RxState = 7;
      }
    } else if(RxState == 7) {
      RxPacket.checksum = c;

      if(RxPacket.checksum == RxChecksum) {
        countNewPackets++;
      }

      RxState, RxChecksum, RxDataCount = 0;

    }

  }

  return countNewPackets;
}
