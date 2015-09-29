#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#define UART_BAUD_RATE 1000000

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdio.h>


#include "AX18ServoDriver.h"
#include "IOPorts_ATMega.h"
#include "uart.h"

FILE uartFileStream = FDEV_SETUP_STREAM(uart_printChar, NULL, _FDEV_SETUP_RW);


int main(void)
{
	
	uart_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	
	stdout = &uartFileStream;
	
	sei();
	
// 	for(int32_t baud  = 0; baud < 0xFE; baud++) {
// 		int32_t baudRate = 2000000/(baud+1);
// 		uart1_init(UART_BAUD_SELECT(baudRate,F_CPU));
// 		AX18SetBaudRate(BROADCAST_ID, 1000000);
// 		//printf("Baudrate tried: %ld\r\n", baudRate);
// 		_delay_ms(100);
// 		
// 	}
// 	printf("Finished baud rate is set to 1000000");
// 	while(1);
	AX18SetID(BROADCAST_ID, 55);
	AX18SetReturnDelayTime(55, 1);
	
	AX18SetSpeed(55, 250);
	while(1) //infinite loop
	{
		//printf("I am alive");
		//uart1_puts("Hallo");	
// 		uart1_RxDisable();
// 		uart1_TxEnable();
// 		_delay_ms(10);
// 		uart1_TxDisable();
// 		uart1_RxEnable();
// 		_delay_ms(10);
		AX18SetPosition(55, (unsigned long) 800);
		
// 		_delay_ms(1000);	
 		char buffer[2];
 		AX18FRead(55, AX_PRESENT_POSITION_L, buffer, 2);
		unsigned long pos = unsigned8ToUnsigned16(buffer[0], buffer[1]);
		printf("POS: %d\r\n", pos);
		_delay_ms(50);
	}
	
	return 0;
}