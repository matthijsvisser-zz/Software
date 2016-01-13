#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#define UART_BAUD_RATE 1000000
#define UART_BAUD_RATE_XBEE 115200

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdio.h>


#include "AX18ServoDriver.h"
#include "IOPorts_ATMega.h"
#include "uart.h"
#include "timer.h"
#include "XbeeCom.h"

FILE uartFileStream = FDEV_SETUP_STREAM(uart_printChar, NULL, _FDEV_SETUP_RW);


int main(void)
{
	XBee_communication_init();
	uart_init(UART_BAUD_SELECT(UART_BAUD_RATE_XBEE,F_CPU));
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	stdout = &uartFileStream;
		
	sei();
	printf("__RESTART__\r\n");

// 	AX18SetID(BROADCAST_ID, 55);
// 	//AX18SetReturnDelayTime(55, 1);
// 	
//AX18SetSpeed(55, 100);

AX18SetTorque(55, 1023);
_delay_ms(50);
	
	unsigned long setTorque;// = AX18GetTorque(55);
	
			unsigned char buffer[2];
			AX18FRead(55, AX_MAX_TORQUE_L, buffer, 2);

			setTorque = unsigned8ToUnsigned16(buffer[0], buffer[1]);

			printf("Received torque limit: %d\r\n", (int) setTorque);
	
	
	unsigned char direction = 0;
	
	startTickTimer();
	
	unsigned long pos = 1000;
	
	uint32_t count = 0;
	
	while(1) //infinite loop
	{
		while (uart_canRead()) {
			char receivedByte = uart_getc();
			uart_putc(receivedByte);
			if (XBee_communication_processSerialData(&receivedByte, 1) > 0) {
				if(XBee_communication_RxPacketsAvailable() > 0) {
					XBee_packet *packet;
					packet = XBee_communication_getRxPacket();
					
					if(packet->command == 0x00) {
							char servoId = packet->data[0];
							char servoPositionLowerByte = packet->data[1];
							char servoPositionHigherByte = packet->data[2];
							unsigned long servoPosition = unsigned8ToUnsigned16(servoPositionLowerByte, servoPositionHigherByte);
							AX18SetPosition(servoId, servoPosition);
					}
					
				}
			}
		}
	}
	
	stopTickTimer();
	return 0;
}

// 		if((direction==0 && pos > 990) || (direction==1 && pos < 310)) {
// 			//resetDiffTimer0();
//
// 			if(direction) {
// 				AX18SetPosition(55, 1000);
// 				direction = 0;
// 			} else {
// 				AX18SetPosition(55, 300);
// 				direction = 1;
// 			}
// 		}
//
// 		if(diffTimer1() >MS_TO_TICKS(20)) {
// 			resetDiffTimer1();
//
// 			unsigned char buffer[2];
// 			AX18FRead(55, AX_PRESENT_POSITION_L, buffer, 2);
//
// 			pos = unsigned8ToUnsigned16(buffer[0], buffer[1]);
//
// 			printf("POS: %d\r\n", (int) pos);
// 		}