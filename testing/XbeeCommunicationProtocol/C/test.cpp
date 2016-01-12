#include <cstdio>
#include "XbeeCom.h"

int main(void) {
  XBee_communication xbee;

  char serialData[4] = {0x5A, 0x3C, 0x42, 0x99};
  char serialData2[12] = {0x01, 0x11, 0x20, 0x31, 0x5A, 0x3C, 0x42, 0x99, 0x01, 0x11, 0x20, 0x31};

  xbee.processSerialData(&serialData[0], 4);
  xbee.processSerialData(&serialData2[0], 12);

  printf("Packets : %d\n", xbee.RxPacketsAvailable());

  XBee_packet *RxPacket;
  unsigned char packetsNum = xbee.RxPacketsAvailable();
  for(int i = 0; i < packetsNum; i++) {
    RxPacket = xbee.getRxPacket();
    printf("command packet %d: %x\n",i,  RxPacket->command);
  }
}
