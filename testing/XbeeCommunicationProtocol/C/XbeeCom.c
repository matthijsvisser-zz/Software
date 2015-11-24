unsigned char processSerialData(char *data, unsigned char length) {

  for(unsigned char i = 0; i < length; i++) {

    if(RxPacketState == 0) {
      if(data[i] == 0x5A) {
        RxPacketState = 1;
      }
    } else if(RxPacketState == 1) {
      if(data[i] == 0x3C) {
        RxPacketState = 2;
      } else {
        RxPacketState = 0;
      }
    } else if(RxPacketState == 2) {
      if(data[i] == 0x42) {
        RxPacketState = 3;
      } else {
        RxPacketState = 0;
      }
    } else if(RxPacketState == 3) {
      if(data[i] == 0x99) {
        RxPacketState = 4;
      } else {
        RxPacketState = 0;
      }
    } else if(RxPacketState == 4) {
      unsigned char length = data[i];
      unsigned char checksum = 0;
      checksum |= length;
      RxPacketState = 5;
    } else if(RxPacketState == 5) {
      unsigned char command = data[i]
      char buffer[length];
      unsigned char dataIndex = 0
      checksum |= command;
      RxPacketState = 6;
    } else if(RxPacketState == 6) {
      buffer[dataIndex++] = data[i];
      checksum |= data[i];
      if(dataIndex > length)
        RxPacketState = 7;
    } else if(RxPacketState == 7) {

    }

  }

}
