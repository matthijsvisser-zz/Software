#include <cstdio>
#include "XbeeCom.h"


int main(void) {
  XBee_communication xbee;
  XBee_packet packet;
  packet.command = 0x21;
  packet.length = 0x55;
  packet.checksum = 0x99;

  unsigned char command;

  for(int i = 0; i < 1; i++) {
    printf("H: %d, T: %d\n", xbee.RxHead, xbee.RxTail);
    xbee.saveRxPacket(&packet);
  }

  printf("NOW H: %d, T: %d\n", xbee.RxHead, xbee.RxTail);


  XBee_packet *RxPacket;
  RxPacket = xbee.getRxPacket();
  printf("0x%x\n", RxPacket->command);

  // xbee.saveRxPacket(&packet);
  // XBee_packet *RxPacket;
  // RxPacket = xbee.getRxPacket();
  // unsigned char command = RxPacket->length;

  //("Command: %d\n", command);
}
