#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#define UART_BAUD_RATE 1000000


#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdbool.h>

#include "AX18ServoDriver.h"
#include "IOPorts_ATMega.h"
#include "uart.h"

int main(void)
{
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	sei();
	_delay_ms(5000);
	
	AX18Speed(10, 100);
	AX18Speed(11, 100);
	AX18Speed(12, 100);
	
	AX18Speed(20, 100);
	AX18Speed(21, 100);
	AX18Speed(22, 100);
	
	AX18Speed(30, 100);
	AX18Speed(31, 100);
	AX18Speed(32, 100);
	
	AX18Speed(40, 100);
	AX18Speed(41, 100);
	AX18Speed(42, 100);
	
	AX18Speed(50, 100);
	AX18Speed(51, 100);
	AX18Speed(52, 100);
	
	AX18Speed(60, 100);
	AX18Speed(61, 100);
	AX18Speed(62, 100);
	
	AX18Position(10, 1023/2);
	AX18Position(11, 230);
	AX18Position(12, 500);
	
	AX18Position(30, 1023/2 - 280);
	AX18Position(31, 200);
	AX18Position(32, 520);
	
	AX18Position(50, 1023/2);
	AX18Position(51, 600);
	AX18Position(52, 500);
	
	
	AX18Position(20, 1023/2);
	AX18Position(21, 770);
	AX18Position(22, 500);
	
	AX18Position(40, 1023/2 - 280);
	AX18Position(41, 800);
	AX18Position(42, 520);
	
	AX18Position(60, 1023/2);
	AX18Position(61, 770);
	AX18Position(62, 500);
	
    while(1)
    {
        
    }
}