#include <cstdio>
#include "XbeeCom.h"

int main(void) {
  XBee_communication xbee;
  XBee_packet packet;
  packet.command = 0x21;
  packet.length = 0x55;
  packet.checksum = 0x99;

  unsigned char command;
printf("Packets : %d\n", xbee.RxPacketsAvailable());
  for(int i = 0; i < 40; i++) {
    printf("H: %d, T: %d\n", xbee.RxHead, xbee.RxTail);
    packet.command = packet.command + 1;
    xbee.saveRxPacket(&packet);
  }

  printf("NOW H: %d, T: %d\n", xbee.RxHead, xbee.RxTail);

  printf("Packets : %d\n", xbee.RxPacketsAvailable());

  XBee_packet *RxPacket;
  for(int i = 0; i < 4; i++) {
    RxPacket = xbee.getRxPacket();
    printf("command: %x\n", RxPacket->command);
  }
}
